#!/usr/bin/python3

import sys
from typing import Tuple
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

class IPv4Validator(qtg.QValidator):
    """Enforce Entry of IPv4 addresses"""
    def validate(self, string: str, index: int) -> Tuple[qtg.QValidator.State, str, int]:
        state = qtg.QValidator.Acceptable
        octets = string.split('.')
        if len(octets) > 4:
            state = qtg.QValidator.Invalid
        elif not all([x.isdigit() for x in octets if x != '']):
            state = qtg.QValidator.Invalid
        elif not all([0 <= int(x) <= 255 for x in octets if x != '']):
            state = qtg.QValidator.Invalid
        elif any([x == '' for x in octets]):
            state = qtg.QValidator.Intermediate # If I leave an empty field the IP Adress will be accepted with a warning
        elif len(octets) < 4:
            state = qtg.QValidator.Intermediate # If I leave  less than 4 fields the IP Adress will be accepted with a warning, I would have told to invalidate it
        else:
            state = qtg.QValidator.Acceptable
        return (state, string, index)

class ChoiceSpinBox(qtw.QSpinBox):
    def __init__(self, choices, *args, **kwargs):
        self.choices = choices
        super().__init__ (
            *args,
            maximum = len(self.choices) - 1, #otherwise changed by **kwargs which comes after
            minimum = 0,
            **kwargs
        )

    def valueFromText(self, text: str) -> int: # enter a ext goes to the index
        index = self.choices.index(text)
        print(f"[valueFromText] for the value {text} the index is {index}")
        return index
    
    def textFromValue(self, v: int) -> str: #shows the values based on the QSpinBox index vaue (we have limited it in the constructor)
        try:
            text = self.choices[v]
            print(f"[textFromValue] for the the index {v} the value is {text}")
            return text
        except IndexError:
            return '!Error!'
        
    def validate(self, string, index):
        state = qtg.QValidator.Invalid
        if string in self.choices:
            state = qtg.QValidator.Acceptable
        elif [v.startswith(string) for v in self.choices]:
            state = qtg.QValidator.Intermediate
        return (state, string, index)


class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        """Main window constructor"""
        super().__init__()
        #Main UI code goes here
        subwidget = qtw.QWidget(self, toolTip = 'This is my Widget')
        label = qtw.QLabel('<b>Hello Widget</b>', self, margin=10)
        # set at 150 pixels wide and 40 pixels high
        label.setFixedSize(150,40)
        print(f"The text of the label is initially {label.text()}")
        #line_edit = qtw.QLineEdit('default Value', self)
        line_edit = qtw.QLineEdit('default Value', self, placeholderText='Type here',
                                  clearButtonEnabled=True, maxLength=20)
        # setting minimum and maximum sizes
        line_edit.setMinimumSize(150, 15)
        line_edit.setMaximumSize(500, 50)
        #testing the validator
        line_edit.setText('0.0.0.0')
        line_edit.setValidator(IPv4Validator())

        button = qtw.QPushButton('Push Me', self, checkable=True, checked=True,
                                 shortcut=qtg.QKeySequence(qtc.Qt.CTRL +  qtc.Qt.SHIFT + qtc.Qt.Key_P))
        combobox = qtw.QComboBox(self, editable=True, insertPolicy=qtw.QComboBox.InsertAtTop)
        combobox.addItem('Lemon', 1)
        combobox.addItem('Peach', 'Oh I Like Peaches !')
        combobox.addItem('Strawberry', qtw.QWidget)
        combobox.insertItem(1, 'Radish', 2)

        spinbox = qtw.QSpinBox(self,
                               value=12,
                               maximum=100,
                               minimum=10,
                               prefix='$',
                               suffix = ' + Tax',
                               singleStep = 5,
                               wrapping=True)
        spinbox.setSizePolicy(qtw.QSizePolicy.Fixed, qtw.QSizePolicy.Preferred)
        
        datetimebox = qtw.QDateTimeEdit(self, 
                                        date = qtc.QDate.currentDate(),
                                        time = qtc.QTime(12,30),
                                        calendarPopup = True,
                                        maximumDate = qtc.QDate(2030, 1, 1),
                                        maximumTime = qtc.QTime(17,0),
                                        displayFormat = 'yyyy-MM-dd HH:mm')
        
        textedit = qtw.QTextEdit(
            self,
            acceptRichText=True,
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=25,
            placeholderText='Enter your Text Here'
        )
        textedit.sizeHint = lambda : qtc.QSize(500,500)
        textedit.setSizePolicy(qtw.QSizePolicy.MinimumExpanding, qtw.QSizePolicy.MinimumExpanding)

        layout = qtw.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(label)
        layout.addWidget(line_edit)

        sublayout = qtw.QHBoxLayout()
        layout.addLayout(sublayout)

        sublayout.addWidget(button)
        sublayout.addWidget(combobox)
        ratingBox = ChoiceSpinBox(['bad', 'average', 'good', 'awesome'], self)
        sublayout.addWidget(ratingBox)

        container = qtw.QWidget(self)
        grid_layout = qtw.QGridLayout()
        #layout.addLayout(grid_layout) #goes to the TabWidget
        container.setLayout(grid_layout)
        grid_layout.addWidget(spinbox, 0, 0)
        grid_layout.addWidget(datetimebox, 0, 1)
        grid_layout.addWidget(textedit, 1, 0, 2, 2)

        form_layout = qtw.QFormLayout()
        layout.addLayout(form_layout)
        form_layout.addRow('Item1', qtw.QLineEdit(self))
        form_layout.addRow('Item2', qtw.QLineEdit(self))
        form_layout.addRow(qtw.QLabel('<b>Item3</b>'), qtw.QLineEdit(self))
        form_layout.addRow(qtw.QLabel('<b>This is a label only row</b>'))
        form_layout.addRow(qtw.QLabel('<b>Item4</b>'), qtw.QLabel('<b>Item4_bis</b>'))

        stretch_layout = qtw.QHBoxLayout()
        layout.addLayout(stretch_layout)
        stretch_layout.addWidget(qtw.QLineEdit('Short'), 1)
        stretch_layout.addWidget(qtw.QLineEdit('Long'), 2)

        #test of the Tab Layout
        tab_widget = qtw.QTabWidget(
            movable=True,
            tabPosition=qtw.QTabWidget.West,
            tabShape=qtw.QTabWidget.Triangular
        )
        layout.addWidget(tab_widget)
        tab_widget.addTab(container, 'Tab the first')
        tab_widget.addTab(subwidget, 'Tab the second')

        # test a groupBox
        groubBox = qtw.QGroupBox('Buttons',
                                 checkable=True,
                                 checked = True,
                                 alignment = qtc.Qt.AlignHCenter,
                                 flat = False 
                                 )
        groubBox.setLayout(qtw.QHBoxLayout())
        groubBox.layout().addWidget(qtw.QPushButton('OK'))
        groubBox.layout().addWidget(qtw.QPushButton('Cancel'))
        layout.addWidget(groubBox)

        
        #End of MainUI Code
        self.show()
        label.setText('My new text')
        print(f"The text of the label is now {label.text()}")

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    retour = app.exec()
    print(f"l'application a retourner avec un code {retour}")
    sys.exit(retour)
