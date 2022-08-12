import pdb
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///Users/NoahZertuche/Desktop/Python_Learning/Selenium_Course/Check_box/checkbox_example.html")

# to_select_value = "61-80"
# locator_by_value = f'input[name="age-group-checkbox"][value="{to_select_value}"]'

# my_choice = driver.find_element(By.CSS_SELECTOR, locator_by_value)
# my_choice.click()
# assert my_choice.is_selected(), f"After selecting {to_select_value} it is not selected. Needs Review!"
# pdb.set_trace()

#Example 2 Verify # of check boxes and if they are selected:
all_checkboxes = driver.find_elements(By.CLASS_NAME, "form-check-input")
exp_num_checkboxes = 4
assert len(all_checkboxes) == exp_num_checkboxes, "Number of checkboxes is incorrect. Investigate!"

for checkbox in all_checkboxes:
    checkbox.click()
    value = checkbox.get_attribute('value')
    if checkbox.is_selected():
        print(f"Checkbox with value {value} is selected!")
    else:
        print(f"Value {value} is not selectable!")

 