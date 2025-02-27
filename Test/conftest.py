import time
import pytest
from selenium import webdriver


Base_url = "https://www.pysquad.com/"

# to open chrome and open URL
@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Base_url)
    time.sleep(2)
    return driver
