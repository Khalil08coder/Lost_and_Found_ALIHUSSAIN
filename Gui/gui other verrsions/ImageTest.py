#This file was just to test out the image resizing and displaying in the GUI. It is not part of the main application.
from tkinter import *
from PIL import Image, ImageTk

# Create the main GUI window
root = Tk()
root.title("Lost and Found")

image = Image.open("image.png.png")  # Replace with your image file path
resized_image = image.resize((250, 200))

img = ImageTk.PhotoImage(resized_image)

label = Label(image=img)
label.image = img  # Required to prevent image from being garbage collected
label.pack()

# Run the GUI application
root.mainloop()