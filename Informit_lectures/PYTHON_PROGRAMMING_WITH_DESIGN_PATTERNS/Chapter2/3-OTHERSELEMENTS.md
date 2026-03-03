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