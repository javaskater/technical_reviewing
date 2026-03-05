# 25
* it is only an extrract of the [Yourname.py Code](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/2.%20Visual%20programming/YourName.py)
* be carefull, the hook on the ok button has to be a function name
```python
    # Hello Button
    self.okButton = Button(root, text="OK", command=self.getName) # and not command=self.getName() which returns the function evaluation
    self.okButton.pack()
```
it has to be **self.getName** and not ~~self.getName()~~ (that latter expression returns the evaluation of the self.getName function where the cLabel is still unknown)
# 26 
* [The SimpleMath code on GitHub](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/2.%20Visual%20programming/SimpleMath.py)
* the *grid* method is analogeous to the pack method ...
# 28 applying colors:
* the [DButton](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/2.%20Visual%20programming/derived2buts.py)
  * it is the example we worked with Just change if to give an hexadecimal value
```python
# derived from DButton calls Quit function
class QuitButton(DButton):
    def __init__(self, root):
        # also sets Quit to Red
        Style().configure("W.TButton", foreground='#234567')
        super().__init__(root, text="Quit",style="W.TButton") # text="Quit",style="W.TButton" are in the **kwargs of the parent
        self.pack(side=RIGHT, padx=10) # added configuration

    # calls the quit function and the program exits
    def comd(self):
        quit()
```
# Radio Buttons
- [Source code on GitHub](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/2.%20Visual%20programming/radiobuts.py)