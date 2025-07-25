
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font

# define save task function
def save_task():
	# retrieve texts from the text box using get function
	texts = text_box.get("1.0", tk.END)
	with open("notebook.txt", "w") as file:
		file.write(texts)


def open_file():
	# open the file dialog window on the screen when "Open" button is clicked
	# "Text Files" is the label shows in the file dialog dropdown 
	# The lable also includes "all files"
	#  * means any name before .txt file(file type)
	# *.* means any name before and after dot

	open_filedialog_path = filedialog.askopenfilename(
		filetypes= [("Text Files", "*.txt"),("all Files", "*.*")]
		)

	if open_filedialog_path:
		# try to open file dialog path and read the files 
		try:
			with open(open_filedialog_path,"r") as file:
				content = file.read
				# clear previous content in the text box
				text_box.delete("1.0", tk.END)
				# insert the new content
				text_box.insert(tk.END, content)
		except:
			messagebox.showerror("Error", "Could not read file!")






# create window
root = tk.Tk()
root.title("Text Editor")
root.geometry("690x320")

# textbox resize
#(When resize the window, the Text box will grow/shrink with it)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# add widgets
# define Textbox and place it
text_box = tk.Text(root, font="Times, 14")
text_box.grid(row=0, column=0, sticky='nsew', padx=15, pady=15)

# define save button and place it
save_button = tk.Button(root, text='Save', width=8, height=1, bg='lightblue', fg= 'black', activebackground='darkblue', activeforeground='white', command=save_task)
save_button.grid(row=0, column=1, sticky='ne', padx=10, pady=10)

# define open button and place it
open_button = tk.Button(root, text='Open',width=8, height=1, bg='lightblue', fg= 'black', activebackground='darkblue', activeforeground='white', command=open_file)
open_button.grid(row=0, column=2, sticky='ne', padx=10, pady=10)

root.mainloop()










