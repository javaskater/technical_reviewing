# a [complicated solution with menus](https://github.com/jwcnmr/jameswcooper/blob/main/Pythonpatterns/2.%20Visual%20programming/ObjMenus.py) 
* We will see the menus later
* Testing in the REPL environment:
```python
>>> from tkinter import filedialog
>>> fname = filedialog.askopenfilename()
>>> print(fname)
/home/jmena01/tmp/bootstrap.jar
>>> fname = filedialog.askopenfilename(defaultextension="*.py") # seems to change nothing
>>> print(fname)
/home/jmena01/CONSULTANT/Python/PyQT5/PACKTBookGUIProgrammingWithPython/Section1/Chap1/hello_world.py
>>> fname = filedialog.askopenfilename(defaultextension="*.py")
>>> print(fname)
/home/jmena01/CONSULTANT/Python/PyQT5/PACKTBookGUIProgrammingWithPython/Section1/Chap1/Chap1.md
>>> fname = filedialog.askopenfilename(defaultextension="*.py") # I click the cancel button
>>> assert(fname is not None)
>>> assert(len(fname) == 0)
```
* with multiple files:
```python
>>> fnames = filedialog.askopenfilenames(defaultextension="*.py")  
>>> for f in fnames: # the default extension does not seem to have an effect
...   print(f)
... 
/home/jmena01/CONSULTANT/Python/PyQT5/PACKTBookGUIProgrammingWithPython/Section1/Chap1/Chap1.md
/home/jmena01/CONSULTANT/Python/PyQT5/PACKTBookGUIProgrammingWithPython/Section1/Chap1/hello_world.py
/home/jmena01/CONSULTANT/Python/PyQT5/PACKTBookGUIProgrammingWithPython/Section1/Chap1/qt_template.py
>>> fnames = filedialog.askopenfilenames(defaultextension="*.py") # I select 3 files
>>> fnames
('/home/jmena01/CONSULTANT/Python/PyQT5/PACKTBookGUIProgrammingWithPython/Section1/Chap1/Chap1.md', '/home/jmena01/CONSULTANT/Python/PyQT5/PACKTBookGUIProgrammingWithPython/Section1/Chap1/hello_world.py', '/home/jmena01/CONSULTANT/Python/PyQT5/PACKTBookGUIProgrammingWithPython/Section1/Chap1/qt_template.py')
>>> type(fnames)
<class 'tuple'>
>>> assert(type(fnames) is tuple) #True
>>> assert(type(fnames) is list)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
>>> fnames = filedialog.askopenfilenames(defaultextension="*.py") # I directly click the cancel button
>>> fnames
''
>>> assert(fnames is not None)
>>> assert(type(fnames) is tuple)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
>>> assert(type(fnames) is str)
>>> assert(len(fnames) == 0)
```
## asksaveasfile

```python
>>> fname = filedialog.asksaveasfile(defaultextension="*.py") #if the name you enter does not end up with .py the filedialog does not close
>>> fname
<_io.TextIOWrapper name='/home/jmena01/CONSULTANT/Python/PyQT5/PACKTBookGUIProgrammingWithPython/Section1/Chap1/hello.py' mode='w' encoding='UTF-8'> #it did create en emty python file
>>> fname = filedialog.asksaveasfile(defaultextension="*.py") # I click the Cancel Button
>>> assert(fname is None)
```