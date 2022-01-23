from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_window = browser.window_handles[0]
    browser.find_element_by_tag_name('button').click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    number = browser.find_element_by_id('input_value').text
    result = calc(number)

    browser.find_element_by_tag_name('input').send_keys(result)

    browser.find_element_by_tag_name('button').click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


