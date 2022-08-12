from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com')

#finding cart element without importing By
#cart = driver.find_element('id', 'site-header-cart')

#finding cart element using By
cart = driver.find_element(By.ID, 'site-header-cart')
cart.click()

driver.get('http://demostore.supersqa.com/my-account/')
user_name = driver.find_element(By.ID, 'username')
user_name.send_keys('myusername')
pdb.set_trace()

# To find available methods just do dir(<variable>)
# Example: dir(driver); dir(cart); dir(myusername)