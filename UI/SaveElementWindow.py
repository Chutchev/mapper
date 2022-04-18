import json
from pathlib import Path

from UI.save_elements_form import Ui_MainWindow

import sys
from PyQt6 import QtWidgets, uic


class SaveWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(SaveWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.xpath_edit.setReadOnly(True)
        self.save_element.clicked.connect(self.save_element_click)
        self.xpath_dict_path = Path(Path.cwd(), "xpath.json")

    def save_element_click(self):
        element_type = self.element_type.text()
        element_name = self.element_name.text()
        elements = self.load_xpaths()
        if element_type not in elements.keys():
            elements[element_type] = {element_name: self.xpath_edit.text()}
        else:
            elements[element_type].update({element_name: self.xpath_edit.text()})
        self.save_xpathes(elements)
        self.close()

    def save_xpathes(self, xpathes):
        with open(self.xpath_dict_path, 'w') as f:
            json.dump(xpathes, f, indent=4, ensure_ascii=False)

    def load_xpaths(self):
        if self.xpath_dict_path.is_file():
            with open(self.xpath_dict_path, 'r') as f:
                elements = json.load(f)
        else:
            elements = {}
        return elements
