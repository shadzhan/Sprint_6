import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step("Заполнить поле имени: {name}")
    def fill_name(self, name):
        self.send_keys_to_input(OrderPageLocators.NAME_INPUT, name)

    @allure.step("Заполнить поле телефона: {phone}")
    def fill_phone(self, phone):
        self.send_keys_to_element(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step("Заполнить поле адреса: {address}")
    def fill_address(self, address):
        self.send_keys_to_element(OrderPageLocators.ADDRESS_FIELD, address)


    @allure.step("Кликнуть на кнопку 'Подтвердить заказ'")
    def click_confirm_order(self):
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Ожидание появления подтверждения заказа")
    def wait_for_confirmation_message(self):
        self.wait_for_element(OrderPageLocators.CONFIRMATION_MESSAGE)

    @allure.step("Получить текст сообщения подтверждения")
    def get_confirmation_text(self):
        return self.get_text_on_element(OrderPageLocators.CONFIRMATION_MESSAGE)

    @allure.step("Заполнить все обязательные поля и оформить заказ")
    def complete_order(self, name, phone, address, payment_method):
        self.fill_name(name)
        self.fill_phone(phone)
        self.fill_address(address)
        self.select_payment_method(payment_method)
        self.click_confirm_order()
        self.wait_for_confirmation_message()
        return self.get_confirmation_text()
