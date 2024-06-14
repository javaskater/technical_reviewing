#!//usr/bin/python3
"""Creates 2 Buttons window"""
import tkinter as tk
from tkinter import messagebox, Button, LEFT, RIGHT
import sys

# write slogan in a messageBox
def disp_slogan():
    messagebox.showinfo("our message", "tkinter is easy to use") # title, message

root = tk.Tk()
root.geometry("200x100+300+300") # x, y wwindow size and position

# creates the Hello Button
slogan = Button(root, text="Hello", command=disp_slogan)
slogan.pack(side=LEFT, padx=10)

#creates the exit button with red letters
button = Button(root, text="QUIT", fg="red", command=sys.exit)
button.pack(side=RIGHT, padx=10)

# start running the tkinter loop
root.mainloop()


