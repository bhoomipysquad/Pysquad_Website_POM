import time
from Pages.insights_dropdown import Insights_Dropdown


class Test_Insights_dropdown:
    def test_insights_dropdown(self,setup):
        self.driver = setup
        #object of dropdown page
        self.td = Insights_Dropdown(self.driver)
        time.sleep(2)
        self.td.to_check_case_studies_menu()
        self.td.to_open_blogs_menu()
        self.td.to_open_4ir_menu()