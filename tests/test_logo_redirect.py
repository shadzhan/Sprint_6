import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import main_site



class TestLogoRedirects:

    @allure.title("Проверка перехода по клику на логотип Самоката")
    def test_scooter_logo_redirect(self, browser):
        browser.get(main_site)
        scooter_logo = browser.find_element(*self.SCOOTER_LOGO)
        scooter_logo.click()

        WebDriverWait(browser, 10).until(EC.url_contains("/"))
        actual_url = browser.current_url
        assert main_site in actual_url, \
            f"Главная страница Самоката не открылась ({actual_url})"

    @allure.title("Проверка перехода по клику на логотип Яндекса")
    def test_yandex_logo_redirect(self, browser):
        browser.get(main_site)
        yandex_logo = browser.find_element(*self.YANDEX_LOGO)
        yandex_logo.click()

        WebDriverWait(browser, 10).until(EC.number_of_windows_to_be(2))
        browser.switch_to.window(browser.window_handles[-1])

        actual_url = browser.current_url
        assert "https://dzen.ru/" in actual_url, \
            f"Дзен не открылось ({actual_url})"
