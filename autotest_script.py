import sys
from pprint import pprint

import selenium
from selenium.webdriver import Chrome
import pyautogui
import keyboard
from pynput import keyboard as kb


def coords(key):
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
            pprint(res.get_property("attributes"))
    if k == "q":
        driver.quit()
        sys.exit()


driver = Chrome("drivers/chromedriver.exe")

driver.get("https://vk.com")
with kb.Listener(on_press=coords) as lst:
    lst.join()
