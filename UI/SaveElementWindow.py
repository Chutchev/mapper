from UI.save_elements_form import Ui_MainWindow

import sys
from PyQt6 import QtWidgets, uic


class SaveWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(SaveWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.xpath_edit.setReadOnly(True)
        self.save_element.clicked.connect(self.save_element_click)
        self.xpath = ""

    def save_element_click(self):
        element_type = self.element_type.text()
        element_name = self.element_name.text()
        print(element_type, element_name, self.xpath)
        self.close()