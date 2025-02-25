from selenium.webdriver.common.by import By

from pages.document_view_page import DocumentViewPage


class DocumentsPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = (By.CSS_SELECTOR, "input[type='search']")
        self.search_btn = (By.CSS_SELECTOR, "button.search-button")
        self.documents_list = (By.CLASS_NAME, "document-item")

    def search_document(self, query):
        self.driver.find_element(*self.search_input).send_keys(query)
        self.driver.find_element(*self.search_btn).click()
        return self

    def open_first_document(self):
        self.driver.find_elements(*self.documents_list)[0].click()
        return DocumentViewPage(self.driver)