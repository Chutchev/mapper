import sys
from pprint import pprint
from webdriver_manager.chrome import ChromeDriverManager
import selenium
from selenium.webdriver import Chrome
import pyautogui
from selenium.webdriver.chrome.service import Service
import keyboard
from pynput import keyboard as kb
from UI.mapper_start import start

elements = {}

def generate_element_dict(key):
    global elements
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
            for attr in res.get_property("attributes"):
                print(res.tag_name, attr['name'], attr['value'], res.get_attribute("innerText"))
    if k in ("q", "ctrl_c"):
        driver.quit()
        sys.exit()


driver = Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://vk.com")
with kb.Listener(on_press=generate_element_dict) as lst:
    lst.join()
