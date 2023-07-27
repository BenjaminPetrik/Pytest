from selenium.webdriver.common.by import By


class BasePageLocators:
    login_link = (By.XPATH, '//a[contains(text(), "Sign in")]')


class LoginPageLocators:
    username = (By.ID, 'login_field')
    password = (By.ID, 'password')
    login_button = (By.CSS_SELECTOR, '.btn[type=submit]')
    error = (By.XPATH, '//div[contains(text(), "Incorrect username or passwor")]')


class RepositoriesPageLocators:
    private_repo = (By.XPATH, '//a[contains(text(), "Avast")]')
    repository_header = (By.CSS_SELECTOR, '#repository-container-header a[data-pjax]')

