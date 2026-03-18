# 17
* Very simple program
  - just dont forget *root.mainloop()* to make everything run
```python
import tkinter as tk
from tkinter import messagebox, Button
def disp_slogan():
    messagebox.showinfo("our message", "tkinter is easy to use")
def main():
    root = tk.Tk()
    root.title("Hello World")
    
    # Hello Button
    slogan = Button(root, text="Hello", command=disp_slogan)
    slogan.pack()

    quitB = Button(root, text="quit", fg="red", command=quit)
    quitB.pack()

    root.mainloop() # the book just forgot that line
if __name__== "__main__":
    main()
```
* for the *root.geometry("200x100+300+300")*
  * x position from the top left is the third number 300
  * y position from the top left is the fourth number 300
  * w: width is the first number here 200
  * h:height is the second number here 100

# 19
* _**kwargs_ means many following __key=value__ arguments
# 23-24
* for each frame instatiation there is the instance of main window missing (here root)