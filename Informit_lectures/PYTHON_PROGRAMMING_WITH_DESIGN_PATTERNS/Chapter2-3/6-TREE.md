# General
-  Treeview can represent
  - either a table (when only one layer)
  - or a real Tree with nodes and leaves
# p 48
## Our Table with States
- [The Code on GitHub](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/3.%20Visual%20tables/TreeStates.py)
- My code
```python
class BuildUI():
    def __init__(self, root, slist):
        self.stateList = slist.getStatesList()
        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ("abbrev", "capital", "founded") # necessary to announce to the tree object the columns other than #0
        headers = ("Abbrev", "Capital", "Founded")
        self.tree.pack(side=tk.TOP, fill=tk.X)
        # prepare the column
        self.tree.column("#0", width=100, minwidth=100, stretch=tk.NO)
        self.tree.column(self.tree["columns"][0], width=50, minwidth=50, stretch=tk.NO)
        self.tree.column(self.tree["columns"][1], width=100, minwidth=100, stretch=tk.NO)
        self.tree.column(self.tree["columns"][2], width=70, minwidth=60, stretch=tk.NO)
        # create the Headings
        self.tree.heading("#0", text="Name")
        self.tree.heading(self.tree["columns"][0], text=headers[0])
        self.tree.heading(self.tree["columns"][1], text=headers[1])
        self.tree.heading(self.tree["columns"][2], text=headers[2])

        for index, stateObj in enumerate(self.stateList):
            print(stateObj)
            self.tree.insert("", index, text=stateObj.getStateName(), values=(stateObj.getStateAbbr(), stateObj.getStateCapital(), stateObj.getStateFounded())) 

        style = ttk.Style()
        style.configure("Treeview.Heading", font=(None, 10, "bold"), foreground="red") # Configure all Tree headers in this page !!
```

## Multi Layer Static Tree
- The Code [is on Github](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/3.%20Visual%20tables/TreeTest.py)
  - What is the root when I insert new Nodes see [answer 0 to this StackOverflow Post](https://stackoverflow.com/questions/77542329/create-a-tree-with-the-ttk-treeview-widget-based-on-a-list)
- we do add one layer only (the Tree Component seems limited in the number of layers it can add)
```python
rootCA = ""
for index, stateObj in enumerate(self.stateList):
    print(stateObj)
    if index == 0:
        rootCA = self.tree.insert("", index, text=stateObj.getStateName(), values=(stateObj.getStateAbbr(), stateObj.getStateCapital(), stateObj.getStateFounded()))      
    else:
        self.tree.insert(rootCA, index, text=stateObj.getStateName(), values=(stateObj.getStateAbbr(), stateObj.getStateCapital(), stateObj.getStateFounded())) 
```