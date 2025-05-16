import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import Urls
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage



class TestLogoRedirects:
    @allure.title("Проверка перехода по клику на логотип Самоката")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open(Urls.MAIN_SITE)

        with allure.step("Кликнуть на логотип Самоката"):
            main_page.click_on_scooter_logo_and_verify()


    @allure.title("Проверка перехода по клику на логотип Яндекса")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.open(Urls.MAIN_SITE)

        with allure.step("Кликнуть на логотип Яндекса"):
            main_page.click_on_yandex_logo_and_verify()

        with allure.step("Проверить переход на Дзен"):
            main_page.switch_to_new_window()
            main_page.verify_yandex_redirect()







