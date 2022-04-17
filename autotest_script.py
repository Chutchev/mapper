import sys

from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import selenium
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from pynput import keyboard as kb
import json

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
    print(ready_xpath)

def generate_element_dict(key):
    global elements, driver
    try:
        k = key.char
    except:
        k = key.name
    if k == "r":
        driver.execute_script("""
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
    if k == "f4":
        res = driver.execute_script("""
                                element = document.querySelector(".myHovered")
                                return element""")
        if res is not None:
            attrs = {}
            for attr in res.get_property("attributes"):
                # xpath //tag[@attr="value"]
                if attr['name'] != 'style':
                    if attr['name'] == 'class':
                        attr['value'].replace(' myHovered', '')
                    attrs[attr['name']] = attr['value']
                if res.get_attribute("innerText") != None:
                    attrs['text'] = res.get_attribute("innerText")
                print(res.tag_name, attr['name'], attr['value'], res.get_attribute("innerText"))
            generate_xpath(res.tag_name, attrs)

    if k in ("q", "ctrl_c"):
        driver.quit()
        sys.exit()

def start():
    global driver
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://vk.com")
    with kb.Listener(on_press=generate_element_dict) as lst:
        lst.join()