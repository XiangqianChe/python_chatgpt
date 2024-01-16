# Part 17: GUI Programming in Python with Tkinter

# 1. Basic GUI Window
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Simple GUI Application")

# Create and add a label to the window
label = tk.Label(window, text="Hello, Tkinter!", font=("Helvetica", 16))
label.pack(pady=20)


# Create a button callback function
def on_button_click():
    label.config(text="Button Clicked!")


# Create and add a button to the window
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack()

# Run the main loop
window.mainloop()

# 2. Entry Widget and Messagebox
from tkinter import messagebox


def show_entry_text():
    text = entry.get()
    messagebox.showinfo("Entry Text", f"You entered: {text}")


# Create a new main window
window2 = tk.Tk()
window2.title("Entry Widget and Messagebox")

# Create and add an entry widget to the window
entry = tk.Entry(window2, width=30, font=("Arial", 12))
entry.pack(pady=20)

# Create and add a button to show the entry text
button2 = tk.Button(window2, text="Show Entry Text", command=show_entry_text)
button2.pack()

# Run the new main loop
window2.mainloop()
