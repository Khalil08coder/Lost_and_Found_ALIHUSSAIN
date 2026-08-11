import tkinter as tk
from tkinter import *

root = tk.Tk()

root.title("Counting Seconds")

button = tk.Button(root, text="Stop", width=25, command=root.destroy)
button.grid(row=5, column=0)

tk.Label(root, text="First Name").grid(row=0, column=0)
tk.Label(root, text="Last Name").grid(row=1, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)


var1 = tk.IntVar()
var2 = tk.IntVar()

tk.Checkbutton(root, text="Male", variable=var1).grid(row=3, sticky=tk.W)
tk.Checkbutton(root, text="Female", variable=var2).grid(row=4, sticky=tk.W)

root.mainloop()
