import os
import tkinter as tk
from PIL import Image, ImageTk

import Login_Screen
import About_Screen


# ===========================================
# FUNCTIONS
# ===========================================

def open_login():
    Login_Screen.loginnow()


def open_about():
    About_Screen.call_ab()


# ===========================================
# MAIN WINDOW
# ===========================================

root = tk.Tk()

root.title("E-Commerce Customer Review Sentiment Analyser")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")

# Opens maximized on Windows
root.state("zoomed")


# ===========================================
# BACKGROUND IMAGE
# ===========================================

bg_image = Image.open(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "HomeScreenPic.png")
)

bg_image = bg_image.resize((screen_width, screen_height))

bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)

bg_label.image = bg_photo

bg_label.place(
    x=0,
    y=0,
    relwidth=1,
    relheight=1
)



# ===========================================
# BUTTONS
# ===========================================

start_analyse = tk.Button(
    root,
    text=" Get Started ",
    bg="#1565C0",
    fg="white",
    font=("Segoe UI", 20, "bold"),
    command=open_login,
    cursor="hand2",
    activebackground="#0D47A1",
    activeforeground="white"
)

start_analyse.place(
    x=775,
    y=370,
    width=582,
    height=95
)


about = tk.Button(
    root,
    text="About Us",
    bg="#1565C0",
    fg="white",
    font=("Segoe UI", 13, "bold"),
    command=open_about,
    cursor="hand2",
    activebackground="#0D47A1",
    activeforeground="white"
)

about.place(
    x=1400,
    y=10
)


# ===========================================
# MAIN LOOP
# ===========================================

root.mainloop()