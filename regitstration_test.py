from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_name('firstname')
input1.send_keys("Вера")

input2 = browser.find_element_by_name('lastname')
input2.send_keys('Сергеевна')

input3 = browser.find_element_by_name('email')
input3.send_keys('verochka45@yandex.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element_by_id('file')
element.send_keys(file_path)

button = browser.find_element_by_tag_name('button')
button.click()