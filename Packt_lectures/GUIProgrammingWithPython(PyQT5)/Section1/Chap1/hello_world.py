#!/usr/bin/python3

from PyQt5 import QtWidgets

app = QtWidgets.QApplication([])

window = QtWidgets.QWidget(windowTitle='Hello Qt')

window.show()

app.exec()

print(f"The title of the window is {window.windowTitle()}")