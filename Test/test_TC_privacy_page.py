from Pages.TC_Privacy_page import TC_Privacy


class Test_Terms_Privacy:
    def test_terms_privacy(self,setup):
        self.driver = setup
        self.tc = TC_Privacy(self.driver)
        self.tc.to_open_tc_privacy_page()
        self.tc.to_open_chat_box()