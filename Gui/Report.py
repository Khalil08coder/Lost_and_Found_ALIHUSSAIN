from tkinter import Toplevel, Label, Entry, Button
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from colours import BG, REPORT_COLOR
from constants import (
    LOCATIONS, FONT_LABEL, FONT_TITLE, FORM_WINDOW_SIZE, LOCATION_WIDTH
)
from dbinformation import insert_reported_item
from Validate import validate_item_name, validate_not_future_date


def open_report_window(parent):
    """Opens a new window where the user can report a lost item.
    parent is the main window that called this function, so the new
    window stays on top of it and closes when the main window closes.
    """
    report = Toplevel(parent)
    report.title("Report Lost Item")
    report.geometry(FORM_WINDOW_SIZE)
    report.configure(bg=BG)

    Label(
        report,
        text="Report Lost Item",
        bg=BG,
        font=FONT_TITLE
    ).pack(pady=15)

    # --- Item Name ---
    Label(report, text="Item Name:", bg=BG, font=FONT_LABEL).pack()
    name_entry = Entry(report, width=25, font=FONT_LABEL)
    name_entry.pack(pady=5)

    # --- Date Lost ---
    Label(
        report,
        text="Date Lost (MM/DD/YYYY):",
        bg=BG,
        font=FONT_LABEL
    ).pack()
    date_entry = Entry(report, width=25, font=FONT_LABEL)
    date_entry.pack(pady=5)

    # --- Location Lost ---
    Label(report, text="Location Lost:", bg=BG, font=FONT_LABEL).pack()
    location_entry = ttk.Combobox(
        report, values=LOCATIONS, width=LOCATION_WIDTH, state="readonly"
    )
    location_entry.pack(pady=5)

    # --- Item Value ---
    Label(report, text="Item Value ($):", bg=BG, font=FONT_LABEL).pack()
    value_entry = Entry(report, width=25, font=FONT_LABEL)
    value_entry.pack(pady=5)

    def submit_report():
        """Reads the form, validates it, and saves the report."""
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

        date_lost = parsed_date.strftime("%m/%d/%Y")

        # GUI doesn't talk to the database,  it calls this one
        # function from dbinformation.py instead.
        insert_reported_item(item_name, date_lost, location, item_value)

        messagebox.showinfo(
            "Success", f"'{item_name}' has been reported as lost."
        )
        report.destroy()

    Button(
        report,
        text="SUBMIT REPORT",
        width=18,
        height=2,
        bg=REPORT_COLOR,
        fg="white",
        command=submit_report
        ).pack(pady=20)
