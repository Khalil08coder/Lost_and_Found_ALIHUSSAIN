import tkinter as tk
from tkinter import messagebox

from dbinformation import get_connection
from gui4 import launch_main_app


class LoginApp:
    """checks student ID + password against the
    users table before opening the main app."""

    def __init__(self):
        self.login_window = tk.Tk()
        self.login_window.title("Login application")

        tk.Label(self.login_window, text="Student ID:").pack()
        self.student_id_entry = tk.Entry(self.login_window)
        self.student_id_entry.pack()

        tk.Label(self.login_window, text="Password:").pack()
        self.password_entry = tk.Entry(self.login_window, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(
            self.login_window, text="Login", command=self.login
        )
        self.login_button.pack()

        self.login_window.mainloop()

    def login(self):
        """Checks the entered ID/password against the database and
        opens the main app on success."""
        conn = get_connection()
        cursor = conn.cursor()

        student_id = self.student_id_entry.get()
        password = self.password_entry.get()

        cursor.execute(
            "SELECT * FROM users WHERE studentID=? AND password=?",
            (student_id, password)
        )
        user = cursor.fetchone()

        conn.close()

        if user:
            self.login_window.destroy()
            launch_main_app()
        else:
            messagebox.showerror(
                "Login Failed", "Invalid Student ID or Password"
            )


if __name__ == "__main__":
    LoginApp()
