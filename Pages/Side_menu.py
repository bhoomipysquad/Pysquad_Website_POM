import time
from selenium.webdriver.common.by import By


class Side_menu:
    def __init__(self,driver):
        self.driver =driver

    button_side_xpath = '//*[@id="header-sticky"]/div/div/div/div[1]/div/div[1]'
    button_close_side_xpath = "//*[name()='path' and contains(@d,'M1 1L11 11')]"

    #to open side menubar and close it
    def click_side_button(self):
        self.driver.find_element(By.XPATH,self.button_side_xpath).click()
        time.sleep(3)

    def click_close_side(self):
        self.driver.find_element(By.XPATH,self.button_close_side_xpath).click()
        time.sleep(3)