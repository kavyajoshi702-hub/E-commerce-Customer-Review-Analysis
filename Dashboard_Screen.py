import os
from tkinter import *
from PIL import Image, ImageTk,ImageOps
import Main_Screen

def call_dash():
    root = Toplevel()
    root.title("E-Commerce Customer Review Sentiment Analyser")
    screen_width = root.winfo_screenwidth() 
    screen_height = root.winfo_screenheight()

    root.geometry(str(screen_width)+"x"+str(screen_height))
    image = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Pictures", "DashboardScreenPic.png"))
    resized_image = image.resize((screen_width, screen_height))

    image = ImageOps.contain(
        image,
        (screen_width, screen_height)
    )

    img = ImageTk.PhotoImage(resized_image)

    label = Label(root,image=img)
    label.image = img
    label.place(x=0, y=0,relwidth=1, relheight=1)

    def predict_button():
        Main_Screen.main_task()

    back=Button(root,text="    START ANALYSIS      ",bg="Blue",fg="white",font=("Segoe UI", 13, "bold"),command=predict_button)
    back.place(x=1300, y=10)


    root.mainloop()