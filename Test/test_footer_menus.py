from Pages.footer_menus import Footer


class Test_Footer_Menus:
    def test_footer_menus(self,setup):
        self.driver = setup
        self.fm = Footer(self.driver)
        self.fm.click_on_footer_menus()
        self.fm.open_sharelyze()
