import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()

