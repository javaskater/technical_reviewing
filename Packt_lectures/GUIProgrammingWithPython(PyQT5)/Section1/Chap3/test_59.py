#!/usr/bin/python3

import sys
from typing import Tuple
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

class MainWindow(qtw.QWidget):

    def __init__(self, title:str) -> None:
        """Main window constructor"""
        super().__init__(windowTitle=title)

        self.quit_button = qtw.QPushButton('Quit', clicked = self.close)
        layout = qtw.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(self.quit_button)

        self.bad_button = qtw.QPushButton('Bad')
        self.bad_button.clicked.connect(self.needs_args)
        layout.addWidget(self.bad_button)

        self.good_button = qtw.QPushButton('Good')
        self.good_button.clicked.connect(self.no_args)
        layout.addWidget(self.good_button)

        #self.quit_button.clicked.connect(self.close)
        self.entry1 = qtw.QLineEdit()
        self.entry2 = qtw.QLineEdit()
        layout.addWidget(self.entry1)
        layout.addWidget(self.entry2)

        self.entry1.textChanged.connect(self.entry2.setText)
        self.entry1.textChanged.connect(print)
        
        self.entry1.editingFinished.connect(lambda:print('editing finished'))
        self.entry2.returnPressed.connect(self.entry1.editingFinished)
        
        #End of MainUI Code
        self.show()

    def needs_args(self, arg1, arg2:str="toto", arg3:str="tata"):
        print(f"[needs_args] arg1: {arg1} arg2: {arg2} arg3: {arg3}")

    def no_args(self):
        print(f"[no_args] I need no argument")

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow('Hello')
    retour = app.exec()
    print(f"l'application a retourné avec un code {retour}")
    sys.exit(retour)
