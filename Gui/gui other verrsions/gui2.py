# Lost and Found Application
# Main GUI

from tkinter import *
from PIL import Image, ImageTk
from colours import *

#this code is used to create the foundation of the window
ws = Tk()
ws.title("Lost and Found")
ws.geometry("1000x900")
ws.configure(bg=BG) 


def view_reported():
    print("Show reported items")  

def view_found():
    print("Show found items")

def about_app():
    print("Lost and Found App - made by Ali Hussain")

menubar = Menu(ws)

options_menu = Menu(menubar, tearoff=0)
options_menu.add_command(label="View Reported Items", command=view_reported)
options_menu.add_command(label="View Found Items", command=view_found)
options_menu.add_separator()
options_menu.add_command(label="Exit", command=ws.quit)
menubar.add_cascade(label="Options", menu=options_menu)

help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=about_app)
menubar.add_cascade(label="Help", menu=help_menu)

ws.config(menu=menubar)

# this code is for the greenish frame around all the components such as the report and found button and search, picture.

outer = Frame(ws, bg=BG)
outer.pack(expand=True, fill=BOTH)

#this code is so when ever i write "card" it will store that component into the frame of "outer"

card = Frame(
    outer,
    bg=CARD,
    highlightbackground=ACCENT,
    highlightthickness=13,
)
# this code is just for the placement of card in the middle of the window and also the size of the card is set to 560x740
card.place(relx=0.5, rely=0.5, anchor="center", width=560, height=740)

#this code is for the title of the application which is "Lost and Found" and also the font size and style is set to Arial, 22, bold and also the color of the text is set to black

Label(
    card,
    text="Lost and Found",
    bg=CARD,
    font=("Arial", 22, "bold")
).pack(pady=20)

#this code is for the search bar and the search button and also the placement of the search bar and the search button is set to the middle of the card and also the width of the search bar is set
# to 28 and the font size and style is set to Arial, 12

search_frame = Frame(card, bg=CARD)
search_frame.pack(pady=10)

search = Entry(search_frame, width=28, font=("Arial", 12))
search.grid(row=0, column=0, padx=(0, 8))

#thhis code is for the search bar button

Button(
    search_frame,
    text="Search",
    width=10,
    bg=FOUND_COLOR, 
    fg="white"
).grid(row=0, column=1)

#this code is for the image, resizeing the image and also the placement of the image in the middle of the card and also the size of the image is set to 200x200

img = Image.open("Lost and Found.png")
img = img.resize((200, 200))
image = ImageTk.PhotoImage(img)

picture = Label(card, image=image, bg=BG)
picture.pack(pady=20)

#this bit of code is for the report and found button and also the placement of the buttons in the middle of the card and also the size of the buttons is set to 18x3
#  and also the color of the buttons is set to red and green respectively

Button(
    card,
    text="REPORT ITEM",
    width=18,
    height=3,
    bg=REPORT_COLOR,
    fg="white"
).pack(pady=10)

Button(
    card,
    text="FOUND ITEM",
    width=18,
    height=3,
    bg=FOUND_COLOR,
    fg="white"
).pack()

ws.mainloop()