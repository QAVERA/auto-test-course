from selenium import webdriver
import math

link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element= browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x)

answer1 = browser.find_element_by_id('answer')
answer1.send_keys(y)

button = browser.find_element_by_tag_name('button')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

input2 = browser.find_element_by_css_selector("[for='robotCheckbox']")
input2.click()

input3 = browser.find_element_by_css_selector("[value='robots']")
input3.click()

button.click()

