import time
from selenium.webdriver.common.by import By


class Insights_Dropdown:
    def __init__(self,driver):
        self.driver = driver

    # to open insights dropdown and pages
    insights_xpath = "//a[@target='_self'][normalize-space()='Insights']"

    def click_and_open_insights(self):
        self.driver.find_element(By.XPATH,self.insights_xpath).click()
        time.sleep(3)
        insights = { 'case studies' : "//span[normalize-space()='Case Studies']",
                         'Blogs': "//span[normalize-space()='Blogs']",
                         '4IR': "//span[normalize-space()='4IR']"
                    }
        for menu, xpath in insights.items():
                try:
                    element = self.driver.find_element(By.XPATH, xpath)
                    element.click()
                    time.sleep(2)
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)
                    self.driver.execute_script("window.scrollTo(0, 0);")
                    time.sleep(2)
                    self.driver.find_element(By.XPATH, self.insights_xpath).click()
                    time.sleep(2)
                except Exception as e:
                    print(f"Error occurred while clicking {menu}: {e}")