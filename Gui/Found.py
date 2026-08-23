from tkinter import Toplevel, Label, Entry, Button
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from colours import BG, FOUND_COLOR
from constants import (
    LOCATIONS, FONT_LABEL, FONT_TITLE, FORM_WINDOW_SIZE, LOCATION_WIDTH
)
from dbinformation import insert_found_item
from Validate import validate_item_name, validate_not_future_date


def open_found_window(parent):
    """Opens a new window where the user can report a found item.

    parent is the main window that called this function, so the new
    window stays on top of it and closes when the main window closes.
    """
    found = Toplevel(parent)
    found.title("Report Found Item")
    found.geometry(FORM_WINDOW_SIZE)
    found.configure(bg=BG)

    Label(
        found,
        text="Report Found Item",
        bg=BG,
        font=FONT_TITLE
    ).pack(pady=15)

    # --- Item Name ---
    Label(found, text="Item Name:", bg=BG, font=FONT_LABEL).pack()
    name_entry = Entry(found, width=25, font=FONT_LABEL)
    name_entry.pack(pady=5)

    # --- Date Found ---
    Label(
        found,
        text="Date Found (MM/DD/YYYY):",
        bg=BG,
        font=FONT_LABEL
    ).pack()
    date_entry = Entry(found, width=25, font=FONT_LABEL)
    date_entry.pack(pady=5)

    # --- Location Found ---
    Label(found, text="Location Found:", bg=BG, font=FONT_LABEL).pack()
    location_entry = ttk.Combobox(
        found, values=LOCATIONS, width=LOCATION_WIDTH, state="readonly"
    )
    location_entry.pack(pady=5)

    # --- Item Value ---
    Label(found, text="Item Value ($):", bg=BG, font=FONT_LABEL).pack()
    value_entry = Entry(found, width=25, font=FONT_LABEL)
    value_entry.pack(pady=5)

    def submit_found():
        """Reads the form, validates it, and saves the found report."""
        item_name = name_entry.get().strip()
        date_text = date_entry.get().strip()
        location = location_entry.get()
        value_text = value_entry.get().strip()

        is_valid, error_message = validate_item_name(item_name)
        if not is_valid:
            messagebox.showerror("Invalid Name", error_message)
            return

        if location == "":
            messagebox.showerror(
                "Missing Info", "Please select a location."
            )
            return

        try:
            parsed_date = datetime.strptime(date_text, "%m/%d/%Y")
        except ValueError:
            messagebox.showerror(
                "Invalid Date", "Please enter the date as MM/DD/YYYY."
            )
            return

        is_valid, error_message = validate_not_future_date(parsed_date)
        if not is_valid:
            messagebox.showerror("Invalid Date", error_message)
            return

        item_value = None
        if value_text != "":
            try:
                item_value = float(value_text)
            except ValueError:
                messagebox.showerror(
                    "Invalid Value", "Item value must be a number."
                )
                return

        date_found = parsed_date.strftime("%m/%d/%y")

        # GUI doesn't talk to the database calls this one
        # function from dbinformation.py instead.
        insert_found_item(item_name, date_found, location, item_value)

        messagebox.showinfo(
            "Success", f"'{item_name}' has been reported as found."
        )
        found.destroy()

    Button(
        found,
        text="SUBMIT FOUND ITEM",
        width=18,
        height=2,
        bg=FOUND_COLOR,
        fg="white",
        command=submit_found
    ).pack(pady=20)
