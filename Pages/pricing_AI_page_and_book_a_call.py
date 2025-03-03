import time
from selenium.webdriver.common.by import By


class AI_pricing:
    def __init__(self,driver):
        self.driver = driver

    # to open pricing page
    pricing_xpath = "//a[@target='_self'][normalize-space()='Pricing']"
    def click_and_open_pricing(self):
        self.driver.find_element(By.XPATH,self.pricing_xpath).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

    # to open AI page
    AI_page_xpath = "//a[@class=' ai-text']"
    def click_and_open_ai_page(self):
        self.driver.find_element(By.XPATH,self.AI_page_xpath).click()
        time.sleep(2)
        original_window = self.driver.window_handles[0]
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(original_window)
        time.sleep(2)


    # to click and open "Book a call"
    book_a_call_xpath = "//button[@class='btn ps-1 border-0']"
    close_xpath = "//div[@class='calendly-popup-close']"
    def open_book_a_call(self):
        self.driver.find_element(By.XPATH,self.book_a_call_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.close_xpath).click()
        time.sleep(2)