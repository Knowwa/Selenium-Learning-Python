from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://demostore.supersqa.com')

#finding by class name
product = driver.find_element(By.CLASS_NAME, 'product')
products = driver.find_elements(By.CLASS_NAME, 'product')
print(product)
print('===============')
for lines in products:
    print(lines)

#example of finding by 'name'
order_by =driver.find_element(By.NAME, 'orderby')
print('===============')
print(order_by.text)

#example of finding by 'tag'
all_links = driver.find_elements(By.TAG_NAME, 'a')
print('================')
print(f"Found number of 'a' tag: {len(all_links)}")

all_li = driver.find_elements(By.TAG_NAME, 'li')
print('================')
print(f"Found number of 'li' tag: {len(all_li)}")