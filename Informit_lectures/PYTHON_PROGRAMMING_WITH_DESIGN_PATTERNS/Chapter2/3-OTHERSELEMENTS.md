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
# 29-30 Radio Buttons
- [Source code on GitHub](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/2.%20Visual%20programming/radiobuts.py)
```python
import tkinter as tk

class ChoiceButton(tk.Radiobutton):
    def __init__(self, rt, radioText, index, gvar, clabel):
        super().__init__(rt, text=radioText, padx=20, variable=gvar, value=index, command = self.cmd)
        self.pack(anchor=tk.W)
        self.color = radioText # Rdio button text
        self.var = gvar
        self.index = index # The selection value
        self.clabel = clabel # The label I want to modify on Radio Button selection (independant of the Radio Buttons)
    
    def cmd(self):
        print(f"color is: {self.color} (index: {self.index}))")
        self.clabel.configure(fg=self.color, text=f"color is: {self.color} (index: {self.index}))")

def main():
    root = tk.Tk()
    tk.Label(root, text = """Choose your favorite color:""", justify=tk.LEFT, padx=20).pack()
    groupv = tk.IntVar(); # The variable associated with our Labels, the selection value is here an integer
    groupv.set(None) # I want at the beginning that no Radio be selected (otherwise it selects the firs Choice by default)
    # Create RadioButtons with Labels
    cLabel = tk.Label(root, text=f"color is ?")
    cLabel.pack() # the pack command returns None, so I need two lines the line we call this action is important If you want the albel after the buttons you should calls it after creating the choice buttons
    ChoiceButton(root, 'Red', 0, groupv, cLabel);
    ChoiceButton(root, 'Green', 1, groupv, cLabel);
    ChoiceButton(root, 'Blue', 2, groupv, cLabel);
    root.mainloop()

if __name__== "__main__":
    main()
```
# 31
* pack anfd grid are both Layouts 
```python
lbl2= tk.Label(root, text="Adress") # in the example the author forgot the root element as first positional parameter
lbl2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W) # with tk.W aligne the label to the left 
```
# p 33 - 44
* a checkbox is a Tk' CheckButton
```python
import tkinter as tk
class  OKButton(tk.Button):
    def __init__(self, root, boxes):
        super().__init__(root, text="Order", command=self.command)
        self.boxes = boxes
    def command(self):
        for cb in self.boxes:
            #texte = cb.cget("text") 
            texte = cb["text"] # the previous or this one give the same result
            print(f"[on Command] for ingredient {texte} we get (checked/not checked) {cb.getVar()}")

class CheckBox(tk.Checkbutton):
    def __init__(self, rt, bText, gvar):
        super().__init__(rt, text=bText,variable=gvar)
        self.text = bText
        self.var = gvar

        # playing with disabled
        if self.text == "Pineapple": # same thing than self["text"] (pure Python)
            self.config(state=tk.DISABLED)
    
    def getVar(self):
        return self.var.get()

class InitUI:
    def __init__(self, root):
        self.ingredients = ["Cheese","Pepperoni","Mushrooms","Sausage","Peppers","Pineapple"]
        cboxes = []
        row = 0
        for ingr in self.ingredients:
            print(f"ingredient {ingr} at row {row}")
            var = tk.IntVar()
            cb = CheckBox(root, ingr, var)
            cb.grid(row=row, column=0, sticky=tk.W)
            cboxes.append(cb)
            row += 1
        
        ok = OKButton(root, cboxes)
        ok.grid(row=3, column=1, sticky=tk.E)

def main():
    root = tk.Tk()
    InitUI(root)
    root.mainloop()

if __name__== "__main__":
    main()
```
* The output is (when we click the Order Button Button)
```bash
[on Command] for ingredient Cheese we get (checked/not checked) 0
[on Command] for ingredient Pepperoni we get (checked/not checked) 0
[on Command] for ingredient Mushrooms we get (checked/not checked) 0 # has not been checked
[on Command] for ingredient Sausage we get (checked/not checked) 1 # has been checked
[on Command] for ingredient Peppers we get (checked/not checked) 1
[on Command] for ingredient Pineapple we get (checked/not checked) 0
```