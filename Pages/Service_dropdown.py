import time
from selenium.webdriver.common.by import By


class Service_Dropdown:
    def __init__(self,driver):
        self.driver = driver

    # to open service dropdown and pages
    services_xpath = '//*[@id="tp-mobile-menu"]/ul/li[2]/a'
    def click_and_open_services(self):
        self.driver.find_element(By.XPATH,self.services_xpath).click()
        time.sleep(2)
        services = { 'web development': "//span[normalize-space()='Web development']",
                     'web design': "//span[normalize-space()='Web design']",
                     'Api design': "//span[normalize-space()='API design']",
                     'Api development': "//span[normalize-space()='App development']",
                     'cloud services': "//span[normalize-space()='Cloud Services']",
                     'ERP': "//span[normalize-space()='ERP']",
                     'product development': "//span[normalize-space()='Product development']",
                     'DBMS': "//span[normalize-space()='DBMS'"
                    }
        for menu,xpath in services.items():
            try:
                element = self.driver.find_element(By.XPATH,xpath)
                element.click()
                time.sleep(2)
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                self.driver.execute_script("window.scrollTo(0, 0);")
                time.sleep(2)
                self.driver.find_element(By.XPATH, self.services_xpath).click()
                time.sleep(2)
            except Exception as e:
                print(f"Error occurred while clicking {menu}: {e}")