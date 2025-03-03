import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Technologies_Dropdown:
    def __init__(self,driver):
        self.driver = driver

    #to open Technologies dropdown and pages
    technologies_xpath = '//*[@id="tp-mobile-menu"]/ul/li[3]/a'

    #to open python page
    python_xpath = "//span[normalize-space()='Python']"
    def to_open_python_menu(self):
        self.driver.find_element(By.XPATH,self.technologies_xpath).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.python_xpath).click()
        time.sleep(1)
        self.driver.execute_script("window.scrollBy(0, 500);")  # Scrolls down 500 pixels vertically
        hover_event1 = {"hover1": "//p[contains(text(),'Our team boasts seasoned veterans tackling complex')]"  ,  "hover2": "//div[@class='row tp-django-expertise-cards d-flex align-items-stretch gap-5 justify-content-center text-center py-4']//div[2]//div[1]//p[1]",
                       "hover3": "//p[contains(text(),'Witness the power of Python through our portfolio ')]"  ,  "hover4": "//p[contains(text(),'Hear directly from satisfied clients who have tran')]"
                       }
        for menu,xpath in hover_event1.items():
            try:
                actions = ActionChains(self.driver)
                actions.move_to_element(self.driver.find_element(By.XPATH,xpath)).perform()
                time.sleep(1)
            except Exception as e:
                print(f"Error occurred while clicking {menu}: {e}")


    #to open Django page
    Django_xpath = "//span[normalize-space()='Django']"
    def to_open_django_menu(self):
        self.driver.find_element(By.XPATH, self.technologies_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Django_xpath).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 500);")  # Scrolls down 500 pixels vertically
        hover_event2 = { "solid architecture" : "//p[contains(text(),'Our developers are active contributors to the Flut')]"  ,  "rich django" : "//div[@class='row tp-django-expertise-cards d-flex align-items-stretch gap-5 justify-content-center text-center py-4']//div[2]//div[1]//p[1]",
                        "restful API" : "//p[contains(text(),'Bring your app to life with smooth, engaging anima')]"  ,  "testing" : "//div[4]//div[1]//p[1]",
                        "ironclad security" : "//div[5]//div[1]//p[1]"  ,  "Experienced Developers" : "//h6[normalize-space()='Experienced Developers']",
                        "Custom Solutions" : "//h6[normalize-space()='Custom Solutions']"  ,  "Agile Development" : "//h6[normalize-space()='Agile Development']",
                        "Success Guarantee" : "//h6[normalize-space()='Success Guarantee']"  ,  "Dedicated Support" : "//h6[normalize-space()='Dedicated Support']"
                       }
        for menu, xpath in hover_event2.items():
            try:
                actions = ActionChains(self.driver)
                actions.move_to_element(self.driver.find_element(By.XPATH, xpath)).perform()
                time.sleep(1)
            except Exception as e:
                print(f"Error occurred while clicking {menu}: {e}")


    #to open flutter page
    flutter_xpath = "//span[normalize-space()='Flutter']"
    contact_us_button_xpath = "//a[@class='tp-btn']"
    def to_open_flutter_menu(self):
        self.driver.find_element(By.XPATH, self.technologies_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.flutter_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.contact_us_button_xpath).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 500);")  # Scrolls down 500 pixels vertically
        hover_event3 = { 'Team of flutter champions' : "//h4[normalize-space()='Team of Flutter champions']"  ,  'in depth knowledge of architecture' : "//div[contains(@class,'container tp-expertise-part')]//div[2]//div[1]",
                         'animation experts' : "//section[contains(@class,'tp-expertise-section p-relative')]//div[3]//div[1]"  ,  'custom plugin development' : "//h4[normalize-space()='Custom plugin development']",
                         'mobile app development' : "//p[contains(text(),'Build high-performance, native-looking apps for iO')]"  ,  'cross platform app development' : "//p[contains(text(),'Reach a wider audience with one app that works sea')]",
                         'ui/ix design' : "//p[contains(text(),'Craft beautiful, user-friendly interfaces that cap')]"  ,  'performance optimization' : "//h3[normalize-space()='Performance optimization']",
                         'integration and consulting' : "//h3[normalize-space()='Integration and Consulting']"  ,  'ongoing maintenance and support' : "//p[contains(text(),'Keep your app up-to-date and secure with our ongoi')]"
                       }
        for menu, xpath in hover_event3.items():
            try:
                actions = ActionChains(self.driver)
                actions.move_to_element(self.driver.find_element(By.XPATH, xpath)).perform()
                time.sleep(1)
            except Exception as e:
                print(f"Error occurred while clicking {menu}: {e}")


    #to open odoo ERP page
    odoo_erp_xpath = "//span[normalize-space()='Odoo ERP']"
    def to_open_odoo_erp_menu(self):
        self.driver.find_element(By.XPATH, self.technologies_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.odoo_erp_xpath).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, -300);")
        time.sleep(4)

        hover_event4 = { 'implement' : "//div[@class='tp-category-content one']//img[@alt='pysquad-service']"  ,  'customize' : "//div[@class='tp-category-content two']//img[@alt='pysquad-service']"  ,
                          'integrate' : "//div[@class='tp-category-content three']//img[@alt='pysquad-service']"  ,  'deploy' : "//div[@class='tp-category-content four']//img[@alt='pysquad-service']"  ,
                          'training' : "//div[@class='tp-category-content five']//img[@alt='pysquad-service']"
                       }
        for menu, xpath in hover_event4.items():
            try:
                actions = ActionChains(self.driver)
                actions.move_to_element(self.driver.find_element(By.XPATH, xpath)).perform()
                time.sleep(1)
            except Exception as e:
                print(f"Error occurred while clicking {menu}: {e}")


    # to open Fast API
    fast_api_xpath = "//span[normalize-space()='Fast API']"
    start_now_xpath = "//a[contains(@class,'tp-btn px-4 py-2 py-sm-2 py-md-3')]"
    view_all_xpath = "//a[normalize-space()='View all']"
    explore_more_xpath = "//a[@href='/blogs/ai-agent-tech-stack-a-quick-guide-to-building-inte'][normalize-space()='Explore']"

    def to_open_fast_api_menu(self):
        self.driver.find_element(By.XPATH, self.technologies_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.fast_api_xpath).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 500);")  # Scrolls down 500 pixels vertically
        hover_event5 = {'expert developers' : "//p[contains(text(),'Our team of Python specialists has extensive exper')]",
                        'custom API solution' : "//div[contains(@class,'tp-fastapi-expertise-cards d-flex flex-wrap')]//div[2]//div[1]//div[2]//p[1]",
                        'security & scalability' : "//p[contains(text(),'Security is paramount. We prioritize security best')]" ,  'clear & consistent' : "//p[contains(text(),'We believe in clear and consistent communication t')]"
                       }
        for menu, xpath in hover_event5.items():
            try:
                actions = ActionChains(self.driver)
                actions.move_to_element(self.driver.find_element(By.XPATH, xpath)).perform()
                time.sleep(1)
            except Exception as e:
                print(f"Error occurred while clicking {menu}: {e}")

        #to click "start now" button
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.view_all_xpath).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.explore_more_xpath).click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)


     # to open react & next_js page
    react_js_xpath = "//span[normalize-space()='React & NextJs']"
    learn_more_xpath = "//button[@class='px-3 py-2 text-white']"
    def to_open_react_js_menu(self):
        self.driver.find_element(By.XPATH, self.technologies_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.react_js_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.learn_more_xpath).click()
        time.sleep(2)
        assert self.driver.current_url == "https://www.pysquad.com/Learn More"
        # hover_event6 = { 'performance & SEO' : "//div[@class='tp-react-features-cards d-flex flex-wrap justify-content-between text-center py-4 px-3 ']//div[1]//p[1]",
        #        }