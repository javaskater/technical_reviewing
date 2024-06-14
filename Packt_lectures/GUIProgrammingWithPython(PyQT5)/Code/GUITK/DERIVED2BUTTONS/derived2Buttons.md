# the [code on GitHub](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/2.%20Visual%20programming/derived2buts.py)
# it profits from subclassing
* subclassing the DButton to make a clean code organisation
 * with a main method
 * with a buildUI method
 * and two class !!!
## Why ttk buttons
* found on Google
> What is the difference between a TK button and a TTK button?
> The main difference is that widget options such as “fg”, “bg” and others related to widget styling are no longer present in Ttk widgets. 
> Instead, use the ttk.Style class for improved styling effects.
## For a ttk the root 
* the root window is at the __master__ key of _**kwargs_ (__init__ method of the Button class)
* __text__ is another key of _**kwargs_
* as could be the command key
* If we don't use the key in the constructor
* we can use those _**kwargs_ parameters in the config method of the Button class
# special Style() method
* the Style() init method creates a new Style object under the chosen name (like a dict)
```python
class QuitButton(DButton):
    def __init__(self, root):
        Style().configure("W.TButton", foreground="red")
        super().__init__(master=root, text="QUIT", style="W.TButton")
        self.pack(side=RIGHT, padx=10)
```
## Others messagebox:
* OK, Cancel choice
```python
>>> result=messagebox.askokcancel("continue", "Go On")
>>> result # I have pushed the OK Button
True
>>> result=messagebox.askokcancel("continue", "Go On")
>>> result #I have pushed the Cancel Button
False
```
* Yes, No, Cancel choice
```python
>>> result=messagebox.askyesnocancel("continue", "Go On")
>>> result # I pressed the Yes Button
True
>>> result=messagebox.askyesnocancel("continue", "Go On")
>>> result # I pressed the No Button
False
>>> result=messagebox.askyesnocancel("continue", "Go On")
>>> result # I pressed the cancel Button
>>> assert(result is None) # result is then None
>>> assert(result is not None)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
```