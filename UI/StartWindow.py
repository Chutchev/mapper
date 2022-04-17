from UI.mainWindow import Ui_MainWindow
from autotest_script import start
from UI.SaveElementWindow import SaveWindow
import sys
from PyQt6 import QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.saveForm = SaveWindow()
        self.btn_mapper.clicked.connect(self.start_script)

    def start_script(self):
        start()
        self.saveForm.show()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()