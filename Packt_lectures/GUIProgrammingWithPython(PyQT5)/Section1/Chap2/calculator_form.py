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
        #Main UI code goes here

        main_layout = qtw.QVBoxLayout()
        self.setLayout(main_layout)
        lcd_display = qtw.QLCDNumber()
        main_layout.addWidget(lcd_display)
        
        history = qtw.QLineEdit(self, placeholderText='History')
        main_layout.addWidget(history)

        button_layout = qtw.QGridLayout()
        main_layout.addLayout(button_layout)

        button_texts = [
            'Clear', 'BackSpace', 'Mem', 'MemClear',
            '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', 'x',
            '.', '0', '=', '/',
        ]

        for num, button_text in enumerate(button_texts):
            b = qtw.QPushButton(button_text, self)
            b.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
            col = num % 4 # can start at 0
            row = num // 4 # can start at 0
            button_layout.addWidget(b,row,col)

        self.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow('Calculator')
    retour = app.exec()
    print(f"l'application a retourner avec un code {retour}")
    sys.exit(retour)
