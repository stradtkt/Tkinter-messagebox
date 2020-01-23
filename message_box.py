from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("Learn to code at gowebkit.com")
root.iconbitmap("c:/gui/gowebkit.ico")
root.geometry("200x200")

# showerror, showwarning, askquestion, askyesno

def popup():
    response = messagebox.askquestion("This is my popup", "Hello World!")
    Label(root, text=response).pack()
    # if response == "yes":
    #     Label(root, text="You clicked yes!").pack()
    # else:
    #     Label(root, text="You clicked no!").pack()


Button(root, text="Popup", command=popup).pack()

mainloop()