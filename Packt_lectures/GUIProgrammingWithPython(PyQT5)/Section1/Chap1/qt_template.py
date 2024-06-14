#!/usr/bin/python3

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        """Main window constructor"""
        super().__init__()
        #Main UI code goes here

        #End of MainUI Code
        self.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    retour = app.exec()
    print(f"l'application a retourner avec un code {retour}")
    sys.exit(retour)
