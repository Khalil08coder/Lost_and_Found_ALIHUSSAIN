import sqlite3
import tkinter as tk
from tkinter import messagebox

from gui3 import launch_main_app


class LoginApp:
    def __init__(self):
        self.login_window = tk.Tk()
        self.login_window.title("Login application")

        tk.Label(self.login_window, text="Student ID:").pack()
        self.student_id_entry = tk.Entry(self.login_window)
        self.student_id_entry.pack()

        tk.Label(self.login_window, text="Password:").pack()
        self.password_entry = tk.Entry(self.login_window, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.login_window, text="Login", command=self.login)
        self.login_button.pack()

        self.login_window.mainloop()

    def login(self):
        conn = sqlite3.connect('lost_and_found.db')
        cursor = conn.cursor()

        student_id = self.student_id_entry.get()
        password = self.password_entry.get()

        cursor.execute("SELECT * FROM users WHERE studentID=? AND password=?", (student_id, password))
        user = cursor.fetchone()

        conn.close()

        if user:
            # Login succeeded: close the login window and open the main app.
            self.login_window.destroy()
            launch_main_app()
        else:
            messagebox.showerror("Login Failed", "Invalid Student ID or Password")


if __name__ == "__main__":
    LoginApp()
