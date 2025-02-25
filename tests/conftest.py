import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv

load_dotenv()

from selenium.webdriver.common.by import By

BASE_URL = os.getenv('BASE_URL')
DOWNLOAD_DIR = os.path.join(os.getcwd(), "downloads")


@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
    })
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

    for f in os.listdir(DOWNLOAD_DIR):
        os.remove(os.path.join(DOWNLOAD_DIR, f))
