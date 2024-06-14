# The example programm
* _quit_ or _sys.exit_ when in use in the REPL let me a terminal which does not input the key strokes !!!
* in the REPL, the elements appear as soon they are declared
  * for the button you must call their _pack_ function...
* this does work:
```python
>>> from tkinter import messagebox
>>> messagebox.showinfo("our message", "tkinter is easy")
'ok'
```
* but import * does not work for messagebox:
```python
>>> from tkinter import *
>>> messagebox.showinfo("our message", "tkinter is easy")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'messagebox' is not defined
>>> exit()
```
## The solution is on [the GitHub page](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/2.%20Visual%20programming/Hellobuts.py)

* in a normal window program 
  * we need to call _mainloop_ to make the window appear
```python
root = tk.Tk() # is not enough to make the window appear

root.mainloop() # launches all the UI
```
* geometry "600x300+100+200" means
  * 600 width
  * 300 height
  * 100 x position from the left
  * 200 y position from the top
* packing a button
  * padx is not the webpadding, it is more the web's margin
```python
slogan = Button(root, text="Hello", command=disp_slogan)
slogan.pack(side=LEFT, padx=10)
```

* The two buttons are packed horizontally, I have to drage the right side of the main window
  * to make the second button appear
  * or augment the width in the root geometry which is our solution
```python
root = tk.Tk()
root.geometry("200x100+300+300") # x, y wwindow size and position
```
* for the second button the padx concerns the right margin
* Note that the first parameter of a Button is the main window (root)