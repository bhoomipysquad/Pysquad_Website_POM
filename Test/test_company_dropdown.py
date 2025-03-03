import time
from Pages.company_dropdown import Company_Dropdown


class Test_company_dropdown:
    def test_company_dropdown(self,setup):
        self.driver = setup
        #object of dropdown page
        self.td = Company_Dropdown(self.driver)
        time.sleep(2)
        self.td.check_right_and_left_button()
        self.td.to_open_culture_page()
        self.td.to_open_careers_page()
        self.td.to_open_contact_us_page()
