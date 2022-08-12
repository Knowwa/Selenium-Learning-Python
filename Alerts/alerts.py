from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb
import time

driver = webdriver.Chrome()
driver.get('file:///Users/NoahZertuche/Desktop/repos/python_selenium_course/Alerts/alerts_example.html')

# # Find the button/alert for JS and click/dismiss:
# java_btn = driver.find_element(By.CSS_SELECTOR, "#jsAlertExample > button")
# java_btn.click()
# time.sleep(3)
# # now we need to figure out how to deal with alert by switching to it
# # use pdb.set_trace() and find all available functions of driver using dir(driver)
# #locate the switch_to function and find all options of it using dir(driver.switch_to)
# #locate option 'alert' and type driver.switch_to.alert
#alert = driver.switch_to.alert
# """Checking to see if alert text is correct"""
# assert alert.text == "I am a JavaScript Alert", "Unexpected text error on alert!"
# alert.accept() #or alert.dismiss()
# pdb.set_trace()



#Example 2
# confirm_alert = driver.find_element(By.CSS_SELECTOR, "#jsConfirmExample > button")
# confirm_alert.click()
# time.sleep(3)
# confirm_alert = driver.switch_to.alert
# confirm_alert.accept() #or .dismiss()

# """Checking to see it alert confirm text is correct"""
# confirm_id_resp = driver.find_element(By.ID,"userResponse1").text
# expected_confirm_message = "Great! You will love it!"
# assert confirm_id_resp == expected_confirm_message, f"Confirm message doesn't match! Message expected: '{expected_confirm_message}', Message returned '{confirm_id_resp}'."
# pdb.set_trace()


#Example 3
prompt_alert = driver.find_element(By.CSS_SELECTOR,"#jsPromptExample > button")
prompt_alert.click()
time.sleep(2)
prompt_alert = driver.switch_to.alert
prompt_alert.send_keys("Noah")
prompt_alert.accept()
pdb.set_trace()