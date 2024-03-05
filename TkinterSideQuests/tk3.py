import tkinter as tk

root = tk.Tk()
check_var = tk.IntVar()  # Declare an IntVar
check_button = tk.Checkbutton(root, text="Check me", variable=check_var)  # Associate the IntVar with a Checkbutton
# if the IntVar is 1, the Checkbutton is checked, if 0, it is not checked
# print the value of the IntVar when the Checkbutton is toggled
def display_checked():
    print(check_var.get())
check_button['command'] = display_checked
check_button.pack()

root.mainloop()
