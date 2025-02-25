from selenium.webdriver.common.by import By

from pages.auth_page import AuthPage
from pages.documents_page import DocumentsPage


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.documents_link = (By.LINK_TEXT, "Документы")
        self.logout_btn = (By.LINK_TEXT, "Выход")

    def navigate_to_documents(self):
        self.driver.find_element(*self.documents_link).click()
        return DocumentsPage(self.driver)

    def logout(self):
        self.driver.find_element(*self.logout_btn).click()
        return AuthPage(self.driver)
