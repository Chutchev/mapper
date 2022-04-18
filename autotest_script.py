import sys

from PyQt6 import QtWidgets
from selenium.webdriver.chrome.webdriver import WebDriver

from pynput import keyboard as kb
import json

from UI.SaveElementWindow import SaveWindow

elements = {}

driver: WebDriver

def generate_xpath(tag, attrs):
    start_xpath = f"//{tag}"
    attr_xpath = ""
    for name, value in attrs.items():
        if name == 'text':
            attr_xpath += f"normalize-space(.)='{value}' and "
        else:
            attr_xpath += f"@{name}='{value}' and "
    attr_xpath = attr_xpath[:-5]
    ready_xpath = f"{start_xpath}[{attr_xpath}]"
    return ready_xpath


def start():
    global driver
    driver.get("https://vk.com")