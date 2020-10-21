# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 12:49:04 2020

@author: lenovo
"""

from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    element = browser.find_element_by_name("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("first_name")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("first_name")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("first_name")
    button = browser.find_element_by_xpath("//button[text()=\"Submit\"]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла