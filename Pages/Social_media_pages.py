import time
from selenium.webdriver.common.by import By


class Social_media:
    def __init__(self,driver):
        self.driver = driver

    # to open social media pages
    def to_open_social_media_pages(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        social_media_xpath = { 'skype' : "//a[@aria-label='Chat with PySquad Informatics on Skype']//i[@class='fab fa-skype']",
                               'Github' : "//a[@aria-label='Visit PySquad Informatics on GitHub']//i[@class='fab fa-github']",
                               'Medium' : "//i[@class='fab fa-medium']",
                               'instagram' : "//i[@class='fab fa-instagram-square']",
                               'Twitter' : "//a[@aria-label='Visit PySquad Informatics on Twitter']//*[name()='svg']",
                               'Linkedin' : "//a[@aria-label='Visit PySquad Informatics on Twitter']//*[name()='svg']"
                             }

        for menu, xpath in social_media_xpath.items():
             try:
                 element = self.driver.find_element(By.XPATH, xpath)
                 element.click()
                 time.sleep(2)
                 original_window = self.driver.window_handles[0]
                 new_window = self.driver.window_handles[1]
                 self.driver.switch_to.window(new_window)
                 time.sleep(2)
                 self.driver.close()
                 self.driver.switch_to.window(original_window)
                 time.sleep(2)
             except Exception as e:
                  print(f"Error occurred while clicking {menu}: {e}")