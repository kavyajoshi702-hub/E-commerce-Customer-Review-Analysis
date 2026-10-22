import tkinter as tk
from tkinter import ttk, messagebox

from PIL import Image, ImageTk
import pandas as pd
import joblib
import os

import joblib
import pandas as pd

# 1. Load the hybrid model
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "sentiment_model.pkl")

# ADD THIS LINE:
model = joblib.load(model_path)


def main_task():

    root = tk.Toplevel()

    root.title("E-Commerce Customer Review Sentiment Analyser")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}")

    root.state("zoomed")


    # =====================================================
    # BACKGROUND IMAGE
    # =====================================================

    image = Image.open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "MainScreenPic.png")
    )

    image = image.resize(
        (screen_width, screen_height)
    )

    photo = ImageTk.PhotoImage(image)

    bg = tk.Label(
        root,
        image=photo
    )

    bg.image = photo

    bg.place(
        x=0,
        y=0,
        relwidth=1,
        relheight=1
    )

    # =====================================================
    # AGE GROUP
    # =====================================================

    tk.Label(
        root,
        text=" Age Group      ",
        font=("Arial",13,"bold"),
        bg="white"
    ).place(x=505,y=75)

    age_options = [
        "18-25",
        "26-35",
        "36-45",
        "46-55",
        "55+"
    ]

    cmb_age = ttk.Combobox(
        root,
        values=age_options,
        state="readonly",
        width=47,
        font=("Segoe UI",12,"bold")
    )

    cmb_age.set("Select Age Group")

    cmb_age.place(
        x=470,
        y=120
    )

    # =====================================================
    # REGION
    # =====================================================

    tk.Label(
        root,
        text=" Region       ",
        font=("Arial",13,"bold"),
        bg="white"
    ).place(x=1010,y=75)

    region_options = [
        "north",
        "south",
        "east",
        "west",
        "central"
    ]

    cmb_region = ttk.Combobox(
        root,
        values=region_options,
        state="readonly",
        width=47,
        font=("Segoe UI",12,"bold")
    )

    cmb_region.set("Select Region")

    cmb_region.place(
        x=980,
        y=120
    )
        # =====================================================
    # PRODUCT CATEGORY
    # =====================================================

    tk.Label(
        root,
        text="Product Category            ",
        font=("Arial",13,"bold"),
        bg="white"
    ).place(x=500,y=190)

    txt_product = tk.Entry(
        root,
        width=40,
        font=("Segoe UI",15),
        highlightthickness=2,
        highlightbackground="gray",
        highlightcolor="blue"
    )

    txt_product.place(x=470,y=225)

    # =====================================================
    # PURCHASE CHANNEL
    # =====================================================

    tk.Label(
        root,
        text=" Purchase Channel       ",
        font=("Arial",13,"bold"),
        bg="white"
    ).place(x=1015,y=190)

    purchase_var = tk.StringVar(value="online")

    tk.Radiobutton(
        root,
        text="Online",
        variable=purchase_var,
        value="online",
        bg="white",
        font=("Segoe UI",12,"bold")
    ).place(x=980,y=225)

    tk.Radiobutton(
        root,
        text="Offline",
        variable=purchase_var,
        value="offline",
        bg="white",
        font=("Segoe UI",12,"bold")
    ).place(x=1080,y=225)

    # =====================================================
    # PLATFORM
    # =====================================================

    tk.Label(
        root,
        text=" Platform       ",
        font=("Arial",13,"bold"),
        bg="white"
    ).place(x=500,y=300)

    txt_platform = tk.Entry(
        root,
        width=40,
        font=("Segoe UI",15),
        highlightthickness=2,
        highlightbackground="gray",
        highlightcolor="blue"
    )

    txt_platform.place(x=470,y=335)

    # =====================================================
    # CUSTOMER RATING
    # =====================================================

    tk.Label(
        root,
        text=" Customer Rating       ",
        font=("Arial",13,"bold"),
        bg="white"
    ).place(x=1015,y=300)

    rating_var = tk.IntVar(value=5)

    x = 980

    for i in range(5):

        tk.Radiobutton(
            root,
            text=str(i + 1),
            variable=rating_var,
            value=i + 1,
            bg="white",
            font=("Segoe UI",12,"bold")
        ).place(x=x, y=335)

        x += 55

    # =====================================================
    # RESPONSE TIME
    # =====================================================

    tk.Label(
        root,
        text=" Response Time (Hours)       ",
        font=("Arial",13,"bold"),
        bg="white"
    ).place(x=500,y=410)

    txt_time = tk.Entry(
        root,
        width=40,
        font=("Segoe UI",15),
        highlightthickness=2,
        highlightbackground="gray",
        highlightcolor="blue"
    )

    txt_time.place(x=470,y=445)

    # =====================================================
    # COMPLAINT REGISTERED
    # =====================================================

    tk.Label(
        root,
        text=" Complaint Registered        ",
        font=("Arial",13,"bold"),
        bg="white"
    ).place(x=1015,y=410)

    complaint_var = tk.StringVar(value="yes")

    tk.Radiobutton(
        root,
        text="Yes",
        variable=complaint_var,
        value="yes",
        bg="white",
        font=("Segoe UI",12,"bold")
    ).place(x=980,y=445)

    tk.Radiobutton(
        root,
        text="No",
        variable=complaint_var,
        value="no",
        bg="white",
        font=("Segoe UI",12,"bold")
    ).place(x=1050,y=445)

    # =====================================================
    # ISSUE RESOLVED
    # =====================================================

    tk.Label(
        root,
        text=" Issue Resolved         ",
        font=("Arial",13,"bold"),
        bg="white"
    ).place(x=500,y=520)

    resolve_var = tk.StringVar(value="yes")

    tk.Radiobutton(
        root,
        text="Yes",
        variable=resolve_var,
        value="yes",
        bg="white",
        font=("Segoe UI",12,"bold")
    ).place(x=470,y=550)

    tk.Radiobutton(
        root,
        text="No",
        variable=resolve_var,
        value="no",
        bg="white",
        font=("Segoe UI",12,"bold")
    ).place(x=530,y=550)

    tk.Radiobutton(
        root,
        text="In Processing",
        variable=resolve_var,
        value="in processing",
        bg="white",
        font=("Segoe UI",12,"bold")
    ).place(x=590,y=550)

    # =====================================================
    # REVIEW
    # =====================================================

    tk.Label(
        root,
        text=" Customer Review/Feedback                                ",
        font=("Arial",13,"bold"),
        bg="white"
    ).place(x=500,y=610)

    txt_review = tk.Text(
        root,
        width=52,
        height=4,
        font=("Segoe UI",12),
        highlightthickness=2,
        highlightbackground="gray",
        highlightcolor="blue"
    )

    txt_review.place(x=470,y=650)

    # =====================================================
    # RESULT FRAME
    # =====================================================

    result_frame = tk.Frame(
        root,
        bg="white",
        bd=2,
        relief="groove"
    )

    result_frame.place(
        x=1120,
        y=520,
        width=340,
        height=240
    )

    tk.Label(
        result_frame,
        text="SENTIMENT ANALYSIS RESULT",
        bg="white",
        fg="#003366",
        font=("Segoe UI",14,"bold")
    ).pack(pady=10)

    result_sentiment = tk.Label(
        result_frame,
        text="Waiting for prediction...",
        bg="white",
        fg="black",
        font=("Segoe UI",15,"bold")
    )

    result_sentiment.pack(pady=10)

    result_confidence = tk.Label(
        result_frame,
        text="",
        bg="white",
        fg="#444444",
        font=("Segoe UI",12)
    )

    result_confidence.pack()

    result_model = tk.Label(
        result_frame,
        text="Model : Random Forest",
        bg="white",
        fg="#1565C0",
        font=("Segoe UI",11,"bold")
    )

    result_model.pack(side="bottom", pady=10)
        # =====================================================
    # SUBMIT FUNCTION
    # =====================================================

    def submit():

        # -----------------------------
        # Read User Inputs
        # -----------------------------

        age = cmb_age.get().strip()
        region = cmb_region.get().strip()
        product = txt_product.get().strip()
        purchase = purchase_var.get().strip()
        platform = txt_platform.get().strip()
        rating = rating_var.get()
        response_time = txt_time.get().strip()
        complaint = complaint_var.get().strip()
        resolved = resolve_var.get().strip()
        review = txt_review.get("1.0", tk.END).strip()

        # -----------------------------
        # Validation
        # -----------------------------

        if age == "Select Age Group":
            messagebox.showerror(
                "Input Error",
                "Please select an Age Group."
            )
            return

        if region == "Select Region":
            messagebox.showerror(
                "Input Error",
                "Please select a Region."
            )
            return

        if product == "":
            messagebox.showerror(
                "Input Error",
                "Please enter Product Category."
            )
            return

        if platform == "":
            messagebox.showerror(
                "Input Error",
                "Please enter Platform."
            )
            return

        if review == "":
            messagebox.showerror(
                "Input Error",
                "Please enter Customer Review."
            )
            return

        if response_time == "":
            messagebox.showerror(
                "Input Error",
                "Please enter Response Time."
            )
            return

        try:
            response_time = float(response_time)
        except ValueError:
            messagebox.showerror(
                "Input Error",
                "Response Time must be numeric."
            )
            return

        # -----------------------------
        # Create DataFrame
        # -----------------------------

        input_data = pd.DataFrame([{
        "age_group": age,
        "region": region,
        "product_category": product,
        "purchase_channel": purchase,
        "platform": platform,
        "customer_rating": rating,
        "review_text": review,
        "response_time_hours":response_time,
        "complaint_registered": complaint,
        "issue_resolved": resolved
        }])
        print(input_data,"---------------------------------")
        # 4. Enforce strict column order matching the new X matrix
        feature_order = [
            "age_group", "region", "product_category", "purchase_channel", "platform",
            "customer_rating", "review_text", "response_time_hours",
            "complaint_registered", "issue_resolved"
        ]
        input_data = input_data[feature_order]




        # -----------------------------
        # Prediction
        # -----------------------------

        try:

            prediction = model.predict(input_data)[0]

            probability = model.predict_proba(input_data)

            confidence = probability.max() * 100

            sentiment = prediction

            # -------------------------
            # Display Result
            # -------------------------

            if str(sentiment).lower() == "positive":

                result_sentiment.config(
                    text="😊 POSITIVE",
                    fg="green"
                )

                result_confidence.config(
                    text=f"Confidence : {confidence:.2f}%"
                )

            elif str(sentiment).lower() == "negative":

                result_sentiment.config(
                    text="☹ NEGATIVE",
                    fg="red"
                )

                result_confidence.config(
                    text=f"Confidence : {confidence:.2f}%"
                )

            else:

                result_sentiment.config(
                    text="😐 NEUTRAL",
                    fg="#cc8800"
                )

                result_confidence.config(
                    text=f"Confidence : {confidence:.2f}%"
                )

        except Exception as e:

            messagebox.showerror(
                "Prediction Error",
                str(e)
            )
                # =====================================================
    # CLEAR FUNCTION
    # =====================================================

    def clear_fields():

        cmb_age.set("Select Age Group")
        cmb_region.set("Select Region")

        txt_product.delete(0, tk.END)

        purchase_var.set("online")

        txt_platform.delete(0, tk.END)

        rating_var.set(5)

        txt_time.delete(0, tk.END)

        complaint_var.set("yes")

        resolve_var.set("yes")

        txt_review.delete("1.0", tk.END)

        result_sentiment.config(
            text="Waiting for prediction...",
            fg="black"
        )

        result_confidence.config(text="")



    # =====================================================
    # BUTTONS
    # =====================================================

    analyse_btn = tk.Button(
        root,
        text="ANALYZE SENTIMENT",
        bg="#1565C0",
        fg="white",
        font=("Arial",18,"bold"),
        width=20,
        command=submit,
        cursor="hand2"
    )

    analyse_btn.place(
        x=800,
        y=760
    )


    clear_btn = tk.Button(
        root,
        text="CLEAR",
        bg="#1565C0",
        fg="white",
        font=("Arial",12,"bold"),
        width=10,
        command=clear_fields,
        cursor="hand2"
    )

    clear_btn.place(
        x=1200,
        y=770
    )

    # =====================================================
    # MAIN LOOP
    # =====================================================

    root.mainloop()