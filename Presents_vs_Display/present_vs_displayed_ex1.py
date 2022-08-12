from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

driver = webdriver.Chrome()
driver.implicitly_wait(10)

url = 'file:///Users/noahzertuche/Desktop/Python_Learning/Selenium_Course/Presents_vs_Display/present_vs_displayed.html'
driver.get(url)

button_1 = driver.find_element(By.ID, 'btn1')
button_1_text = button_1.text
print(f'First Button text: {button_1_text}')
button_2 = driver.find_element(By.ID, 'btn2')
button_2_text = button_2.text
print(f'Second Button text: {button_2_text}')
button_3 = driver.find_element(By.ID, 'btn3')
button_3_text = button_3.text
print(f'Third Button text: {button_3_text}')
button_4 = driver.find_element(By.ID, 'btn4')
button_4_text = button_4.text
print(f'Fourth button text: {button_4_text}')

if button_4.is_displayed():
    button_4.click()
else:
    raise Exception("Button_4 is not Displyed")

pdb.set_trace()


