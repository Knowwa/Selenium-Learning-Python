from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://demostore.supersqa.com")

cart_elem = driver.find_element(By.LINK_TEXT, 'Cart')
print(cart_elem.text)

account_element = driver.find_element(By.LINK_TEXT, 'My account')
print(account_element.text)

#Partial Link_Text
account_elem_p = driver.find_element(By.PARTIAL_LINK_TEXT, 'acc')
print(account_elem_p.text)

footer_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, 'Built with')
print(footer_link_text.text)

#must be <a> tag or it will fail
driver.find_element(By.LINK_TEXT, '0 items')
