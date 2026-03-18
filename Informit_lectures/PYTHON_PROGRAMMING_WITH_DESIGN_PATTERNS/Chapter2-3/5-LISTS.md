# [Simple List](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/3.%20Visual%20tables/SimpleList.py)
## TODO 
- create a State (taking a String of the file as the init parameter)
- create a StateList (taking the file as the init parameter)
- the Windows toString method becomes here __str__ in python
```python
class State():
    def __init__(self, stateLine):
        self._tokens = stateLine.split(',')
        self._state_name = ""
        if len(self._tokens) > 3:
            self._state_name = self._tokens[0].strip()
            self._state_abbr = self._tokens[1].strip()
            self._state_founded = self._tokens[2].strip()
            self._state_capital = self._tokens[3].strip()
    
    def getStateName(self):
        return self._state_name
    
    def getStateAbbr(self):
        return self._state_abbr
    
    def __str__(self): # The Java toString method
        return f"{self._state_abbr} | {self._state_capital}"
```
# 43
## The ScrollBar see [StateLiistScroll](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/3.%20Visual%20tables/StateLiistScroll.py)
- all the 5 configuration Lines are necessary
```python
scrollBar = tk.Scrollbar(root)
scrollBar.config(command=self.listbox.yview) # without this command the scroll bar does not scroll the list, connects the scollBar to the List
self.listbox.grid(column=0, row=0, rowspan=4, padx=10) # We put the scrollBar on the next column
scrollBar.grid(column=1, row=0, rowspan=4, sticky="NS") # NS means North an South extension of the scrollbar
self.listbox.config(yscrollcommand=scrollBar.set) # for the scrollBar synchronises with the actual ListBox elements in the active Window
```
# 44 
## adding the labels and the events
- same code [StateLiistScroll](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/3.%20Visual%20tables/StateLiistScroll.py)
  - but also [ListBoxStateData](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/3.%20Visual%20tables/ListBoxStateData.py)
## The event
```python
self.listbox.bind('<<ListboxSelect>>', self.onselect) # ListboxSelect case matters
```
- the current selected listBox element is a tuple (with one element)
```bash
I selected (7,)
I selected (5,)
```
# 45
- same code [StateLiistScroll](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/3.%20Visual%20tables/StateLiistScroll.py)
  - but also [ListBoxStateData](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/3.%20Visual%20tables/ListBoxStateData.py)
## Adding an Entry
* I completed the example with the case when we press the Back Key
```python
    def keyPress(self, evt):
            chr = evt.char.upper()
            self.str_entry_arr.append(chr)
            self.complete()

    def complete(self):
        str_entry_upper = "".join(self.str_entry_arr)
        print(f"[Entry][complete] I pressed {str_entry_upper}")
        # search for state starting with the String
        i = 0
        found = False
        states = self.stateList.getStatesList()
        while (not found) and i < len(states):
            actual_state_name_upper = states[i].getStateName().upper()
            found = actual_state_name_upper.startswith(str_entry_upper)
            if not found:
                i += 1
            else: # found
                state_found = states[i]
                self.listbox.select_clear(0, tk.END) # clear the actual selections
                self.listbox.select_set(i)
                self.loadLabel(state_found)
    
    def backPress(self, evt):
        print(f"[Entry][backPress] I pressed back key")
        if len(self.str_entry_arr) > 0:
            self.str_entry_arr = self.str_entry_arr[:-1]
        if len(self.str_entry_arr) > 0:
            self.complete()
```
# ComboBox
- [The code on GitHub](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/3.%20Visual%20tables/StateDisplayCombo.py)
- combobox is inot in tkinter but on tkinter.ttk
```python
import tkinter as tk
import tkinter.ttk as ttk # Here is the Combobo
```
- I added the fllowing code to make the combobox work when entering data in the Entry
```python
def keyPress(self, evt):
        chr = evt.char.upper()
        self.str_entry_arr.append(chr)
        self.complete()

def complete(self):
    str_entry_upper = "".join(self.str_entry_arr)
    print(f"[Entry][complete] I pressed {str_entry_upper}")
    # search for state starting with the String
    i = 0
    found = False
    states = self.stateList.getStatesList()
    while (not found) and i < len(states):
        actual_state_name_upper = states[i].getStateName().upper()
        found = actual_state_name_upper.startswith(str_entry_upper)
        if not found:
            i += 1
        else: # found
            state_found = states[i]
            self.combo.set(state_found.getStateName())

def backPress(self, evt):
    print(f"[Entry][backPress] I pressed back key")
    if len(self.str_entry_arr) > 0:
        self.str_entry_arr = self.str_entry_arr[:-1]
    if len(self.str_entry_arr) > 0:
        self.complete()
```
