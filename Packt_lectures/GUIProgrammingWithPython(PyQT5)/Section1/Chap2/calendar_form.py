#!/usr/bin/python3

import sys
from typing import Tuple
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        """Main window constructor"""
        super().__init__()

        #configure the window
        self.setWindowTitle("My Calendar App")
        self.resize(800, 600)

        self.calendar = qtw.QCalendarWidget() #new here
        self.event_list = qtw.QListWidget() #new here
        self.event_title = qtw.QLineEdit()
        self.event_category = qtw.QComboBox()
        self.event_time = qtw.QTimeEdit(qtc.QTime(8,0))
        self.allday_check = qtw.QCheckBox('All Day')
        self.event_detail = qtw.QTextEdit()
        self.add_button = qtw.QPushButton('Add/Update')
        self.delete_button = qtw.QPushButton('Delete')

        # Add event categories
        self.event_category.addItems(['Select Category ...', 'New ...', 'Work',
                                      'Meeting', 'Doctor', 'Family'])
        self.event_category.model().item(0).setEnabled(False)

        # Main Layout
        main_layout = qtw.QHBoxLayout()
        self.setLayout(main_layout)
        main_layout.addWidget(self.calendar)
        # we need to allow the calendar to expand
        self.calendar.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        ## The rightLayout added to the mainLayout
        right_layout = qtw.QVBoxLayout()
        main_layout.addLayout(right_layout)
        right_layout.addWidget(qtw.QLabel('Events on Date'))
        right_layout.addWidget(self.event_list)
        self.event_list.setSizePolicy(qtw.QSizePolicy.Expanding, qtw.QSizePolicy.Expanding)
        ### The down part of the right Layout
        event_form = qtw.QGroupBox('Event') # https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QGroupBox.html
        right_layout.addWidget(event_form) # it is a widget grouping others wodgets
        event_form_layout = qtw.QGridLayout() # using a Layout (we add widgets to the Layout)
        event_form.setLayout(event_form_layout) # and we attach the Layout to the GroupBox Widget
        ### We aach the child widgets to the GroupBox through its Layout
        #### First Line (1 row, 3 columns)
        event_form_layout.addWidget(self.event_title, 1, 1, 1, 3)
        #### second Line 
        event_form_layout.addWidget(self.event_category, 2, 1)
        event_form_layout.addWidget(self.event_time, 2, 2)
        event_form_layout.addWidget(self.allday_check, 2, 3)
        #### third Line (1 row, 3 columns)
        event_form_layout.addWidget(self.event_detail, 3, 1, 1, 3)
        #### fourth Line
        event_form_layout.addWidget(self.add_button, 4, 2)
        event_form_layout.addWidget(self.delete_button, 4, 3)

        

        self.show()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    retour = app.exec()
    print(f"l'application a retourner avec un code {retour}")
    sys.exit(retour)
