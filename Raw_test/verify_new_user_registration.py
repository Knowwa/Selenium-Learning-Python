from selenium import webdriver; from selenium.webdriver.common.keys import Keys; import time
from selenium.webdriver.common.by import By;import pdb; import string; import random

"""Verify registration of new user"""
driver = webdriver.Chrome()
driver.implicitly_wait(10); driver.get('http://demostore.supersqa.com/my-account/')

user_name = "Noah"
password = "password1."

email_field = driver.find_element(By.CSS_SELECTOR, "#reg_email")
password_field = driver.find_element(By.CSS_SELECTOR, "#reg_password")
register_btn_field = driver.find_element(By.CLASS_NAME, "woocommerce-form-register__submit")

#Generate Random email:
random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(15))
random_email = random_string + '@gmail.com'
#Enter data and submit:
email_field.send_keys(random_email)
password_field.send_keys("mynewpassword1!")
time.sleep(2)
register_btn_field.click()
logout_btn = driver.find_element(By.CSS_SELECTOR,"li.woocommerce-MyAccount-navigation-link--customer-logout a")

time.sleep(2)
if logout_btn.is_displayed():
    logout_btn.click()
    print("PASS")
else:
    raise Exception("User not logged in after registering!")
pdb.set_trace()
driver.quit()
