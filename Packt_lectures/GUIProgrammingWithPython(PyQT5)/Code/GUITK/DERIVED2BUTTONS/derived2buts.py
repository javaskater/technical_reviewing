#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox, LEFT, RIGHT
from tkinter.ttk import Button, Style
import sys

class DButton(Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        super().config(command=self.cmd)
    
    def cmd(self):
        pass

class OKButton(DButton):
    def __init__(self, root):
        super().__init__(master=root, text="OK")
        self.pack(side=LEFT, padx=10)

    def cmd(self):
        print("[OKButton] pressing the OK button")
        messagebox.showinfo("My OK", "TKInter is easy to use")

class QuitButton(DButton):
    def __init__(self, root):
        Style().configure("W.TButton", foreground="red")
        super().__init__(master=root, text="QUIT", style="W.TButton")
        self.pack(side=RIGHT, padx=10)

    def cmd(self):
        print("[QuitButton] pressing the quit button")
        sys.exit(0)


def buildUI()->int:
    print("[buildUI] I create the main window")
    root = tk.Tk()
    root.geometry("200x100+300+300")
    ok=OKButton(root)
    q=QuitButton(root)
    status=root.mainloop()
    return status

def main():
    print("[main] I will buid the ui")
    buildUI()

if __name__ == "__main__":
    main()