import os
import smtplib
import secrets
from email.message import EmailMessage
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
import Login_Screen

# ==========================================
# DATABASE CONNECTION
# ==========================================
def get_db_connection():
    connection = sqlite3.connect("test1.db")
    return connection, connection.cursor()


def login(current_window):
    current_window.destroy()
    Login_Screen.loginnow()


# ==========================================
# FORGOT PASSWORD WINDOW FUNCTION
# ==========================================
def forgepass():
    # Main Toplevel Window Setup
    root = tk.Toplevel()
    root.title("E-Commerce Customer Review Sentiment Analyser - Forgot Password")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}")
    root.state("zoomed")

    # Global variable inside function to securely hold OTP state
    generated_otp = None

    def send_otp():
        nonlocal generated_otp
        try:
            user_email = e1.get().strip()
        except tk.TclError:
            return  # Prevent error if window is closed

        error_label.config(text="", fg="red")

        if not user_email:
            error_label.config(text="⚠ Please enter your registered email address.")
            return

        connection, cursor = get_db_connection()
        cursor.execute("SELECT * FROM Signup WHERE Email=?", (user_email,))
        user_record = cursor.fetchone()
        connection.close()

        if not user_record:
            error_label.config(text="⚠ Email not found in database.")
            return

        SENDER_EMAIL = "kavyajoshi.702@gmail.com"
        APP_PASSWORD = os.environ.get("SENTIMENT_GMAIL_APP_PASSWORD", "")

        if not APP_PASSWORD:
            error_label.config(text="Email reset is not configured. Set SENTIMENT_GMAIL_APP_PASSWORD.", fg="red")
            return

        generated_otp = secrets.randbelow(900000) + 100000

        msg = EmailMessage()
        msg["Subject"] = "Password Reset OTP - Sentiment Analyser"
        msg["From"] = SENDER_EMAIL
        msg["To"] = user_email
        msg.set_content(
            f"Hello,\n\nHere is your OTP: {generated_otp} to reset your password. It is valid for 2 hours."
        )

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.starttls()
                smtp.login(SENDER_EMAIL, APP_PASSWORD)
                smtp.send_message(msg)
            error_label.config(text="✓ OTP sent successfully to your email!", fg="green")
        except Exception as e:
            error_label.config(text=f"⚠ Failed to send email: {e}", fg="red")

    def verify_otp():
        nonlocal generated_otp
        try:
            entered_otp = e2.get().strip()
        except tk.TclError:
            return

        error_label.config(text="", fg="red")

        if not generated_otp:
            error_label.config(text="⚠ Please request an OTP first.")
            return

        if entered_otp == str(generated_otp):
            error_label.config(text="✓ OTP Verified Successfully!", fg="green")
        else:
            error_label.config(text="⚠ Invalid OTP. Please try again.", fg="red")

    def reset_password():
        nonlocal generated_otp
        try:
            user_email = e1.get().strip()
            entered_otp = e2.get().strip()
            new_pass = e3.get()
            confirm_pass = e4.get()
        except tk.TclError:
            return

        error_label.config(text="", fg="red")

        if not user_email or not entered_otp or not new_pass or not confirm_pass:
            error_label.config(text="⚠ All fields are required.")
            return

        if entered_otp != str(generated_otp):
            error_label.config(text="⚠ Verify valid OTP before resetting password.", fg="red")
            return

        if len(new_pass) < 8:
            error_label.config(text="⚠ Password must contain at least 8 characters.", fg="red")
            return

        if new_pass != confirm_pass:
            error_label.config(text="⚠ New passwords do not match.", fg="red")
            return

        connection, cursor = get_db_connection()
        cursor.execute(
            "UPDATE Signup SET Password=?, Confirm_Password=? WHERE Email=?",
            (new_pass, confirm_pass, user_email),
        )
        connection.commit()
        connection.close()

        error_label.config(text="✓ Password reset successful! Redirecting...", fg="green")
        root.after(1500, lambda: login(root))

    # Background Image
    try:
        image = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "ForgetPassScreenPic.png"))
        image = image.resize((screen_width, screen_height))
        photo = ImageTk.PhotoImage(image)

        bg = tk.Label(root, image=photo)
        bg.image = photo
        bg.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception:
        root.configure(bg="#f0f0f0") # Fallback if image path issues happen

    # Widgets
    global e1, e2, e3, e4, error_label
    
    e1 = tk.Entry(root, width=45, bg="white", fg="black", font=("Segoe UI", 23))
    e1.place(x=637, y=110)

    btn_send_otp = tk.Button(
        root,
        text="                   Send OTP to registered email                      ",
        bg="#1565C0",
        fg="#FFFFFF",
        font=("Segoe UI", 13),
        command=send_otp,
        cursor="hand2",
    )
    btn_send_otp.place(x=637, y=165)

    e2 = tk.Entry(root, width=25, bg="white", fg="black", font=("Segoe UI", 23))
    e2.place(x=637, y=288)

    btn_verify_otp = tk.Button(
        root,
        text="                         Verify OTP                           ",
        bg="#1565C0",
        fg="#FFFFFF",
        font=("Segoe UI", 14),
        command=verify_otp,
        cursor="hand2",
    )
    btn_verify_otp.place(x=637, y=340)

    btn_resend_otp = tk.Button(
        root,
        text="      Resend code      ",
        fg="#1565C0",
        bg="#FFFFFF",
        font=("Segoe UI", 13),
        command=send_otp,
        cursor="hand2",
    )
    btn_resend_otp.place(x=1200, y=288)

    e3 = tk.Entry(root, width=43, bg="white", fg="black", font=("Segoe UI", 23), show="*")
    e3.place(x=637, y=440)

    e4 = tk.Entry(root, width=43, bg="white", fg="black", font=("Segoe UI", 23), show="*")
    e4.place(x=637, y=637)

    error_label = tk.Label(root, text="", bg="white", fg="red", font=("Arial", 14, "bold"))
    error_label.place(x=637, y=780)

    btn_reset = tk.Button(
        root, 
        text="                                                          Reset Password                                                              ",
        font=("Segoe UI", 14, "bold"),
        bg="blue",
        fg="white",
        command=reset_password,
        cursor="hand2",
    )
    btn_reset.place(x=637, y=690)

    btn_remem = tk.Button(
        root,
        text="         Remember your Password? Login now               ",
        font=("Segoe UI", 13, "bold"),
        bg="white",
        fg="blue",
        command=lambda: login(root),
        cursor="hand2",
        bd=0,
    )
    btn_remem.place(x=524, y=748)