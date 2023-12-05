import tkinter as tk
from tkinter import filedialog
# Create a Tkinter window
root = tk. Tk()
root.title("Text Editor")
root. geometry("500x500")
# Create a Text widget and add it to the window
text = tk. Text(root, wrap="word")
text.pack(fill="both", expand=True)
# Create a function to open a file
def open_file():
    file_path = filedialog. askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            contents = file.read()
            text.delete("1.0", tk.END)
            text.insert("1.0", contents)
# Create a function to save a file
def save_file():
    file_path = filedialog. asksaveasfilename()
    if file_path:
        with open(file_path, "w") as file:
            contents = text.get("1.0", tk.END)
    file.write(contents)
# Create a Frame to hold the buttons
buttons = tk. Frame(root)
buttons.pack(side="left", fill="y")
# Create an Open button and add it to the Frame
open_button = tk. Button(buttons, text="Open", command=open_file)
open_button.pack(fill="x")
# Create a Save button and add it to the Frame
save_button = tk.Button(buttons, text="Save", command=save_file)
save_button.pack(fill="x")
# Start the Tkinter event loop
root.mainloop()