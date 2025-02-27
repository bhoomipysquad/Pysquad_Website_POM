import time
from selenium.webdriver.common.by import By


class TC_Privacy:
    def __init__(self,driver):
        self.driver = driver

    # to open t&c and privacy page
    def to_open_tc_privacy_page(self):
        tc_and_privacy = { "Terms_and_condition" : "//a[normalize-space()='Terms and conditions']",
                       "Privacy" : "//a[@class='ml-50']"
                     }
        for menu, xpath in tc_and_privacy.items():
             try:
                 self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                 time.sleep(2)
                 element = self.driver.find_element(By.XPATH, xpath)
                 element.click()
                 time.sleep(2)
                 self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                 time.sleep(2)
                 self.driver.execute_script("window.scrollTo(0, 0);")
                 time.sleep(2)
                 self.driver.back()
                 time.sleep(2)
             except Exception as e:
                  print(f"Error occurred while clicking {menu}: {e}")


    # to open chatbox
    chatbox_xpath = "//i[@class='fa-solid fa-messages']"
    def to_open_chatbox(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.chatbox_xpath).click()
        time.sleep(2)
        original_window = self.driver.window_handles[0]
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(original_window)
        time.sleep(2)



