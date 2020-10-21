# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 13:01:53 2020

@author: lenovo
"""

from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_xpath("//button[text()=\"I want to go on a magical journey!\"]")
    button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    num1 = browser.find_element_by_id("input_value")
    x = num1.text
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    button = browser.find_element_by_xpath("//button[text()=\"Submit\"]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла