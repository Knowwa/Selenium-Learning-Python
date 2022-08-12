from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('file:///Users/noahzertuche/Desktop/Python_Learning/Selenium_Course/Wait/page_with_slow_image.html')
driver.implicitly_wait(10)

image = driver.find_element(By.ID, 'the_slow_image')
image.click()
print("Found Image")