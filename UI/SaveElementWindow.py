from UI.save_elements_form import Ui_MainWindow

import sys
from PyQt6 import QtWidgets, uic


class SaveWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(SaveWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)