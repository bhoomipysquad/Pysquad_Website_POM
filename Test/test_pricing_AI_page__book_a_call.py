from Pages.pricing_AI_page_and_book_a_call import AI_pricing


class Test_AI_Pricing:
     def test_ai_pricing(self,setup):
          self.driver = setup
          self.ai = AI_pricing(self.driver)
          self.ai.click_and_open_pricing()
          self.ai.click_and_open_ai_page()
          self.ai.open_book_a_call()