# p 58 (75/526)
* signals are events (user action, timeout, asynchronous call), slots are responses to those events !!!
* The _close()_ slot of the __QWidget__ class is the response to the close window clic envent
  * the code is in the _QWidget_ class and i causes to close the window if it is a top level Window
# 59
* I test the code in the [test_59.py)](./test_59.py) python app
# 60
* the setText method of a _QLineEdit_ needs a string as a parameter
  * the signal passes the text carried
```python
self.entry1.textChanged.connect(self.entry2.setText)
``` 
* We can pass a [Python lambda function](https://www.w3schools.com/python/python_lambda.asp)
* the _editing finished_ signal is thrown when the QLineEdit loses the Focus
  * click on another input Widget
  * use the Tab Key (to pass the focus from widget to widget)
  * quit the application (which happens here through the _concel_ button) 
* the signal _self.entry2.returnPressed_ is connected to the signal _self.entry1.editingFinished_ this means:
  * when I click Enter on entry2
  * it sends the signal editingfinised (with its data here None) which calls its associated slot !!!
# 63
* inside _pyqtSignal_ we use Python's type objects (_str_, _int_) !!!

* we can have [custom type as dictionary keys](https://stackoverflow.com/questions/4901815/object-of-custom-type-as-dictionary-key)
* Google says _Dictionary keys must be of an immutable type_ see [dictionary keys restrictions](https://realpython.com/lessons/restrictions-dictionary-keys-and-values/)

# 64
* anticipating the case where submitted ca emit either a str alone or a int with a str
  * the signal _submitted = qtc.pyqtSignal(str)_ works the same way than _pushButton.clicked_
  * you connect to it a function (without the parenthese)
  * The parameters types are given in the signal definition
  * And their values are given  in the _signal.emit_ function parameters !!! 
  > It then binds our custom signal, FormWindow.submitted , 
  > to the setText slot of the label; setText takes a single string for an argument, 
  > and our signal sends a single string.
  > FormWindow doesn't need to know anything whatsoever about MainWindow , 
  > and MainWindow only needs to know that FormWindow has a submitted signal that emits the entered string
# 65
* @nnotations
```python
class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        """Main window constructor"""
        super().__init__()
        #Main UI code goes here
        self.setLayout(qtw.QVBoxLayout())

        self.label = qtw.QLabel('Click "change" to change this text.')
        self.change = qtw.QPushButton("Change", clicked = self.onChange)
        self.change.setCheckable(True)
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.change)

        #End of MainUI Code
        self.show()
    
    @qtc.pyqtSlot(bool)
    def onChange(self, click:bool):
        print(f"[MainWindow][onChange] j'ai cliqué {click}")
        self.formwindow = FormWindow()
        self.formwindow.submitted.connect(self.label.setText)
        self.formwindow.show()
```
* the annotation _@qtc.pyqtSlot(bool)_ tells us that the clicked signal takes a bool and not a string.
 * to make that boolean be True, you have to [make the Button Toggable](https://stackoverflow.com/questions/55722834/why-a-qt-signalclickedbool-does-not-same-with-a-really-mouse-clicked-behavior)

# 66
* Here we register two signal, 
  * one that sends out a string only
  * one that sends out an int and a string
* The Change Button of the Mainwindows connnectes the two signals of the Form Windows to methods of the Main window  while creating the form window
* the Submit button of the Form Windows emits one of the two signals depending on the text of the QLineEdit
# 67: Automating the Caledar Form
* Still TODO  