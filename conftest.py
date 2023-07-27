import pytest
import logging
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    logging.info('Starting Chrome browser...')
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    logging.info('Closing browser session...')
    browser.quit()
