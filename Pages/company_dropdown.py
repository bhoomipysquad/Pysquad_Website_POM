import time
from telnetlib import EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Company_Dropdown:
    def __init__(self,driver):
        self.driver = driver
    company_xpath = "//a[@target='_self'][normalize-space()='Company']"

    # XPaths for left and right buttons
    About_xpath = "//span[normalize-space()='About Us']"
    left_button = "//i[@class='fa-regular fa-arrow-left']"
    right_button = "//i[@class='fa-regular fa-arrow-right']"

    def check_right_and_left_button(self):
        # Click on the company element first
        self.driver.find_element(By.XPATH, self.company_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.About_xpath).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 400);")
        time.sleep(2)

        # Left button clicking logic
        left_button_click = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.left_button))
        )
        num_clicks = 5
        successful_left_clicks = 0
        for i in range(num_clicks):
            try:
                left_button_click.click()  # Click the left button
                time.sleep(1)  # Allow some time for the action to happen

                # Assert that the button is still clickable (optional, based on button behavior)
                assert left_button_click.is_enabled(), "Left button is not enabled after click."
                print(f"Left button clicked {i + 1} times successfully.")

                # You can also check if some expected change happens after clicking (e.g., page or element change)
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "some_element_to_appear_after_click"))
                )
                successful_left_clicks += 1  # Increment successful clicks

            except Exception as e:
                print(f"Error after left button click {i + 1}: {e}")
                break  # Stop clicking if there's an issue with the button

        # Assert that all 5 left button clicks were successful
        assert successful_left_clicks == num_clicks, f"Left button failed to click {num_clicks} times in a row."

        # Right button clicking logic
        right_button_click = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.right_button))
        )
        successful_right_clicks = 0
        for i in range(num_clicks):
            try:
                right_button_click.click()  # Click the right button
                time.sleep(1)  # Allow some time for the action to happen

                # Assert that the button is still clickable (optional)
                assert right_button_click.is_enabled(), "Right button is not enabled after click."
                print(f"Right button clicked {i + 1} times successfully.")

                # You can also check if some expected change happens after clicking
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "some_element_to_appear_after_click"))
                )
                successful_right_clicks += 1  # Increment successful clicks

            except Exception as e:
                print(f"Error after right button click {i + 1}: {e}")
                break  # Stop clicking if there's an issue with the button

        # Assert that all 5 right button clicks were successful
        assert successful_right_clicks == num_clicks, f"Right button failed to click {num_clicks} times in a row."


    #to open culture page
    culture_xpath = "//span[normalize-space()='Culture']"
    def to_open_culture_page(self):
        self.driver.find_element(By.XPATH, self.company_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.culture_xpath).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 400);")
        time.sleep(2)


    # to open careers page
    careers_xpath = "//span[normalize-space()='Careers']"
    def to_open_careers_page(self):
        self.driver.find_element(By.XPATH, self.company_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.careers_xpath).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 400);")
        time.sleep(2)
        careers = { "sales" : "/html[1]/body[1]/div[1]/main[1]/section[2]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[1]/a[1]","frontend" : "//a[@class='active']", "backend" : "//a[normalize-space()='Backend']" }
        for menu,xpath in careers.items():
           try:
               self.driver.find_element(By.XPATH, xpath).click()
               time.sleep(2)
           except Exception as e:
               print(f"Error occurred while clicking {menu}: {e}")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, -800);")
        time.sleep(2)

        hover = {"fun and engaging culture" : "//section[contains(@class,'tp-careerPage-benefits py-3 py-md-5')]//div[contains(@class,'container container-1350')]//div[1]//div[1]" ,
                 "collaborative environmanet": "//div[contains(@class,'circle-card text-center rounded-circle d-flex flex-column align-items-center justify-content-center py-4 px-2 p-relative')]//div[contains(@class,'h-100 d-flex flex-column align-items-center justify-content-center')]",
                 "learning opportunities" : "//section[contains(@class,'tp-careerPage-benefits py-3 py-md-5')]//div[3]//div[1]" ,  "Team events" : "//main//div[4]//div[1]//img[1]"
                 }
        for menu, xpath in hover.items():
            try:
                actions = ActionChains(self.driver)
                actions.move_to_element(self.driver.find_element(By.XPATH, xpath)).perform()
                time.sleep(1)
            except Exception as e:
                print(f"Error occurred while clicking {menu}: {e}")


    #to open contact us page
    contactus_xpath = "//span[normalize-space()='Contact Us']"
    india_xpath = "//p[contains(text(),'A 605, Shilp Aaron,Sindhu Bhavan Road, Ahmedabad, ')]"
    uk_xpath = "//p[normalize-space()='2, sunkist way, Wallington,SM6 9LQ']"
    def to_open_contact_us_page(self):
        self.driver.find_element(By.XPATH, self.company_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.contactus_xpath).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.india_xpath).click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.uk_xpath).click()
        time.sleep(2)