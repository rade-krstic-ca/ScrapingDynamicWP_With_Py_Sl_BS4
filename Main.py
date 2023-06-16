from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import polasci_class
import requests
import webbrowser
import time
import re
import os
import TestingPage


os.system('cls')

html_code = ''
url = "http://www.gspns.co.rs/"
req = requests.get(url).text
soup = BeautifulSoup(req, 'lxml')

#print(soup.prettify())
#a_tags = soup.find_all('a')
#print("'a' Links:")
#for a_tag in a_tags:
#    print(a_tag)
print()
a_medjumesni = soup.find_all('a',href=re.compile('medjumesni'))
a_gradski = soup.find_all('a',href=re.compile('/gradski'))
a_prigradski = soup.find_all('a', href=re.compile('prigradski'))
#print("Gradski:")
#for a_tag in a_gradski:
#    print("'a' tag is:{}\nHis parent is:\n {}".format(a_tag['href'], a_tag.parent.prettify()))
#print("Prigradski:")
#for a_tag in a_prigradski:
#    print("'a' tag is:{}\nHis parent is:\n {}".format(a_tag['href'], a_tag.parent.prettify()))
#print("Medjumesni:")
#for a_tag in a_medjumesni:
#    print("'a' tag is:{}\nHis parent is:\n {}".format(a_tag['href'], a_tag.parent.prettify()))
print()

def choose_page():
    choos = int(input("Choice:\n1. Gradski\n2. Prigradski\n3. Medjumesni\n0. exit\nAnswer(1 - 3): "))
    while(choos !=0):
        find_tag = ''
        match choos:
            case 1:
                find_tag = soup.find('a',href=re.compile('/gradski'))
            case 2:
                find_tag = soup.find('a', href=re.compile('prigradski'))
            case 3:
                find_tag = soup.find('a', href=re.compile('medjumesni'))
            case _:
                break
        html_code = url + find_tag['href']
        #webbrowser.open(html_code)
        testing = TestingPage.TestingPage(html_code)
        busLines_list = testing.get_BusLines_List_withBS(choos)
        destination_choose = testing.choose_destination(busLines_list)
        polasci = testing.get_BusTimeTable(destination_choose, choos)
        time.sleep(2)
        return polasci
        
polasci = choose_page()

print()
os.system('cls')
testing = TestingPage.TestingPage(html_code)
testing.reading_TimeTable(polasci)
#Just fot the TEST^
print()