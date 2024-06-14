# The first example
* It is on the [Packtpub GitHub Page](https://github.com/PacktPublishing/Mastering-GUI-Programming-with-Python/blob/master/Chapter01/hello_world.py)
  
## Note 1
* There is no explicit link between **window** and **app**
* *app.exec()* is blocking
  * The print function is executed only once the app has been closed by the user
```python
#!/usr/bin/python3

from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])

window = QtWidgets.QWidget(windowTitle='Hello Qt')

window.show()

app.exec()

print(f"The title of the window is {window.windowTitle()}")
``` 
## the qt_template

* it returns 0
* very good idea to make a _sys.exit(retour)_ to niform the calling shell of the return of our program

```python
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's required to have a reference to the MainWidow
    # if it goes out of scope it will be destroyed 
    mw = MainWindow()
    retour = app.exec()
    print(f"l'application a retourner avec un code {retour}")
    sys.exit(retour)
```
* It is the role of the _QApplication_ object to change put in debuuging mode
  * changing styles and themes
  * that is why we pass it sys.argv
  
* p 19 (36) it does well explain the role of the *__main__*

# QtDesigner
* It has been installed in the [PyQT5 installation.md file](../../installation.md)
* Its usage is the occasion for the [Qt Designer Manual](https://doc.qt.io/qt-5/qtdesigner-manual.html)
  * _here in version 5_
* There is no Tool menu but a _Form / Preview ..._ the preview is also accessible with __CRL + R__