from tkinter import *
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_editor.delete("1.0", END)
            text_editor.insert(END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_editor.get("1.0", END))

root = Tk()
root.title("Dark Notepad")
root.config(bg="#1E1E1E")

text_editor = Text(root, bg="#282828", fg="white", insertbackground="white", selectbackground="#454545", selectforeground="white")
text_editor.pack(fill=BOTH, expand=True)

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

root.mainloop()