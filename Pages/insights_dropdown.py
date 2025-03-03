import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Insights_Dropdown:
    def __init__(self,driver):
        self.driver = driver
    # to open insights dropdown and pages
    insights_xpath = "//a[@target='_self'][normalize-space()='Insights']"

    #to open case studies menu
    case_studies_xpath = "//span[normalize-space()='Case Studies']"
    hover4_xpath = "//a[normalize-space()='Pulse - Transforming Data into Actionable Insights']"
    def to_check_case_studies_menu(self):
        self.driver.find_element(By.XPATH, self.insights_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.case_studies_xpath).click()
        time.sleep(2)
        click_menus = { "hover2" : "//a[contains(text(),'Transforming Education at a Singapore-Based Univer')]", "hover1" : "//a[normalize-space()='Amplifying Campaign Success in the Media Industry']", "hover3" : "//a[contains(text(),'Revolutionizing Data Reconciliation for the Govern')]"
                      }
        for menu,xpath in click_menus.items():
           try:
               self.driver.find_element(By.XPATH, xpath).click()
               time.sleep(1)
               self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
               time.sleep(2)
               self.driver.execute_script("window.scrollTo(0, 0);")
               time.sleep(2)
               self.driver.back()
               time.sleep(2)
           except Exception as e:
               print(f"Error occurred while clicking {menu}: {e}")

        self.driver.execute_script("window.scrollTo(0, 800);")
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.hover4_xpath).click()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        self.driver.back()

        menu2 = { "hover5" : "//a[@href='/case-studies-details/empowering-the-content-modification-and-reselling'][normalize-space()='View Project']",
                  "hover6" : "//a[@href='/case-studies-details/avia-optimizing-stock-management-for-the-aviation'][normalize-space()='View Project']",
                  "hover7" : "//a[@href='/case-studies-details/mediacom-powering-data-streaming-with-big-data-and'][normalize-space()='View Project']"
                  }
        for menu,xpath in menu2.items():
           try:
               self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
               time.sleep(2)
               self.driver.execute_script("window.scrollBy(0, -800);")
               time.sleep(2)
               self.driver.find_element(By.XPATH, xpath).click()
               time.sleep(2)
               self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
               time.sleep(1)
               self.driver.execute_script("window.scrollTo(0, 0);")
               time.sleep(2)
               self.driver.back()
               time.sleep(2)
               self.driver.execute_script("window.scrollBy(0, -800);")
               time.sleep(2)
           except Exception as e:
               print(f"Error occurred while clicking {menu}: {e}")


    # to open Blogs menu
    Blogs_xpath = "//span[normalize-space()='Blogs']"
    def to_open_blogs_menu(self):
        self.driver.find_element(By.XPATH, self.insights_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Blogs_xpath).click()
        time.sleep(2)
        all_work = { "blog1" : "//a[@href='/blogs/ai-agent-tech-stack-a-quick-guide-to-building-inte'][normalize-space()='Read More']",
                     "blog2" : "//a[@href='/blogs/time-series-anomaly-detection-with-pycaret'][normalize-space()='Read More']",
                     "blog3" : "//div[3]//div[1]//div[3]//div[1]//a[1]"
                   }
        for menu,xpath in all_work.items():
           try:
               self.driver.find_element(By.XPATH, xpath).click()
               time.sleep(2)
               self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
               time.sleep(1)
               self.driver.execute_script("window.scrollTo(0, 0);")
               time.sleep(2)
               self.driver.back()
               time.sleep(2)
           except Exception as e:
               print(f"Error occurred while clicking {menu}: {e}")


    # open 4IR menu
    IR_xpath = "//span[normalize-space()='4IR']"
    left_button = "//i[@class='fa-regular fa-arrow-left']"
    right_button = "//i[@class='fa-regular fa-arrow-right']"
    def to_open_4ir_menu(self):
        self.driver.find_element(By.XPATH, self.insights_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.IR_xpath).click()
        time.sleep(2)

        left_click = self.driver.find_element(By.XPATH,self.left_button)
        num_clicks = 5           # Define the number of times you want to click the element
        for i in range(num_clicks):             # Perform the click multiple times
            left_click.click()  # Clicking the element
            time.sleep(1)
        right_click = self.driver.find_element(By.XPATH,self.right_button)
        num_clicks = 5                       # Define the number of times you want to click the element
        # Perform the click multiple times
        for i in range(num_clicks):
            right_click.click()  # Clicking the element
            time.sleep(1)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)
        hover_event = { "innovative mindset" : "//p[@class='hidden text-white text-center align-items-center justify-content-center'][contains(text(),'Proactively adapt to the evolving needs of clients')]",
                        "cutting edge tech" : "//div[@class='row tp-ir-page-innovation']//div[2]//div[1]//p[1]",
                        "user centric design" : "//section[@class='tp-ir-page innovation py-5']//div[3]//div[1]//p[1]",
                        "agile development" : "//p[contains(text(),'We embrace Agile methodologies, fostering a dynami')]",
                        "continuous improvement" : "//p[contains(text(),'Innovation is a journey, not a destination. PySqua')]",
                        "fostering collaboration" : "//p[contains(text(),'Innovation thrives in collaborative environments. ')]",
                        "future ready solutions" : "//p[contains(text(),'Our commitment goes beyond the present. PySquad cr')]",
                        "stretegic vision" : "//div[8]//div[1]//p[1]"
                     }
        for menu, xpath in hover_event.items():
            try:
                actions = ActionChains(self.driver)
                actions.move_to_element(self.driver.find_element(By.XPATH, xpath)).perform()
                time.sleep(4)
            except Exception as e:
                print(f"Error occurred while clicking {menu}: {e}")