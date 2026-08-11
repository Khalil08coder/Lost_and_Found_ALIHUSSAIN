from tkinter import *
from tkinter import messagebox
from colours import *


def open_report_window(parent):
    """Opens the Report Item window."""

    report = Toplevel(parent)
    report.title("Report Lost Item")
    report.geometry("400x420")
    report.configure(bg=BG)

    Label(
        report,
        text="Report Lost Item",
        bg=BG,
        font=("Arial", 18, "bold")
    ).pack(pady=15)
