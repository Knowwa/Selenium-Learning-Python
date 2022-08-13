from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb; import time

driver = webdriver.Chrome()
driver.get('file:///Users/NoahZertuche/Desktop/repos/python_selenium_course/Multiple%20windows%20and%20tabs/windows-and_tabs_example.html')

"""Example 1: How to switch focus to other active windows by searching for all window handles in (pdb)driver.window_handles"""
pg1_btn = driver.find_element(By.CSS_SELECTOR, "#windows > a.btn.btn-warning").click()
#original_window_handle = driver.current_window_handle
all_window_handles = driver.window_handles
original_window_handle = all_window_handles[0]
new_window = all_window_handles[1]

driver.switch_to.window(new_window)
pg1_window_text = driver.find_element(By.CSS_SELECTOR, "body > h1").text
print(f'After switching focus to new active window: {new_window}')
print('Closing Tab')
driver.close()
print('Switching back to original window')
driver.switch_to.window(original_window_handle)
print(driver.title)

pdb.set_trace()
time.sleep(3)
driver.quit()