import os
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3

import Signup_Screen
import Dashboard_Screen
import Forget_Screen


# ==========================================
# DATABASE CONNECTION
# ==========================================

connection = sqlite3.connect("test1.db")
cursor = connection.cursor()

def forge():
    Forget_Screen.forgepass()

# ==========================================
# LOGIN WINDOW
# ==========================================

def loginnow():

    # --------------------------------------
    # LOGIN FUNCTION
    # --------------------------------------

    def save():

        error_label.config(
            text="",
            fg="red"
        )

        username = e1.get().strip()
        password = e2.get()

        # ==============================
        # VALIDATION
        # ==============================

        if username == "":
            error_label.config(
                text="⚠ Username cannot be empty."
            )
            return

        if " " in username:
            error_label.config(
                text="⚠ Username should not contain spaces."
            )
            return

        if password == "":
            error_label.config(
                text="⚠ Password cannot be empty."
            )
            return

        if len(password) < 8:
            error_label.config(
                text="⚠ Password must contain at least 8 characters."
            )
            return

        # ==============================
        # DATABASE CHECK
        # ==============================

        cursor.execute(
            "SELECT * FROM Signup WHERE Username=? AND Password=?",
            (username, password)
        )

        data = cursor.fetchone()

        if data:
            error_label.config(
            text="✓ Login Successful!",
            fg="green")

            root.after(800, lambda: (
            root.destroy(),
            Dashboard_Screen.call_dash()))
        else:
            error_label.config(
                text="⚠ Invalid Username or Password.",
                fg="red"
            )

    # --------------------------------------
    # SIGNUP BUTTON
    # --------------------------------------

    def signup_btn():

        Signup_Screen.signup()

    # ======================================
    # MAIN WINDOW
    # ======================================

    root = tk.Toplevel()

    root.title("Login")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}")

    root.state("zoomed")

    # ======================================
    # BACKGROUND IMAGE
    # ======================================

    bg_image = Image.open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "LoginScreenPic.png")
    )

    bg_image = bg_image.resize(
        (screen_width, screen_height)
    )

    photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(
        root,
        image=photo
    )

    bg_label.image = photo

    bg_label.place(
        x=0,
        y=0,
        relwidth=1,
        relheight=1
    )

    # ======================================
    # LABELS
    # ======================================

    l1 = tk.Label(
        root,
        text="Username: ",
        bg="white",
        fg="black",
        font=("Times New Roman", 20)
    )
    l1.place(x=850, y=310)

    l2 = tk.Label(
        root,
        text="Password: ",
        bg="white",
        fg="black",
        font=("Times New Roman", 20)
    )
    l2.place(x=850, y=425)

    l3 = tk.Label(root)
    l3.place(x=100, y=340)

    # ======================================
    # ENTRY BOXES
    # ======================================

    e1 = tk.Entry(
        root,
        width=25,
        bg="white",
        fg="black",
        font=("Segoe UI", 30)
    )
    e1.place(x=850, y=350)

    e2 = tk.Entry(
        root,
        width=25,
        bg="white",
        fg="black",
        font=("Segoe UI", 30),
        show="*"
    )
    e2.place(x=850, y=466)

    # ======================================
    # ERROR LABEL
    # ======================================

    error_label = tk.Label(
        root,
        text="",
        bg="white",
        fg="red",
        font=("Arial", 14, "bold")
    )

    error_label.place(x=850, y=520)

    # ======================================
    # REMEMBER ME
    # ======================================

    remember_var = tk.IntVar()

    r1 = tk.Checkbutton(
        root,
        text="Remember Me",
        variable=remember_var,
        bg="white",
        fg="black",
        font=("Copperblack", 18)
    )

    r1.place(x=840, y=540)

    # ======================================
    # LOGIN BUTTON
    # ======================================

    Log_btn = tk.Button(
        root,
        text=" -->  Login",
        bg="#1565C0",
        fg="white",
        font=("Arial", 20, "bold"),
        command=save,
        cursor="hand2",
        activebackground="#0D47A1",
        activeforeground="white"
    )

    Log_btn.place(
        x=850,
        y=590,
        width=540,
        height=70
    )


    # ======================================
    # SIGNUP SECTION
    # ======================================

    signup_label = tk.Label(
        root,
        text="--------------Don't have an account?--------------------",
        fg="blue",
        bg="white",
        font=("Copperblack", 18)
    )

    signup_label.place(x=850, y=670)

    sign_btn = tk.Button(
        root,
        text="Signup now",
        fg="blue",
        bg="white",
        font=("Copperblack", 15),
        command=signup_btn,
        cursor="hand2",
        bd=0,
        activebackground="white",
        activeforeground="blue"
    )

    sign_btn.place(x=1230, y=665)


    # ======================================
    # FORGOT PASSWORD BUTTON
    # ======================================

    fgtpass_btn = tk.Button(
        root,
        text="Forgot Password?        ",
        fg="blue",
        bg="white",
        font=("Copperblack", 15),
        cursor="hand2",
        bd=0,
        activebackground="white",
        activeforeground="blue",
        command=forge
    )

    fgtpass_btn.place(x=1200, y=540)

    # ======================================
    # MAIN LOOP
    # ======================================

    root.mainloop()