import time
from Test.conftest import Base_url

class Test_Conftest:
 def test_conftest(self,setup):
    self.driver = setup
    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    self.driver.execute_script("window.scrollTo(0, 0);")

    act_url = self.driver.current_url
    if act_url == Base_url:
        assert True
        self.driver.close()
    else:
        self.driver.save_screenshot("openurl.png")
        assert False

