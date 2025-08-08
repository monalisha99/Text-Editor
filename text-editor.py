import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font


def save_task():
    # Get the text from the text box
    texts = text_box.get("1.0", tk.END).strip()

    if not texts:
        messagebox.showwarning("Empty", "Text box is empty. Nothing to save.")
        return

    # Ask for save location (asksaveasfilename, not askopenfilename)
    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if save_path:
        try:
            with open(save_path, "w") as file:
                file.write(texts)
            messagebox.showinfo("Saved", "File saved successfully!")
        except:
            messagebox.showerror("Error", "Could not save file!")


def open_file():
	# open the file dialog window on the screen when "Open" button is clicked
	# "Text Files" is the label shows in the file dialog dropdown 
	# The lable also includes "all files"
	#  * means any name before .txt file(file type)
	# *.* means any name before and after dot

	open_filedialog_path2 = filedialog.askopenfilename(
		filetypes= [("Text Files", "*.txt"),("all Files", "*.*")]
		)

	if open_filedialog_path2:
		# try to open file dialog path and read the files 
		try:
			with open(open_filedialog_path2,"r") as file:
				content = file.read()
				# clear previous content in the text box
				text_box.delete("1.0", tk.END)
				# insert the new content
				text_box.insert(tk.END, content)
		except:
			messagebox.showerror("Error", "Could not read file!")


def on_mouse_wheel(event):
	# This function is used to scroll the text box when mouse wheel is scrolled
	# event.delta is the amount of scroll
	# positive value means scroll down, negative means scroll up
	text_box.yview_scroll(int(-1*(event.delta/120)), "units")


# create window
root = tk.Tk()
root.title("Text Editor")
root.geometry("690x320")

# textbox resize
# (When resize the window, the Text box will grow/shrink with it)
root.grid_rowconfigure(1, weight=1)  # Only row 1 is resizable
root.grid_columnconfigure(0, weight=1)

# add a frame first
frame1 = tk.Frame(root, bg="gray")
frame1.grid(row=1, column=0, columnspan=2, padx=15, pady=3, sticky='nsew')

# Make frame1 row and column resizable
frame1.grid_rowconfigure(1, weight=1)
frame1.grid_columnconfigure(0, weight=1)

# add textbox inside the frame
# padx=(10,0) means, 10 pixels on the left(from the frame border) and o pixels on the right
text_box = tk.Text(frame1, font=("Courier New", 16), wrap='word')
text_box.grid(row=1, column=0, padx=(4,0), pady=3, sticky='nsew')

#text_box.window_create("end", window=frame_in_textbox)

#Add a scrollbar outside the text, but inside the layout frame
# make sure scrollbar column is not 0, because frame and textbox lies in column=0
scroll_bar = tk.Scrollbar(frame1, orient='vertical', command=text_box.yview, bg='lightblue', activebackground='blue')

# padx=(5,10) means, 5 pixels on the left(from the textbox) and 10 pixels from the right
scroll_bar.grid(row=1, column=1, padx=(5,10),sticky='ns')


# Link the text box and scrollbar:
# This ensures the scrollbar moves as the text scrolls vertically
text_box.config(yscrollcommand=scroll_bar.set)

# add "save" buttons
save_button = tk.Button(root,text='Save', 
	width=8, 
	height=2, 
	bg='lightblue', 
	fg='black', 
	activebackground='darkblue', 
	activeforeground='white',
	command=save_task)
save_button.grid(row=0, column=0, sticky='ne', padx=108, pady=3)


# bind mousewheel event to the textbox
text_box.bind("<Button-5>", on_mouse_wheel)
text_box.bind("<Button-4>", on_mouse_wheel)

# define open button and place it
open_button = tk.Button(root, text='Open', width=8, height=2, bg='lightblue', fg='black', activebackground='darkblue', activeforeground='white', command=open_file)
open_button.grid(row=0, column=0, sticky='ne', padx=15, pady=3)

root.mainloop()










