# Lost and Found Application
# Main GUI

from tkinter import *
from tkinter import ttk # tree view
from tkinter import messagebox
from PIL import Image, ImageTk
from colours import *
from dbinformation import get_reported_items, get_found_items #pulls in two functions from the database.py file that are used to get the reported and found items from the database


#this code is used to create the foundation of the window
ws = Tk()
ws.title("Lost and Found") 
ws.geometry("560x560")
ws.configure(bg=BG)


# This code ise for the menu and was used via the help of the internet and also the code is used to create a menu bar with options such as view reported items, view found items, exit and about. The menu bar is placed at the top of the window and also the color of the menu bar is set to white.
# these open a new window (Toplevel) and show a table (Treeview)
#although this was used to create via the help of hte internet i have put the video i used to help me out in the development log
# pulling live data out of the SQLite database

def view_reported():
    win = Toplevel(ws) #top level is used to create a new window on top of the main window
    win.title("Reported Items") #this is the same as the main window but it uses "win" instead of "ws" and also the title of the window is set to "Reported Items"
    win.geometry("650x400")
    win.configure(bg=BG)

    Label(win, text="Reported (Lost) Items", bg=BG,   
          font=("Arial", 16, "bold")).pack(pady=10)

    cols = ("ItemID", "Item Name", "Date Lost", "Location Lost", "Value") #cols means the tables columns
    tree = ttk.Treeview(win, columns=cols, show="headings", height=12) #creates the actual table widget #show="headings" hides the default leftmost "tree" column so it looks like a plain table, not a nested folder tree.
    for col in cols: 
        tree.heading(col, text=col)
        tree.column(col, width=110)
    tree.pack(padx=15, pady=10, fill=BOTH, expand=True)

    for row in get_reported_items(): #runs SQL query # and returns lists of rows, each row is a tuple of values for each column in the table. #this code is used to insert the data into the treeview widget and also the data is inserted into the treeview widget in the form of a list of tuples.
        tree.insert("", "end", values=row)


def view_found(): #basically the same as the view reported
    win = Toplevel(ws)
    win.title("Found Items")
    win.geometry("650x400")
    win.configure(bg=BG)

    Label(win, text="Found Items", bg=BG,
          font=("Arial", 16, "bold")).pack(pady=10)

    cols = ("ItemID", "Item Name", "Date Found", "Location Found", "Value")
    tree = ttk.Treeview(win, columns=cols, show="headings", height=12)
    for col in cols:
        tree.heading(col, text=col)
        tree.column(col, width=110)
    tree.pack(padx=15, pady=10, fill=BOTH, expand=True)

    for row in get_found_items():
        tree.insert("", "end", values=row)


def about_app(): #this shows a message box and tells the information about the application
    messagebox.showinfo(
        "About",
        "Lost and Found Application\n\n"
        "Built with Python + Tkinter + SQLite\n"
        "Created by Ali Hussain\n\n"
        "Tracks reported and found items around school."
    )

#code copied from teachers
menubar = Menu(ws) #menubar and is attached to the main window via ws

options_menu = Menu(menubar, tearoff=0) #tearoff=0 means that the menu cannot be torn off and made into a separate window
options_menu.add_command(label="View Reported Items", command=view_reported)# the add command makes it so when you click on the "View Reported Items" option in the menu, it will call the view_reported function and open a new window with the reported items
options_menu.add_command(label="View Found Items", command=view_found)
options_menu.add_separator() #creates a line between the commands in the menu
options_menu.add_command(label="Exit", command=ws.quit) 
menubar.add_cascade(label="Options", menu=options_menu) # what attaches the dropdown menu

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
    bg=BG,
    highlightbackground=ACCENT,
    highlightthickness=13,
)
# this code is just for the placement of card in the middle of the window and also the size of the card is set to 560x560
card.place(relx=0.5, rely=0.5, anchor="center", width=560, height=560)

#this code is for the title of the application which is "Lost and Found" and also the font size and style is set to Arial, 22, bold and also the color of the text is set to black

Label(
    card,
    text="Lost and Found",
    bg=BG,
    font=("COMIC", 22, "bold")
).pack(pady=20)

#this code is for the search bar and the search button and also the placement of the search bar and the search button is set to the middle of the card and also the width of the search bar is set
# to 28 and the font size and style is set to Arial, 12

search_frame = Frame(card, bg=BG)
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
img = img.resize((200, 150))
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
