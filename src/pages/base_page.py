from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from src.pages.locators import BasePageLocators, LoginPageLocators


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(5)

    def is_element_present(self, method, selector):
        try:
            self.browser.find_element(method, selector)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, method, selector):
        try:
            WebDriverWait(self.browser, 2).until(ec.presence_of_element_located((method, selector)))
        except TimeoutException:
            return True
        return False

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.login_link).click()

    def user_can_login(self):
        self.browser.find_element(*LoginPageLocators.username).send_keys('veniamin_petrikovskyi@outlook.com')
        self.browser.find_element(*LoginPageLocators.password).send_keys('Kross1517')
        self.browser.find_element(*LoginPageLocators.login_button).click()
        assert self.is_not_element_present(*LoginPageLocators.error), 'Login has failed!'
