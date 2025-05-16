import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from curl import Urls

class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self, url):
        self.open_url(Urls.MAIN_SITE)

    @allure.step("Принять куки")
    def accept_cookies(self):
        self.click_on_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Кликнуть на иконку вопроса {number}")
    def click_on_faq_question(self, number):
        self.click_on_element(MainPageLocators.faq_questions_items(number))

    @allure.step("Ожидание появления ответа {number}")
    def wait_for_faq_answer(self, number):
        self.wait_for_element(MainPageLocators.faq_answers_items(number))

    @allure.step("Получение текста ответа {number}")
    def get_faq_answer_text(self, number):
        return self.get_text_on_element(MainPageLocators.faq_answers_items(number))

    @allure.step("Клик по кнопке 'Куки'")
    def click_on_cookie_button(self):
        self.click_on_element(MainPageLocators.COOKIE_BUTTON)


    @allure.step("Кликнуть на кнопку 'Заказать' вверху страницы")
    def click_on_order_button_top(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Ожидание перехода на страницу заказа (сверху)")
    def wait_for_order_page_from_top(self):
        self.wait_for_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Кликнуть на кнопку 'Заказать' внизу страницы")
    def click_on_order_button_bottom(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Ожидание перехода на страницу заказа (снизу)")
    def wait_for_order_page_from_bottom(self):
        self.wait_for_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step("Кликнуть на логотип 'Самокат'")
    def click_on_scooter_logo_and_verify(self):
        self.click_on_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть на логотип 'Яндекс'")
    def click_on_yandex_logo_and_verify(self):
        self.click_on_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Проверить переход на Дзен в новом окне")
    def verify_yandex_redirect(self):
        self.switch_to_new_window()
        self.assert_text_in_url(Urls.YANDEX_DZEN)
