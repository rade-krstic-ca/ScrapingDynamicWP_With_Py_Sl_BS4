from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re

class TestingSelenium:
    def __init__(self):
        pass
    
    def get_driver(self):
        chromeOptions = Options()
        chromeOptions.add_argument("--kiosk")
        return webdriver.Chrome(options=chromeOptions)
    
    def findElementTAG_NAME(self,TAG_NAME_String):
        driver = webdriver.Chrome()    
        return driver.find_elements(By.TAG_NAME, TAG_NAME_String)
    
    def findElementCSS_SELECTOR(self, CSSString):
        driver = webdriver.Chrome()
        return driver.find_element(By.CSS_SELECTOR, CSSString)
    
testing = TestingSelenium()
linie = input("Linija: ")
driver = testing.get_driver()
driver.get("http://www.gspns.co.rs/red-voznje/prigradski")
options_tags = driver.findElementTAG_NAME("option")
for element in options_tags:
    print(f"option: {element.text}")
for destination in options_tags:
    if destination.text == re.compile(str(linie).upper()):
        destination.click()
        btn_prikaz = driver.findElementCSS_SELECTOR("button[onclick='ispis_polazaka()']")
        btn_prikaz.click()