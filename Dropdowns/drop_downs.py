from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('file:///Users/NoahZertuche/Desktop/Python_Learning/Selenium_Course/Dropdowns/drop_down_example.html')

drop_down = driver.find_element(By.ID, "age-range-select")

#Option 1 is using a select class
# drop_down_object = Select(drop_down)

# #select options all have the same result:
# #drop_down_object.select_by_index(3)
# drop_down_object.select_by_value("41-60")

# all_options = drop_down_object.options
# for option in all_options:
#     print(option.text)

#Option 2 find_element by finding li:
driver.find_element(By.ID, 'dropdownMenuButton').click()
dropdown_home = driver.find_element(By.CSS_SELECTOR, "#dropdowns > div:nth-child(3) > div > ul > li:nth-child(1) > a")
dropdown_home.click()

import pdb; pdb.set_trace()