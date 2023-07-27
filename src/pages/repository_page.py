from .base_page import BasePage
from .locators import RepositoriesPageLocators, BasePageLocators


class RepositoriesPage(BasePage):
    def guest_should_not_see_private_repositories(self):
        assert self.is_element_present(*BasePageLocators.login_link), \
            'The user is logged in already'
        assert self.is_not_element_present(*RepositoriesPageLocators.private_repo), \
            'Guest can see the private repo'

    def user_can_open_private_repo(self):
        self.browser.find_element(*RepositoriesPageLocators.private_repo).click()
        header = self.browser.find_element(*RepositoriesPageLocators.repository_header).text
        assert 'AvastAutomationTestVeniamin' == header, 'This is not an AVAST repository'
