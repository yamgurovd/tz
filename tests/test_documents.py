import os

import pytest

from dotenv import load_dotenv

from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.documents_page import DocumentsPage
from pages.document_view_page import DocumentViewPage

load_dotenv()

VALID_EMAIL = os.getenv('BASE_URL')
VALID_PASSWORD = os.getenv('PASSWORD')


class TestDocumentWorkflow:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.auth_page = AuthPage(browser)
        self.auth_page.load()

    def test_full_document_workflow(self, browser):
        main_page = self.auth_page.login_with_email(VALID_EMAIL, VALID_PASSWORD)

        documents_page = main_page.navigate_to_documents()

        documents_page.search_document("Договор_Тест_2024")

        document_view_page = documents_page.open_first_document()

        document_view_page.draw_line()

        document_view_page.download_document()

        files = os.listdir(DOWNLOAD_DIR)
        assert any(file.startswith("Договор_Тест_2024") for file in files)

    def test_phone_auth_document_access(self, browser):
        pytest.skip("Phone auth test in development")
