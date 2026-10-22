import os
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    ConfusionMatrixDisplay
)

# =====================================================
# LOAD DATA
# =====================================================

data = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Customer_Sentiment_30000.csv"))

print("=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

print("\nDataset Shape:", data.shape)
print("\nFirst 5 Records:")
print(data.head())

print("\nDuplicate Reviews:",
      data["review_text"].duplicated().sum())

print("Unique Reviews:",
      data["review_text"].nunique())

print("\nSentiment Distribution")
print(data["sentiment"].value_counts())

# =====================================================
# CHECK FOR DATA LEAKAGE
# =====================================================

print("\nRating vs Sentiment")
print(pd.crosstab(data["customer_rating"], data["sentiment"]))

print("\nComplaint vs Sentiment")
print(pd.crosstab(data["complaint_registered"], data["sentiment"]))

print("\nIssue Resolved vs Sentiment")
print(pd.crosstab(data["issue_resolved"], data["sentiment"]))

# =====================================================
# REMOVE LEAKAGE COLUMNS
# =====================================================

X = data.drop(columns=[
    "sentiment",
    "customer_rating",
    "complaint_registered",
    "issue_resolved",
    "customer_id"
])

y = data["sentiment"]

# =====================================================
# TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
    shuffle=True
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# =====================================================
# PREPROCESSING
# =====================================================

categorical_features = [
    "age_group",
    "region",
    "product_category",
    "purchase_channel",
    "platform"
]

numeric_features = [
    "response_time_hours"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "text",
            TfidfVectorizer(
                stop_words="english",
                max_features=5000,
                ngram_range=(1, 2)
            ),
            "review_text"
        ),
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "num",
            "passthrough",
            numeric_features
        )
    ]
)

# =====================================================
# RANDOM FOREST MODEL
# =====================================================

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(
        n_estimators=200,
        max_depth=20,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    ))
])

print("\nTraining Random Forest Model...")

model.fit(X_train, y_train)

print("Training Completed!")

# =====================================================
# PREDICTION
# =====================================================

y_pred = model.predict(X_test)

# =====================================================
# PERFORMANCE METRICS
# =====================================================

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)
recall = recall_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)
f1 = f1_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"Accuracy : {accuracy*100:.2f}%")
print(f"Precision: {precision*100:.2f}%")
print(f"Recall   : {recall*100:.2f}%")
print(f"F1 Score : {f1*100:.2f}%")

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# =====================================================
# CONFUSION MATRIX
# =====================================================

ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred,
    cmap="Blues"
)

plt.title("Confusion Matrix")
plt.show()

# =====================================================
# CROSS VALIDATION
# =====================================================

print("\nRunning 5-Fold Cross Validation...")

cv_scores = cross_val_score(
    model,
    X,
    y,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

print("\nCross Validation Scores")
print(cv_scores)

print("\nMean Accuracy :", cv_scores.mean())
print("Std Deviation :", cv_scores.std())

# =====================================================
# PERFORMANCE GRAPH
# =====================================================

metrics = ["Accuracy", "Precision", "Recall", "F1 Score"]
values = [accuracy, precision, recall, f1]

plt.figure(figsize=(8,5))

bars = plt.bar(metrics, values)

plt.ylim(0,1)

for bar in bars:
    plt.text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height()+0.01,
        f"{bar.get_height()*100:.2f}%",
        ha="center"
    )

plt.title("Random Forest Performance")
plt.ylabel("Score")

plt.show()

# =====================================================
# SENTIMENT DISTRIBUTION
# =====================================================

plt.figure(figsize=(6,4))

data["sentiment"].value_counts().plot(
    kind="bar"
)

plt.title("Sentiment Distribution")
plt.ylabel("Count")

plt.show()

# =====================================================
# FEATURE IMPORTANCE
# =====================================================

feature_names = model.named_steps["preprocessor"].get_feature_names_out()

importances = model.named_steps["classifier"].feature_importances_

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importances
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 20 Important Features\n")
print(importance_df.head(20))

# =====================================================
# SAVE MODEL
# =====================================================

joblib.dump(model, "sentiment_model.pkl")

print("\nModel saved successfully as sentiment_model.pkl")