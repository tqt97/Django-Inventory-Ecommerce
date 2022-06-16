import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="function")
def chrome_browser_instance(request):
    """
    Provide a selenium webdriver instance
    """
    options = Options()
    options.headless = False
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.close()
