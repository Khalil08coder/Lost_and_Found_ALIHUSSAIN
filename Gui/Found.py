from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from colours import *
from dbinformation import get_connection

#Fixed list used as a dropdown menu later on in the code
LOCATIONS = [
    "Rutherford",
    "Snell",
    "Mansfield",
    "Upham",
    "Batten",
    "Hillary",
    "Te Kanawa",
    "Kupe",
]


def open_found_window(parent):  #This function gets called apon when someone clicks the found button in the main window. It opens a new window where the user can report a found item. The function takes a parent parameter, which is the main window that called this function. This is used to make the new window a child of the main window, so it stays on top and is closed when the main window is closed.
    """Opens a new window where the user can report a found item."""

    # this code creates a new window
    found = Toplevel(parent)
    found.title("Report Found Item")
    found.geometry("400x420")
    found.configure(bg=BG)

    #this is for the title at the top
    Label(
        found,
        text="Report Found Item",
        bg=BG,
        font=("Arial", 18, "bold")
    ).pack(pady=15)

    # --- Item Name --- #this sits above a entry which is a text box a user can type into. The user can type the name of the item they have lost into this text box.
    Label(found, text="Item Name:", bg=BG, font=("Arial", 12)).pack()
    name_entry = Entry(found, width=25, font=("Arial", 12))
    name_entry.pack(pady=5)

    # --- Date Found ---
    Label(found, text="Date Found (MM/DD/YYYY):", bg=BG, font=("Arial", 12)).pack()
    date_entry = Entry(found, width=25, font=("Arial", 12))
    date_entry.pack(pady=5)

    # --- Location Found ---
    Label(found, text="Location Found:", bg=BG, font=("Arial", 12)).pack()
    location_entry = ttk.Combobox(found, values=LOCATIONS, width=22, state="readonly")
    location_entry.pack(pady=5)

    # --- Item Value ---
    Label(found, text="Item Value ($):", bg=BG, font=("Arial", 12)).pack()
    value_entry = Entry(found, width=25, font=("Arial", 12))
    value_entry.pack(pady=5)

    # --- Submit Button --- # this code is for the submit button. Defined inside Open_report_window meaning it has direct access to name entry and date entry.
    def submit_found():
        item_name = name_entry.get()
        date_text = date_entry.get()
        location = location_entry.get()
        value_text = value_entry.get()

        if item_name == "": # it then see if the input is missing, if so then it shows the message box error
            messagebox.showerror("Missing Info", "Please enter the item name.")
            return

        if location == "":
            messagebox.showerror("Missing Info", "Please select a location.")
            return

        try: #this code is different as it checks if the date is in the correct formart, the strptime function is used to convert the typed text into a real date. If it is unable to  using the formart m/d/yyyy then it shows a box error.
            parsed_date = datetime.strptime(date_text, "%m/%d/%Y")
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter the date as MM/DD/YYYY.")
            return

        item_value = None #the value is optional, so if the user leaves it blank, it will be stored as NULL in the database. If the user enters a value, it will be converted to a float and stored in the database. If the user enters a non-numeric value, an error message will be shown.
        if value_text != "":
            try:
                item_value = float(value_text)
            except ValueError:
                messagebox.showerror("Invalid Value", "Item value must be a number.")
                return

        date_found = parsed_date.strftime("%m/%d/%y ") # Convert to MM/DD/YYYY format #strfttime is the reverse of strptime, it converts a date object into a string in the specified format. This is done so that the date is stored in the database in a consistent format.

        conn = get_connection()  # this code saves it to the database. get connection opens the database, cur.execute runs the SQL command, and conn.commit saves the changes to the database. conn.close closes the connection to the database.
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO ItemTable (ItemName, DateFound, LocationFound, ItemValue, ItemStatus)
            VALUES (?, ?, ?, ?, 'Found')
        """, (item_name, date_found, location, item_value))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"'{item_name}' has been reported as found.")
        found.destroy()

    Button(
        found,
        text="SUBMIT FOUND ITEM",
        width=18,
        height=2,
        bg=FOUND_COLOR,
        fg="white",
        command=submit_found #tells tkinter to call upon the submit_found function when the button is clicked.
    ).pack(pady=20)