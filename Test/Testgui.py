import tkinter as tk


root = tk.Tk()
root.title("Frame Header Example")
root.geometry("1000x900")


header = tk.Frame(root, bg="#2c3e50", height=60)
header.pack(side="top", fill="x")

header.pack_propagate(False)


header= tk.Label(
    header, 
    text="MACLEANS COLLEGE", 
    fg="#F6FF00", 
    bg="#005EFF", 
    font=("Arial", 16, "bold")
)

header.pack(expand=True)

frame = tk.LabelFrame(root, text="Student Details",)
frame.pack(padx=10, pady=10, fill="both",)

label_name = tk.Label(frame, text="Name:", font=("Arial", 12), fg="#000000")
label_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)

name = tk.Entry(frame, font=("Arial", 12), bd=1, relief="solid")
name.grid(row=0, column=1, sticky="ew", padx=10, pady=5)

date = tk.Label(frame, text="Date (DD/MM/YYYY):", font=("Arial", 12), fg="#000000")
date.grid(row=1, column=0, sticky="w", padx=10, pady=5)

date_entry = tk.Entry(frame, font=("Arial", 12), bd=1, relief="solid", bg="#e0e0e0",)
date_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=5)


Time = tk.Label(frame, text="Time:", font=("Arial", 12), fg="#000000")
Time.grid(row=2, column=0, sticky="w", padx=10, pady=5)

Time_entry = tk.Entry(frame, font=("Arial", 12), bd=1, relief="solid", bg="#e0e0e0",)
Time_entry.grid(row=2, column=1, sticky="ew", padx=10, pady=5)


House = tk.Label(frame, text="House:", font=("Arial", 12), fg="#000000")
House.grid(row=3, column=0, sticky="w", padx=10, pady=5)

House_entry = tk.Entry(frame, font=("Arial", 12), bd=1, relief="solid", bg="#e0e0e0",)
House_entry.grid(row=3, column=1, sticky="ew", padx=10, pady=5)

button = tk.Button(
    root, 
    text="Submit check in", 
    fg="#E5FF00",    
    bg="#005EFF",        
    font=("Arial", 12)
)
button.pack(pady=10)

footer = tk.Frame(root, bg="#f0f0f0", bd=1, relief="groove")
footer.pack(side="bottom", fill="x")

footer_text = tk.Label(
    footer, 
    text="Excellence is not an act, but a habit.",
    font=("Times New Roman", 30, "italic"), 
    bg="#005EFF", 
    fg="#FFFF00",
)

footer_text.pack(pady=5, padx=10, side="left")

root.mainloop()
