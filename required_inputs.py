from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector(
        'input[required][class="form-control first"]'
    ).send_keys("1stName")

    browser.find_element_by_css_selector(
        'input[required][class="form-control second"]'
    ).send_keys("2ndName")

    browser.find_element_by_css_selector(
        'input[required][class="form-control third"]'
    ).send_keys("Mail")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(2)
    browser.quit()