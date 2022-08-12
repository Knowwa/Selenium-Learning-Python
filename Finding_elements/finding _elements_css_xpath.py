import pdb
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com')

#cart = driver.find_element(By.CSS_SELECTOR, '#site-header-cart > li:nth-child(1) > a')
my_account = driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a')
#cart.click()
time.sleep(2)
my_account.click()
pdb.set_trace()

# time.sleep(5)
# driver.quit()