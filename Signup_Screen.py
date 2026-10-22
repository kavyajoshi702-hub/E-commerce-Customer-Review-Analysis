import os
import tkinter as tk
from PIL import Image, ImageTk
import sqlite3
import Login_Screen

# ==========================================
# DATABASE CONNECTION
# ==========================================

connection = sqlite3.connect("test1.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Signup(
    Full_name TEXT,
    Username TEXT,
    Email TEXT,
    Password TEXT,
    Confirm_Password TEXT
)
""")

connection.commit()

# ==========================================
# LOGIN BUTTON
# ==========================================

def login_btn():
    Login_Screen.loginnow()


# ==========================================
# SIGNUP WINDOW
# ==========================================

def signup():

    root = tk.Toplevel()

    root.title("Signup")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}")

    root.state("zoomed")

    # ======================================
    # BACKGROUND IMAGE
    # ======================================

    bg_image = Image.open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "SignUpScreenPic.png")
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
    # HOVER EFFECTS
    # ======================================

    def enter_signup(event):
        Sgn_btn.config(bg="#0D47A1")

    def leave_signup(event):
        Sgn_btn.config(bg="#1565C0")

    def enter_login(event):
        b4.config(
            bg="#E8E8E8"
        )

    def leave_login(event):
        b4.config(
            bg="white"
        )

    # ======================================
    # RETRIEVE FUNCTION
    # ======================================

    def retrieve():
               # ======================================
        # GET USER INPUT
        # ======================================

        full_name = e1.get().strip()
        username = e2.get().strip()
        email = e3.get().strip()
        password = e4.get()
        confirm_password = e5.get()

        error_label.config(text="", fg="red")

        # ======================================
        # VALIDATION
        # ======================================

        if full_name == "" or username == "" or email == "" or password == "" or confirm_password == "":
            error_label.config(text="⚠ All fields are required.")
            return

        if " " not in full_name:
            error_label.config(text="⚠ Enter both first and last name.")
            return

        if " " in username:
            error_label.config(text="⚠ Username cannot contain spaces.")
            return

        if len(username) < 4:
            error_label.config(text="⚠ Username must be at least 4 characters.")
            return

        if "@" not in email or "." not in email:
            error_label.config(text="⚠ Enter a valid email address.")
            return

        if len(password) < 8:
            error_label.config(text="⚠ Password must contain at least 8 characters.")
            return

        if password != confirm_password:
            error_label.config(text="⚠ Passwords do not match.")
            return

        if x.get() == 0:
            error_label.config(text="⚠ Please accept the Terms & Conditions.")
            return

        # ======================================
        # CHECK USERNAME
        # ======================================

        cursor.execute(
            "SELECT * FROM Signup WHERE Username=?",
            (username,)
        )

        if cursor.fetchone():
            error_label.config(text="⚠ Username already exists.")
            return

        # ======================================
        # CHECK EMAIL
        # ======================================

        cursor.execute(
            "SELECT * FROM Signup WHERE Email=?",
            (email,)
        )

        if cursor.fetchone():
            error_label.config(text="⚠ Email already registered.")
            return

        # ======================================
        # INSERT DATA
        # ======================================

        cursor.execute(
            "INSERT INTO Signup VALUES(?,?,?,?,?)",
            (
                full_name,
                username,
                email,
                password,
                confirm_password
            )
        )

        connection.commit()

        error_label.config(
            text="✓ Account created successfully!",
            fg="green"
        )

        # Automatically open Login after 1.5 seconds
        root.after(1500, login_btn)

    # ======================================
    # LABELS
    # ======================================

    l1 = tk.Label(root, text="Full Name: ", bg="white", fg="black", font=("Times New Roman", 13))
    l1.place(x=870, y=200)

    l2 = tk.Label(root, text="Username: ", bg="white", fg="black", font=("Times New Roman", 13))
    l2.place(x=870, y=295)

    l3 = tk.Label(root, text="Email: ", bg="white", fg="black", font=("Times New Roman", 13))
    l3.place(x=870, y=385)

    l4 = tk.Label(root, text="Password: ", bg="white", fg="black", font=("Times New Roman", 13))
    l4.place(x=870, y=485)

    l5 = tk.Label(root, text="Confirm Password: ", bg="white", fg="black", font=("Times New Roman", 13))
    l5.place(x=870, y=578)

    # ======================================
    # ENTRY FIELDS
    # ======================================

    e1 = tk.Entry(root, width=26, bg="white", fg="black", font=("Times New Roman", 30))
    e1.place(x=865, y=232)

    e2 = tk.Entry(root, width=26, bg="white", fg="black", font=("Times New Roman", 30))
    e2.place(x=865, y=327)

    e3 = tk.Entry(root, width=26, bg="white", fg="black", font=("Times New Roman", 30))
    e3.place(x=865, y=421)

    e4 = tk.Entry(root, width=26, bg="white", fg="black", font=("Times New Roman", 30), show="*")
    e4.place(x=865, y=516)

    e5 = tk.Entry(root, width=26, bg="white", fg="black", font=("Times New Roman", 30), show="*")
    e5.place(x=865, y=608)

    # ======================================
    # TERMS
    # ======================================

    x = tk.IntVar()

    t1 = tk.Checkbutton(
        root,
        text="I agree to Terms & Condition and Privacy policy",
        variable=x,
        font=("Times New Roman", 15),
        fg="black",
        bg="white"
    )

    t1.place(x=865, y=683)

    # ======================================
    # ERROR LABEL
    # ======================================

    error_label = tk.Label(
        root,
        text="",
        fg="red",
        bg="white",
        font=("Arial", 12, "bold")
    )

    error_label.place(x=865, y=780)

    # ======================================
    # SIGNUP BUTTON
    # ======================================

    Sgn_btn = tk.Button(
        root,
        text="SignUp",
        bg="#1565C0",
        fg="white",
        font=("Arial", 20, "bold"),
        command=retrieve,
        cursor="hand2",
        activebackground="#0D47A1",
        activeforeground="white"
    )

    Sgn_btn.place(
        x=865,
        y=715,
        width=525,
        height=70
    )

    Sgn_btn.bind("<Enter>", enter_signup)
    Sgn_btn.bind("<Leave>", leave_signup)

    # ======================================
    # LOGIN SECTION
    # ======================================

    l6 = tk.Label(
        root,
        text="-------------------------Already have an account?-------------------------------",
        bg="white",
        fg="black",
        font=("CopperBlack", 12)
    )

    l6.place(x=900, y=800)

    b4 = tk.Button(
        root,
        text="Login Now",
        bg="white",
        fg="black",
        font=("CopperBlack", 12),
        command=login_btn,
        cursor="hand2"
    )

    b4.place(x=1230, y=796)

    root.mainloop()