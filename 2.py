# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:35:52 2020

@author: lenovo
"""

from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element_by_id("input_value")
    x = num1.text
    y = calc(x)
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
#    select = Select(browser.find_element_by_tag_name("select"))
#    select.select_by_value(str(num1+num2)) # ищем элемент с текстом "Python"
    button = browser.find_element_by_xpath("//button[text()=\"Submit\"]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла