from selenium import webdriver; import time
from selenium.webdriver.common.by import By;

"""Verify invalid user login"""

class InvalidUserLoginError:

    invalid_email = 'noah.alex@supersqa.com'
    expected_error_messg = 'Unknown email address. Check again or try your username.'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://demostore.supersqa.com/my-account/')
        self.driver.implicitly_wait(10)

    def input_email(self):
        field = self.driver.find_element(By.ID,"username")
        field.send_keys(InvalidUserLoginError.invalid_email)

    def input_password(self):
        field = self.driver.find_element(By.ID,"password")
        field.send_keys('abcd132445')

    def click_login(self):
        field = self.driver.find_element(By.NAME,"login")
        field.click()

    def verify_error_messg(self):
        verify = self.driver.find_element(By.CSS_SELECTOR, "#content > div > div.woocommerce > ul > li")
        if InvalidUserLoginError.expected_error_messg == verify.text:
            print("PASS")
        else:
            print(f"ERROR: Displayed login error message text does not match Expected_error_messg: {self.expected_error_messg}")
        
    def main(self):
        self.input_email()
        self.input_password()
        self.click_login()
        self.verify_error_messg()
        self.driver.quit()


if __name__ == '__main__':
    obj = InvalidUserLoginError()
    obj.main()

