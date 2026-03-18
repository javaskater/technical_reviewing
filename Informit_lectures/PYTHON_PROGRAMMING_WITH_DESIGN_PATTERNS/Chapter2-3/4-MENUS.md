# 35
## [Final code for PyTk Menus](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/2.%20Visual%20programming/Menus.py)
* The fileMenu is two times bound to the main menubar
```python
fileMenu = tk.Menu(menubar, tearoff=0) # from fileMenu to the menubar (parent)
menubar.add_cascade(label="File", menu=fileMenu) # from the parent (menubar) to the file sub manu
```
* without tearoff=0 you can detach the commands from the menu main item by clicking on the dotted line
* The only command I put
```python
    fileMenu.add_command(label="New", command=None)
    fileMenu.add_command(label="Open", command=None)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quit) # the only command beacuse it is a system command
```
# 36 Object Menus
* [The source code on GitHub](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/2.%20Visual%20programming/ObjMenus.py)
* for the menubar or the commands the root parameter at the constructor is not vers useful
* The Action calsses are only containers, all the Work is done in the TopMenu calss when adding the command
* I had problem with calling the super()__init__() no self parameter is needed
```python
class MenuBar(tk.Menu):
    def __init__(self, root):
        super().__init__(root) # no self parameter is needed
        root.config(menu=self)
```