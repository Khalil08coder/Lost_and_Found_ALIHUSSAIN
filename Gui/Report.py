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


def open_report_window(parent):  #This function gets called apon when someone clicks the report button in the main window. It opens a new window where the user can report a lost item. The function takes a parent parameter, which is the main window that called this function. This is used to make the new window a child of the main window, so it stays on top and is closed when the main window is closed.
    """Opens a new window where the user can report a lost item."""

    # this code creates a new window
    report = Toplevel(parent)
    report.title("Report Lost Item")
    report.geometry("400x420")
    report.configure(bg=BG)

    #this is for the title at the top
    Label(
        report,
        text="Report Lost Item",
        bg=BG,
        font=("Arial", 18, "bold")
    ).pack(pady=15)

    # --- Item Name ---  #this sits above a entry which is a text box a user can type into. The user can type the name of the item they have lost into this text box.
    Label(report, text="Item Name:", bg=BG, font=("Arial", 12)).pack()
    nameEntry = Entry(report, width=25, font=("Arial", 12))
    nameEntry.pack(pady=5)

    # --- Date Lost --- 
    Label(report, text="Date Lost (MM/DD/YYYY):", bg=BG, font=("Arial", 12)).pack()
    date_entry = Entry(report, width=25, font=("Arial", 12))
    date_entry.pack(pady=5)

    # --- Location Lost ---
    Label(report, text="Location Lost:", bg=BG, font=("Arial", 12)).pack()
    location_entry = ttk.Combobox(report, values=LOCATIONS, width=22, state="readonly")
    location_entry.pack(pady=5)

    # --- Item Value ---
    Label(report, text="Item Value ($):", bg=BG, font=("Arial", 12)).pack()
    value_entry = Entry(report, width=25, font=("Arial", 12))
    value_entry.pack(pady=5)


    # --- Submit Button ---  # this code is for the submit button. Defined inside Open_report_window meaning it has direct access to name entry and date entry.
    def submit_report():
        item_name = nameEntry.get() #it reads the inputs
        date_text = date_entry.get()
        location = location_entry.get()
        value_text = value_entry.get()

        if item_name == "": # it then see if the input is missing, if so then it shows the message box error.
            messagebox.showerror("Missing Info", "Please enter the item name.")
            return

        if location == "":
            messagebox.showerror("Missing Info", "Please select a location.")
            return

        try: #this code is different as it checks if the date is in the correct formart, the strptime function is used to convert the typed text into a real date. If it is unable to  using the formart m/d/yyyy then it shows a box error.
            parsed_date = datetime.strptime(date_text, "%m/%d/%Y")
        except:
            messagebox.showerror("Invalid Date", "Please enter the date as MM/DD/YYYY.")
            return

        item_value = None #the value is optional, so if the user leaves it blank, it will be stored as NULL in the database. If the user enters a value, it will be converted to a float and stored in the database. If the user enters a non-numeric value, an error message will be shown.
        if value_text != "":
            try:
                item_value = float(value_text)
            except ValueError:
                messagebox.showerror("Invalid Value", "Item value must be a number.")
                return

        date_lost = parsed_date.strftime("%m/%d/%Y")  # Convert to MM/DD/YYYY format #strfttime is the reverse of strptime, it converts a date object into a string in the specified format. This is done so that the date is stored in the database in a consistent format.

        conn = get_connection()  # this code saves it to the database. get connection opens the database, cur.execute runs the SQL command, and conn.commit saves the changes to the database. conn.close closes the connection to the database.
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO ItemTable (ItemName, DateLost, LocationLost, ItemValue, ItemStatus)
            VALUES (?, ?, ?, ?, NULL)
        """, (item_name, date_lost, location, item_value))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"'{item_name}' has been reported as lost.")
        report.destroy()

    Button(
        report,
        text="SUBMIT REPORT",
        width=18,
        height=2,
        bg=REPORT_COLOR,
        fg="white",
        command=submit_report #tells tkinter to call upon the submit_report function when the button is clicked.
    ).pack(pady=20)