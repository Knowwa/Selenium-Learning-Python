from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Option 1 is done on Selenium 3
# driver = webdriver.Chrome(executable_path='/Users/noahzertuche/Downloads/chromedriver')
# driver.get("https://google.com")

# Option 1 is done on Selenium 4
# se = Service(executable_path='/Users/noahzertuche/Downloads/chromedriver')
# driver = webdriver.Chrome(service=se)

# Option 2 is adding the executable to the system path. 
# Now that we updated the system path Option 1 won't work anymore
driver = webdriver.Chrome()
driver.get("https://google.com")