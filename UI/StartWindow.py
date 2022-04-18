from UI.SaveElementWindow import SaveWindow
from UI.mainWindow import Ui_MainWindow
from autotest_script import generate_xpath
import sys
from PyQt6 import QtWidgets, uic, QtCore
from webdriver_manager.chrome import ChromeDriverManager
import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.saveForm = SaveWindow()
        self.btn_mapper.clicked.connect(self.start_script)

    def start_script(self):
        self.driver = Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://vk.com")
        self.setFocus()

    def keyPressEvent(self, event) -> None:
        if event.key() == QtCore.Qt.Key.Key_R:
            self.driver.execute_script("""
                                        body = document.getElementsByTagName("body")[0]
                                        body.onmouseover = handleover;
                                        body.onmouseout = handleover;
                                        function handleover(event) {
                                            console.log(event.type)
                                            if (event.type=="mouseover"){
                                                    event.target.style.border = "4px red solid"
                                                    event.target.classList.add("myHovered")
                                                }
                                            if (event.type=="mouseout"){
                                                    event.target.style.border = ""
                                                    event.target.classList.remove("myHovered")
                                                }
                                        }
                                        """)
        if event.key() == QtCore.Qt.Key.Key_F4:
            res = self.driver.execute_script("""
                                            element = document.querySelector(".myHovered")
                                            return element""")
            if res is not None:
                attrs = {}
                for attr in res.get_property("attributes"):
                    if attr['name'] != 'style':
                        if attr['name'] == 'class':
                            attr['value'] = attr['value'].replace(' myHovered', '')
                        attrs[attr['name']] = attr['value']
                    if res.get_attribute("innerText") != None:
                        attrs['text'] = res.get_attribute("innerText")
                ready_xpath = generate_xpath(res.tag_name, attrs)
                self.saveForm.xpath = ready_xpath
                self.saveForm.xpath_edit.setText(ready_xpath)
                self.saveForm.show()


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()