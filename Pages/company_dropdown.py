import time
from selenium.webdriver.common.by import By


class Company_Dropdown:
    def __init__(self,driver):
        self.driver = driver

    # to open company dropdown and pages using forloop
    company_xpath = "//a[@target='_self'][normalize-space()='Company']"

    def click_and_open_company(self):
        self.driver.find_element(By.XPATH,self.company_xpath).click()
        time.sleep(3)
        company = { 'About us' : "//span[normalize-space()='About Us']" ,
                    'culture': "//span[normalize-space()='Culture']",
                    'careers': "//span[normalize-space()='Careers']",
                    'contact us': "//span[normalize-space()='Contact Us']"
                   }
        for menu, xpath in company.items():
                try:
                    element = self.driver.find_element(By.XPATH, xpath)
                    element.click()
                    time.sleep(2)
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)
                    self.driver.execute_script("window.scrollTo(0, 0);")
                    time.sleep(2)
                    self.driver.find_element(By.XPATH, self.company_xpath).click()
                    time.sleep(2)
                except Exception as e:
                    print(f"Error occurred while clicking {menu}: {e}")