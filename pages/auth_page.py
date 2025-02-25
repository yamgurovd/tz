from selenium.webdriver.common.by import By

from pages.main_page import MainPage
from tests.conftest import BASE_URL


class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = BASE_URL

        # Locators
        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "password")
        self.submit_btn = (By.CSS_SELECTOR, "button[type='submit']")
        self.phone_tab = (By.XPATH, "//button[contains(text(), 'Телефон')]")
        self.phone_field = (By.ID, "phone")
        self.token_field = (By.ID, "token")

    def load(self):
        self.driver.get(self.url)

    def login_with_email(self, email, password):
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.submit_btn).click()
        return MainPage(self.driver)

    def switch_to_phone_login(self):
        self.driver.find_element(*self.phone_tab).click()
        return self

    def login_with_phone(self, phone, token):
        self.driver.find_element(*self.phone_field).send_keys(phone)
        self.driver.find_element(*self.token_field).send_keys(token)
        self.driver.find_element(*self.submit_btn).click()
        return MainPage(self.driver)