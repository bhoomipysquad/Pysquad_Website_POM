from Pages.Social_media_pages import Social_media


class Test_Social_Media:
    def test_social_media_pages(self,setup):
        self.driver = setup
        self.sm = Social_media(self.driver)
        self.sm.to_open_social_media_pages()