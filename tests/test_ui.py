import allure

from src.pages.repository_page import RepositoriesPage


@allure.feature("UI")
def test_guest_cant_open_repo(browser):
    link = 'https://github.com/BenjaminPetrik?tab=repositories'
    repo_page = RepositoriesPage(browser, link)
    repo_page.open()
    with allure.step("Guest can't see private repos"):
        repo_page.guest_should_not_see_private_repositories()


@allure.feature("UI")
def test_user_can_open_repo(browser):
    link = 'https://github.com/BenjaminPetrik?tab=repositories'
    repo_page = RepositoriesPage(browser, link)
    repo_page.open()
    with allure.step("Guest can go to login page"):
        repo_page.go_to_login_page()
    with allure.step("Guest can login"):
        repo_page.user_can_login()
    with allure.step("User can open private repos"):
        repo_page.user_can_open_private_repo()
