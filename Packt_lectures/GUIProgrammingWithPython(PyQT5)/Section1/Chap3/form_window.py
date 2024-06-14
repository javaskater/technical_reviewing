#!/usr/bin/python3

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

class FormWindow(qtw.QWidget):

    submitted = qtc.pyqtSignal([str], [int,str])

    def __init__(self) -> None:
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())


        self.edit = qtw.QLineEdit()
        self.submit = qtw.QPushButton('submit', clicked = self.onSubmit)

        self.layout().addWidget(self.edit)
        self.layout().addWidget(self.submit)

    def onSubmit(self):
        text = self.edit.text()
        if text.isdigit():
            self.submitted[int, str].emit(int(text), text)
        else:
            self.submitted[str].emit(text)
        self.close()


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
        self.formwindow.submitted[str].connect(self.onSubmittedStr)
        self.formwindow.submitted[int, str].connect(self.onSubmittedIntStr)
        self.formwindow.show()

    @qtc.pyqtSlot(str)
    def onSubmittedStr(self, string):
        self.label.setText(string)

    @qtc.pyqtSlot(int, str)
    def onSubmittedIntStr(self, integer, string):
        message = f"The string {string} becomes the number {integer}"
        self.label.setText(message)
 
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    retour = app.exec()
    print(f"l'application a retourner avec un code {retour}")
    sys.exit(retour)
