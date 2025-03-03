import time
from selenium.webdriver.common.by import By


class Footer:
    def __init__(self,driver):
        self.driver = driver

    #to open contact us page
    def click_on_footer_menus(self):
        quick_links = { "contact_us" : "//div[@class='tp-footer-widget-content']//a[normalize-space()='Contact Us']",
                        "About_us" : "//div[@class='tp-footer-widget-content']//a[normalize-space()='About Us']",
                        "Services" : "//div[@class='tp-footer-widget-content']//a[normalize-space()='Services']",
                        "Blogs" : "//div[@class='tp-footer-widget-content']//a[normalize-space()='Blogs']",
                        "case_studies" : "//a[normalize-space()='Case studies']",
                       }
        for menu, xpath in quick_links.items():
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


    # to open sharelyze app
    sharelyze_xpath = "//a[@class='footer-a ps-2']"
    def open_sharelyze(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.sharelyze_xpath).click()
        time.sleep(2)
        original_window = self.driver.window_handles[0]
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        assert self.driver.current_url == "https://sharelyze.com/"
        self.driver.switch_to.window(original_window)
        time.sleep(2)