#create a tkinter window 300 x 300

import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Dog Breeds")
root.geometry("300x300")

# using the grid system to place widgets
# create a grid of 4 rows and one column
# add a label to the first row, a combobox to the second row, and a button to the third row, a cancel button to the fourth row

# Breed label
breed_label = ttk.Label(root, text="Select Breed:")
breed_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

# Breed combobox
breed_combobox = ttk.Combobox(root, state="readonly")
breed_combobox.grid(row=1, column=0, padx=10, pady=10)

# Submit button
submit_button = ttk.Button(root, text="Submit")
submit_button.grid(row=2, column=0, padx=10, pady=10)

# Cancel button
cancel_button = ttk.Button(root, text="Cancel")
cancel_button.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()

