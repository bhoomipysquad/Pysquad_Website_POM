import time
from Pages.insights_dropdown import Insights_Dropdown


class Test_Insights_dropdown:
    def test_insights_Dropdown(self,setup):
        self.driver = setup
        #object of dropdown page
        self.td = Insights_Dropdown(self.driver)
        time.sleep(2)
        self.td.click_and_open_insights()