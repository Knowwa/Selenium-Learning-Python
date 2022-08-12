from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#Example 1 of sending keys
driver = webdriver.Chrome()
# driver.get('http://demostore.supersqa.com/my-account/')

# user_name = driver.find_element(By.ID, "username")
# pass_word = driver.find_element(By.ID, "password")
# log_in_btn = driver.find_element(By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button")

# user_name.send_keys("noahz@gmail.com")
# pass_word.send_keys("123456789")
# log_in_btn.click()

#Example 2 of sending other keys or key buttons (keystrokes)

# driver.get('http://demostore.supersqa.com')

# search_field = driver.find_element(By.CLASS_NAME, "search-field")
# search_field.send_keys("hoodie")
# time.sleep(3)
# search_field.send_keys(Keys.ENTER)

#Example 3 (use send keys and Keys)
driver.get('http://demostore.supersqa.com/my-account/')

user_name = driver.find_element(By.ID, "username")
user_name.send_keys("abcd")
time.sleep(3)
user_name.send_keys(Keys.TAB)








