# import tkinter
from email import header
from tkinter import *
from PIL import Image, ImageTk
#create root window
root = Tk()
label = Label(root, text="geekforgeeks")
#rootwindow title and dimensions
root.title("welcome to geekforgeeks")
#set geimetry (widthxheight)
root.geometry('350x200')

lbl = Label(root, text="are you a geek?")
lbl.grid()



def clicked():
    lbl.configure(text="I just got clicked")

    btn = Button(root, text="click me",
    fg = "red", command=clicked)

    btn.grid(column=1, row=0)
#executor tkinter


    img = Image.open("AdobeStock_273861792_Preview.jpeg").resize((WINDOW_WIDTH,80))
    _img = ImageTk.PhotoImage(img)
    tk.Label(header, image=_img).pack()
    
import tkinter as tk

root = tk.Tk()
root.title("Counting Seconds")

button = tk.Button(root, text="Stop", width=25, command=root.destroy)
button.pack()



root.mainloop()


