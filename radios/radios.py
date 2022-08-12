import pdb
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('file:///Users/NoahZertuche/Desktop/Python_Learning/Selenium_Course/radios/radios_example.html')

#Test Case: checking if the default option is selected:
expected_default_value = '21-40'
locator_by_value = 'input[name="age-group-radio"][value="{value}"]'

default_element = driver.find_element(By.CSS_SELECTOR, locator_by_value.format( value = expected_default_value))
"""This is one way of checking"""
# if default_element.is_selected() ==False:
#     print(f"The default value of {expected_default_value} is not selected!")
# else:
#     print("pass")

"""This is another way of checking"""
#assert default_element.is_selected(), f"The default value of {expected_default_value} is not selected!"

#test Case 2, checking if all expected values are working
expected_values = ['21-40','41-60','61-80','81+']
all_radios = driver.find_elements(By.NAME,"age-group-radio")
assert len(all_radios) == len(expected_values), f"The # of radios doesn't = the number of expected values!\nExpected: {len(expected_values)}, Actual: {len(all_radios)}"

#Printing out the displayed value:
for radio in all_radios:
    print(radio.get_attribute('value'))
pdb.set_trace()
