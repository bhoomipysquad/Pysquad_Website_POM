import time
from Pages.company_dropdown import Company_Dropdown


class Test_company_dropdown:
    def test_company_Dropdown(self,setup):
        self.driver = setup
        #object of dropdown page
        self.td = Company_Dropdown(self.driver)
        time.sleep(2)
        self.td.click_and_open_company()