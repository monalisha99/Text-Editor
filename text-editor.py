
import tkinter as tk
from tkinter import messagebox

# define save task function
def save_task():
	# retrieve texts from the text box using get function
	texts = text_box.get("1.0", tk.END)
	with open("notebook.txt", "w") as file:
		for i in texts:
			file.write(i + "\n")


# create window
root = tk.Tk()
root.title("Text Editor")
root.geometry("1080x640")

# add widgets
# define Textbox and place it
text_box = tk.Text(root, width=80, height=24)
text_box.grid(row=0, column=0, sticky='nws', padx=5, pady=5)

# define save button and place it
save_button = tk.Button(root, text='Save', width=10, height=2 )
save_button.grid(row=0, column=1, sticky='ne', padx= 10, pady=10, command=save_task())



root.mainloop()










