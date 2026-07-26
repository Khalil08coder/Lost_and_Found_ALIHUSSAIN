#This code was my first attempt at creating a gui using my wireframe as inspriation. The code includes a sidebar and main navigator buttons for reporting or finding an item.

from tkinter import *

ws = Tk()
ws.geometry("1000x1000")
ws.title("PythonGuides")
ws["bg"] = "cyan"

f = ("Times", 12)

def nextPage():
    print("Found")

def prevPage():
      print("Report")


side = Frame(
    ws,
    bg="white",
    width=50
)
side.pack(side=LEFT, fill=Y)

Button(
    side,
    text="home",
    width=3,
    height=2
).pack(pady=25)

Button(
    side,
    text="inventory",
    width=3,
    height=2
).pack(pady=25)

Button(
    side,
    text="setting",
    width=3,
    height=2
).pack(pady=25)

Button(
    side,
    text="help",
    width=3,
    height=2
).pack(pady=25)


main = Frame(ws, bg="cyan")
main.pack(expand=True)

Button(
    main,
    text="REPORT ITEM",
    font=f,
    width=15,
    height=5,
    command=prevPage
).pack(pady=40)

Button(
    main,
    text="FOUND ITEM",
    font=f,
    width=15,
    height=5,
    command=nextPage
).pack()

ws.mainloop()