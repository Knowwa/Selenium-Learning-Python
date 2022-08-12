import pdb
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://meletrix.com/products/zoom65-essential-edition")

case_option = driver.find_element(By.CLASS_NAME, "single-option-selector")
drop_down_obj = Select(case_option)

option_1 = drop_down_obj.select_by_value("Black Cases")
option_2 = drop_down_obj.select_by_value("Cool Grey Cases")
option_3 = drop_down_obj.select_by_value("Navy Cases")

option_1.is_enabled()


# all_options = drop_down_obj.options
# for option in all_options: 
#     if option.is_enabled() == True and option.text == "Black Cases":
#         drop_down_obj.select_by_value(f"{option.text}")
    
#     else:
#         print(f"{option.text} is not avalible!")

#easier way:
#create variables as options ex) option1= true click
                                #else: option2 = click
                                


pdb.set_trace()