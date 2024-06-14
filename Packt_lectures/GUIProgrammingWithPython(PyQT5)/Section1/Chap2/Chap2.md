## The Code to download
* The Code is on the [GitHub page for Chap 2](https://github.com/PacktPublishing/Mastering-GUI-Programming-with-Python/tree/master/Chapter02)

# 26 (43/256)
* I try that example in the python REPL
```python
>>> from PyQt5 import QtWidgets as qtw
>>> from PyQt5 import QtCore as qtc
>>> app = qtw.QApplication([])
>>> window = qtw.QWidget(cursor=qtc.Qt.ArrowCursor)
>>> window.setWindowFlags(qtc.Qt.Sheet| qtc.Qt.Popup)
>>> window.show()
```
* No Handle to close the window
## QLabel
* I can set a new text after the __show__ function has been called on the parent _QWidget_
```python
class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        """Main window constructor"""
        super().__init__()
        #Main UI code goes here
        subwidget = qtw.QWidget(self, toolTip = 'This is my Widget')
        label = qtw.QLabel('Hello Widget', self)
        print(f"The text of the label is initially {label.text()}")
        line_edit = qtw.QLineEdit('default value', self)
        #End of MainUI Code
        self.show()
        label.setText('My new text')
        print(f"The text of the label is now {label.text()}")
```
* When I change the margin of the Label, I have to manually expand the window to make it appear
  
# 27
## QLineEdit
* Interesting adding controls in the constructor!!
```python
line_edit = qtw.QLineEdit('default Value', self, placeholderText='Type here',
                                  clearButtonEnabled=True, maxLength=20)
```
# 28
* The __QPushButton__ is a child of the _QAbstractButton_ like:
  * _QCheckBox_
  * _QRadioButton_
  * _QToolButton_ (for use in [toolbar Widgets](https://doc.qt.io/qt-5/qtoolbutton.html)) 
* for the Keyboard Shortcut it is important not to have Blanks (and prefer lowercase letters)
  *  __qtg.QKeySequence('Ctrl+p')__ and not _qtg.QKeySequence('Ctrl + P')_
  * could have been _QKeySequence(qtc.Qt.CTRL + qtc.Qt.Key_P)_ very interesing if you want the Uppercase letter:
```python
shortcut=qtg.QKeySequence(qtc.Qt.CTRL +  qtc.Qt.SHIFT + qtc.Qt.Key_P)
```
# 29
## QComboBox
* select widget in HTML
* The example shows us that we can have integer, strings, or Objects sa values (in the same combobox!!!)
* * the property _insertPolicy=qtw.QComboBox.InsertAtTop_ is not very useful as the entered String has an associated None value 

# 30
## QSpinBox
* The prfix and suffix are only for the display, the value remains the integer !!! (Could be discrete things)
# 31
## QDateTimeEdit 
* The __calendarPopup__ makes that the up and down arrows disappear
* With the up and down arrows the minutes are by default incremented / decremented
  * if you select the month that the mont value that will be changed by the arrows
* if I want only Time (and no date) there is _QTimeEdit_
*  if I want only date (and no Time) there is _QDateEdit_
# 34
## QTextEdit
* Is line _QLineEdit_ but for many lines inputs
  * and it has buttons of a WYSIWYG editor !  
*  I don't know how to activate the buttons
  * even if I put _acceptRichText=True,_ the WYSIWYG Toolbar does not appear  
# 35
## Layout
* you can add Wiget to a Layout,
* or add a Layout to a Layout (composition) to create more complex layouts !!!
* the GridLayout is similar to HTML Tables with rows numbers, column numbers (starting from 0)
  * and also rowspan and colspan values (by defult 1)
## QForm Layout
* a special form of GridLayouts specialized in two-column forms
```python
form_layout.addRow('Item1', qtw.QLineEdit(self)) #accept on ly a combination Label, Widget
form_layout.addRow(qtw.QLabel('<b>Item3</b>'), qtw.QLineEdit(self))
form_layout.addRow(qtw.QLabel('<b>This is a label only row</b>'))
form_layout.addRow(qtw.QLabel('<b>Item4</b>'), qtw.QLabel('<b>Item4_bis</b>'))
```
# 40
## SizeHints
* We have 2 SizePolicies values for a widget
  * one for its width
  * one for its height
* The [lambda in python](https://www.data-transitionnumerique.com/lambda-python/) can be very simple
  * here the case with overloading sizeHint function for the textedi widget
*  _stetch_ works only  with the _QHBoxLayout and QVBoxLayout classes_
*  

# 43
## A GroupBox
* is a widget that
* has a layout that we set
* its layout can be retrieved trhough the _layout()_ method
  * in that layout we can add widgets!!!

# 44
## Validating widgets
* remember that the validate method is called at each key-stroke in the input field.
* The majic with the _Visual Studio Code_ Python is that if Generates the following code
  * only by seeing that I am extending _qtg.QValidator_ 
```python
from typing import Tuple
# autres imports
class IPv4Validator(qtg.QValidator):
    """Enforce Entry of IPv4 addresses"""
    def validate(self, a0: str, a1: int) -> Tuple[State, str, int]:
        return super().validate(a0, a1)
```
* So I know I have to return au Tuple with the State as the first element (State is not defined)
 * knowing that I have to return a Tuple is not clear in the [documentation](https://doc.qt.io/qt-5/qvalidator.html)
 * It is only said the 
> The function can change both input and pos (the cursor position) if required.
* that is why the new input and position are returned
### Case Of he IPV4 validator
* If I leave an empty field the IP Adress will be accepted with a warning
* Same thing if the number of octets less than 4
* in both case I could replace the empty octets with a 0 and reconstruct the string to be returned
  * If less than 4 octets complete the octets array with [0]
* the validator's state return type is [qtg.QValidator.State](https://doc.qt.io/qtforpython-5/PySide2/QtGui/QValidator.html)
* when setting a validator to a widget we call the Validator's constructor

# 47 Spinbox
* We pass the Spinbox a _list_ not a _Dictionary_
* the value is the index in the list, the text is the element of the list
```python
>>> choices = ['bad', 'average', 'good', 'awesome']
>>> l = [e for e in choices] # in case of a dict it gives a list of the keys
>>> l
['bad', 'average', 'good', 'awesome']
>>> i = choices.index('bad')
>>> i
0
>>> i = choices.index('good')
>>> i
2
```
* the _validate_ method deals with the list's elements (string is the element value, index is its position)

## SpinBox constructor

* _*args_ is the list of arguments of the parent it has only an element the reference to the parent window (_MainWindow_)
  * the other parameters belong to the _**kwargs_ dict, see:
```python
spinbox = qtw.QSpinBox(self,
                value=12,
                maximum=100,
                minimum=10,
                prefix='$',
                suffix = ' + Tax',
                singleStep = 5,
                wrapping=True)
```
## SpinBox validator:
* it works the following way
  * if the value is not Acceptable
  * it goes back to the previous _Acceptable_ value
* with the function _print_ I see that
  * _valueFromText_ is called when I manually enter an Acceptable Text
  * _valueFromText_ is called when I use the arrows of the spinbox 

# The [Calendar GUI](https://github.com/PacktPublishing/Mastering-GUI-Programming-with-Python/blob/master/Chapter02/calendar_form.py)
* the solution [is inline](https://github.com/PacktPublishing/Mastering-GUI-Programming-with-Python/blob/master/Chapter02/calendar_form.py)
* The minimal code
  * super() does not need self
  * you have to call the show() method otherwise you have to kill the _/usr/bin/python3 ./calendar_form.py_ Linux process
```python
  class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        """Main window constructor"""
        super().__init__()

        #configure the window
        self.setWindowTitle("My Calendar App")
        self.resize(800, 600)

        self.show()
```
## Adding the widgets using Python code:
* Interesting the way to simulate a ComboBox PlaceHolder by disabling the first element
  * it uses the model that we will see in more detail in chapter 5 (page 50) 
## Setting the Layout
* with the calendar alone (it is auto-expanding) we can test the application
* for the form part (right + down) we encompass things in a [GroupBox](https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QGroupBox.html)
  * it is a widget grouping others widgets
  * using a Layout 
    * we add child widgets to that Layout
    * and we attach the Layout to the GroupBox Widget
## The GUI using QTDesigner (52 and above)
* The design directly adapds to the setted Values
* There is a distinction between the _object name_ and the _Window Title_
* We can only set the Layout when there is already a widget on the Window
* The object inspector on the right is very interesting !!!!
* To drag the Label in the Vertical Layout (which has a width of zero) it is better to drag it in the object inspector (see the TIP at the end of page 53)
* The properties editor presents the Hierarchy of Objects (very practical) the Label text is at the last child (draw down the )
* the List Widget must be the List view
* __Ctrl + R__ 

# Questions of Chapter 2:
## The Validator
```python
>>> s='Bonjour'
>>> s[2:3]
'n'
>>> s[6:7]
'r'
>>> s[10:12]
''
>>> ss = s[0:3] + s[10:12]
>>> ss
'Bon'
>> s = 'Bon-jour-tout-le-monde'
>>> d1 = s[3:4]
>>> d1
'-'
>>> d2 = s[7:8]
>>> d2
'r'
>>> d2 = s[8:9]
>>> d2
'-'
>>> d3=s[13:14]
>>> d3
'-'
>>> d4=s[16:17]
>>> d4
'-'
>>> ss = all([c == '-' for c in d1+d2+d3+d4])
>>> ss
True
>>> ss = 'Bon-jour'
>>> d1 = ss[3:4]
>>> d2 = ss[8:9]
>>> d3 = ss[13:14]
>>> d4 = ss[16:17]
>>> d1+d2+d3+d4
'-'
>>> t = all([c == '-' for c in d1+d2+d3+d4])
>>> t
True
>>> t = all([c == '-' for c in ''])
>>> t
True
>>> t = all(['','Bon'])
>>> t
False
>>> t = all(['J','Bon'])
>>> t
True
```
* _ss_ if the inventory number we chack for the letters, the numbers or the dashes __only on the existing letters__ (see above for the dashes)
## The Calculator
* [The LCD Display](https://doc.qt.io/qt-5/qlcdnumber.html)
* I have had difficulties placing the buttons in a GridLayout (especially when augmenting the columns numbers, must be placed at the very right)
  * CTRL + R to visualize the ui form  