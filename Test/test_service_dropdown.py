import time
from Pages.Service_dropdown import Service_Dropdown


class Test_Service_dropdown:
    def test_service_dropdown(self,setup):
        self.driver = setup
        #object of dropdown page
        self.sd = Service_Dropdown(self.driver)
        time.sleep(2)
        self.sd.click_and_open_services()

