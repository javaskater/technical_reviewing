#!/usr/bin/python3

import sys
from typing import Tuple
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

class InventoryNumberValidator(qtg.QValidator):
    valid_letters = 'ABCDEFGHJKLMNPQRSTUVWXYZ' #not I nor O
    """Enforce Entry of Inventory Number XX-999-9999X"""
    def validate(self, string: str, index: int) -> Tuple[qtg.QValidator.State, str, int]:
        state = qtg.QValidator.Acceptable
        seq1 = string[0:2]
        dash1 = string[2:3]
        seq2 = string[3:6]
        dash2 = string[6:7]
        seq3 = string[7:11]
        seq4 = string[11:12]

        if not all([char == '-' for char in dash1 + dash2]):
            state  = qtg.QValidator.Intermediate #authorize modification but not validate
        elif not all([char in self.valid_letters for char in seq1 + seq4]):
            state  = qtg.QValidator.Intermediate #authorize modification but not validate
        elif not all([char.isdigit() for char in seq2 + seq3]):
            state  = qtg.QValidator.Intermediate #authorize modification but not validate
        elif len(string) > 12:
            state  = qtg.QValidator.Invalid
        elif not all([seq1, dash1, seq2, dash2, seq3, seq4]): #on or more sequence are empty
            state  = qtg.QValidator.Intermediate #authorize modification but not validate
        return (state, string, index)



class MainWindow(qtw.QWidget):
    def __init__(self, title:str) -> None:
        """Main window constructor"""
        super().__init__(windowTitle=title)
        #Main UI code goes here
        #line_edit = qtw.QLineEdit('default Value', self)
        line_edit = qtw.QLineEdit('', self, placeholderText='XX-999-9999X',
                                  clearButtonEnabled=True, maxLength=20)
        # setting minimum and maximum sizes
        line_edit.setMinimumSize(150, 15)
        line_edit.setMaximumSize(500, 50)
        #testing the validator
        line_edit.setValidator(InventoryNumberValidator())

        

        layout = qtw.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(line_edit)
        
        #End of MainUI Code
        self.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow('Hello')
    retour = app.exec()
    print(f"l'application a retourner avec un code {retour}")
    sys.exit(retour)
