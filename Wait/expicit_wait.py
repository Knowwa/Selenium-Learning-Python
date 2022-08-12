from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('file:///Users/noahzertuche/Desktop/Python_Learning/Selenium_Course/Wait/page_with_slow_image.html')

#implicit Wait:
my_image = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.ID, 'the_slow_image')))
print("Found Image")
