"""
Lost and Found App
Main Gui for my lost and found system
Displays a window and lets the user either report an item or find one.
"""

from tkinter import Tk, Toplevel, Frame, Label, Button, Menu
from tkinter import BOTH
from tkinter import ttk  # tree view
from tkinter import messagebox
from PIL import Image, ImageTk
from colours import BG, ACCENT, REPORT_COLOR, FOUND_COLOR
from constants import (
    MAIN_WINDOW_WIDTH, MAIN_WINDOW_HEIGHT, TABLE_WINDOW_SIZE
)
from dbinformation import get_reported_items, get_found_items
from Report import open_report_window
from Found import open_found_window

# Width for each Treeview column, derived from the window width and the
# number of columns in that table, instead of a guessed literal like
# 110. If a column is ever added or removed, every column automatically
# resizes to still fill the table width evenly.
TABLE_WIDTH = int(TABLE_WINDOW_SIZE.split("x")[0])


def _column_width(num_columns, padding=30):
    """Derives an even column width from the table window's width."""
    return (TABLE_WIDTH - padding) // num_columns


def launch_main_app():
    """Builds and shows the main Lost and Found window.

    Wrapped in a function (rather than running at import time) so
    Login.py can call it AFTER a successful login instead of it
    opening automatically.
    """
    ws = Tk()
    ws.title("Lost and Found")
    ws.geometry(f"{MAIN_WINDOW_WIDTH}x{MAIN_WINDOW_HEIGHT}")
    ws.configure(bg=BG)

    def view_reported():
        """Opens a window showing all currently reported (lost) items,
        pulled live from the database into a Treeview table."""
        win = Toplevel(ws)
        win.title("Reported Items")
        win.geometry(TABLE_WINDOW_SIZE)
        win.configure(bg=BG)

        Label(
            win, text="Reported (Lost) Items", bg=BG,
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        cols = ("ItemID", "Item Name", "Date Lost", "Location Lost",
                "Value")
        # "headings" hides the default leftmost tree column so it
        # looks like a plain table, not a nested folder tree.
        tree = ttk.Treeview(win, columns=cols, show="headings", height=12)
        col_width = _column_width(len(cols))
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=col_width)
        tree.pack(padx=15, pady=10, fill=BOTH, expand=True)

        for row in get_reported_items():
            tree.insert("", "end", values=row)

    def view_found():
        """Same idea as view_reported(), for found items."""
        win = Toplevel(ws)
        win.title("Found Items")
        win.geometry(TABLE_WINDOW_SIZE)
        win.configure(bg=BG)

        Label(
            win, text="Found Items", bg=BG,
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        cols = ("ItemID", "Item Name", "Date Found", "Location Found",
                "Value")
        tree = ttk.Treeview(win, columns=cols, show="headings", height=12)
        col_width = _column_width(len(cols))
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=col_width)
        tree.pack(padx=15, pady=10, fill=BOTH, expand=True)

        for row in get_found_items():
            tree.insert("", "end", values=row)

    def about_app():
        """Shows a message box with information about the app."""
        messagebox.showinfo(
            "About",
            "Lost and Found Application\n\n"
            "Built with Python + Tkinter + SQLite\n"
            "Created by Ali Hussain\n\n"
            "Tracks reported and found items around school."
        )

    # Menu bar setup adapted from the teacher's example code.
    menubar = Menu(ws)

    # tearoff=0 stops the menu from being torn off into its own window.
    options_menu = Menu(menubar, tearoff=0)
    options_menu.add_command(
        label="View Reported Items", command=view_reported
    )
    options_menu.add_command(label="View Found Items", command=view_found)
    options_menu.add_separator()
    options_menu.add_command(label="Exit", command=ws.quit)
    menubar.add_cascade(label="Options", menu=options_menu)

    help_menu = Menu(menubar, tearoff=0)
    help_menu.add_command(label="About", command=about_app)
    menubar.add_cascade(label="Help", menu=help_menu)

    ws.config(menu=menubar)

    # Outer frame + the green-bordered "card" that holds everything.
    outer = Frame(ws, bg=BG)
    outer.pack(expand=True, fill=BOTH)

    card = Frame(
        outer,
        bg=BG,
        highlightbackground=ACCENT,
        highlightthickness=13,
    )
    card.place(
        relx=0.5, rely=0.5, anchor="center",
        width=MAIN_WINDOW_WIDTH, height=MAIN_WINDOW_HEIGHT
    )

    Label(
        card,
        text="Lost and Found",
        bg=BG,
        font=("COMIC", 22, "bold")
    ).pack(pady=20)

    # Logo image
    img = Image.open("Lost_And_Found.png")
    img = img.resize((200, 150))
    image = ImageTk.PhotoImage(img)

    picture = Label(card, image=image, bg=BG)
    picture.image = image
    picture.pack(pady=20)

    # Report and Found buttons
    Button(
        card,
        text="REPORT ITEM",
        width=18,
        height=3,
        bg=REPORT_COLOR,
        fg="white",
        command=lambda: open_report_window(ws)
    ).pack(pady=10)

    Button(
        card,
        text="FOUND ITEM",
        width=18,
        height=3,
        bg=FOUND_COLOR,
        fg="white",
        command=lambda: open_found_window(ws)
    ).pack()

    ws.mainloop()


# Only run automatically if this file is run directly, not when imported.
if __name__ == "__main__":
    launch_main_app()
