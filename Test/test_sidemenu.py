import time
from Pages.Side_menu import Side_menu

class Test_Side_menu:
    def test_open_side_menu(self,setup):
        self.driver = setup
        self.sm = Side_menu(self.driver)
        time.sleep(4)
        self.sm.click_side_button()
        self.sm.click_close_side()
