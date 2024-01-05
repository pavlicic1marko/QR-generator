# This is a QR generator
from tkinter import *
import pyqrcode
# Pillow fork of PIL
from PIL import ImageTk, Image

root = Tk()

canvas = Canvas(root, width=400, height=600)
canvas.pack()

app_label = Label(root, text="QR code Generator", fg='blue', font=("arial", 30))
canvas.create_window(200, 50, window=app_label)

# Adding labels
name_label = Label(root, text="Link name", font=("arial", 15))
link_label = Label(root, text="Link", font=("arial", 15))
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

# Adding input fields
name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200, 120, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

# Add Button
button = Button(text="Generate QR")
canvas.create_window(200, 250, window=button)

# start GUI
root.mainloop()
