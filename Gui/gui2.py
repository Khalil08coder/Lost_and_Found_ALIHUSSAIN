# Lost and Found Application
# Main GUI

from tkinter import *

# Create window
ws = Tk()
ws.title("Lost and Found")
ws.geometry("1000x900")
ws.configure(bg="cyan")


side = Frame(ws, bg="white", width=120)
side.pack(side=LEFT, fill=Y)

Label(
    side,
    text="MENU",
    bg="white",
    font=("Arial", 14, "bold")
).pack(pady=20)

Button(side, text="Home", width=12, height=2).pack(pady=10)
Button(side, text="Profile", width=12, height=2).pack(pady=10)
Button(side, text="Settings", width=12, height=2).pack(pady=10)
Button(side, text="Help", width=12, height=2).pack(pady=10)

main = Frame(ws, bg="cyan")
main.pack(expand=True)

Label(
    main,
    text="Lost and Found System",
    bg="cyan",
    font=("Arial", 22, "bold")
).pack(pady=20)

# Search bar
search = Entry(main, width=35, font=("Arial", 12))
search.pack(pady=10)

Button(main, text="Search", width=12).pack()

# Display image
try:
    img = PhotoImage(file="image.png.png")
    pic = Label(main, image=img, bg="cyan")
    pic.pack(pady=20)
except:
    Label(
        main,
        text="Image not found.",
        bg="cyan",
        fg="red"
    ).pack(pady=20)

# Buttons
Button(
    main,
    text="REPORT ITEM",
    width=18,
    height=3,
    bg="red",
    fg="white"
).pack(pady=10)

Button(
    main,
    text="FOUND ITEM",
    width=18,
    height=3,
    bg="green",
    fg="white"
).pack()

ws.mainloop()