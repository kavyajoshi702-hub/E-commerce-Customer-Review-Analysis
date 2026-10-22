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
print("HYBRID DATASET INFORMATION")
print("=" * 60)
print("\nDataset Shape:", data.shape)

# =====================================================
# PREPARE FEATURES (KEEPING RATINGS & COMPLAINTS)
# =====================================================
# We ONLY drop the target (sentiment) and the useless unique identifier (customer_id)
X = data.drop(columns=[
    "sentiment",
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

print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

# =====================================================
# UPDATED PREPROCESSING PIPELINE
# =====================================================
# Added complaint_registered and issue_resolved here
categorical_features = [
    "age_group",
    "region",
    "product_category",
    "purchase_channel",
    "platform",
    "complaint_registered",
    "issue_resolved"
]

# Added customer_rating here as a numerical feature
numeric_features = [
    "response_time_hours",
    "customer_rating"
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

print("\nTraining Hybrid Random Forest Model...")
model.fit(X_train, y_train)

print("Training Completed!")

# =====================================================
# PERFORMANCE METRICS
# =====================================================
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="weighted", zero_division=0)
recall = recall_score(y_test, y_pred, average="weighted", zero_division=0)
f1 = f1_score(y_test, y_pred, average="weighted", zero_division=0)

print("\n" + "=" * 60)
print("MODEL PERFORMANCE (WITH METADATA FEATURES)")
print("=" * 60)
print(f"Accuracy : {accuracy*100:.2f}%")
print(f"Precision: {precision*100:.2f}%")
print(f"Recall   : {recall*100:.2f}%")
print(f"F1 Score : {f1*100:.2f}%")

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# =====================================================
# SAVE HYBRID MODEL
# =====================================================
joblib.dump(model, "sentiment_model.pkl")
print("\nHybrid model saved successfully as sentiment_model.pkl")

