from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class DocumentViewPage:
    def __init__(self, driver):
        self.driver = driver
        self.canvas = (By.ID, "document-canvas")
        self.download_btn = (By.ID, "download-btn")

    def draw_line(self, start_x=100, start_y=100, end_x=200, end_y=200):
        canvas = self.driver.find_element(*self.canvas)
        action = webdriver.ActionChains(self.driver)
        action.move_to_element_with_offset(canvas, start_x, start_y) \
            .click_and_hold() \
            .move_by_offset(end_x - start_x, end_y - start_y) \
            .release() \
            .perform()
        return self

    def download_document(self):
        self.driver.find_element(*self.download_btn).click()
        return self