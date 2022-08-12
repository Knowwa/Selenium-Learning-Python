from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb
import time

driver = webdriver.Chrome()
driver.get('file:///Users/NoahZertuche/Desktop/repos/python_selenium_course/iframes/iFrames_example.html')

"""Example 1: Verify alert text in (button outside iframe) returns the correct text."""
# btn_outside_iframe = driver.find_element(By.ID,"btnOutFrame").click()
# out_alert = driver.switch_to.alert
# alert_text = out_alert.text
# expected_alert_text = 'Just Clicked Outside iFrame'
# time.sleep(2)
# assert alert_text == expected_alert_text, f'Error!: Alert text is incorrect. Expected text: {expected_alert_text} Returned: {alert_text}'
# out_alert.accept()
#-----------------------------------------------------------------------------------------------------------------------------------------------

"""Example 2: How to locate elements in iframe using web-element, then verify button inside iframe returns the correct text."""
# iframe_1 = driver.find_element(By.ID,"myFrame1")
# #if you want to work with an element that is inside a frame you have to .switch_to the frame
# driver.switch_to.frame(iframe_1)
# driver.find_element(By.ID,"btnInFrame").click()
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.dismiss()

# #!!!!Once the focus is on the inside frame you must .switch_to the original content.
# driver.switch_to.default_content()
# driver.find_element('id', 'btnOutFrame').click()
# print(driver.switch_to.alert.text)
#------------------------------------------------------------------------------------------------------------------------------------------------

"""Example 3: using frame id instead web element when switching to frame"""
# driver.switch_to.frame('myFrame1')
# driver.find_element(By.ID, "btnInFrame").click()
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.accept()
#------------------------------------------------------------------------------------------------------------------------------------------------
"""Example 4: using frame index instead web element or ID when switching to frame"""
driver.switch_to.frame(0)
driver.find_element(By.ID, "btnInFrame").click()
time.sleep(3)
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()