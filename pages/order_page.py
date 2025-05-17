import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step("Заполнить поле имени: {name}")
    def fill_name(self, name):
        self.send_keys_to_input(OrderPageLocators.NAME_INPUT, name)

    @allure.step("Заполнить поле фамилия: {surname}")
    def fill_surname(self, surname):
        self.send_keys_to_input(OrderPageLocators.SURNAME_INPUT, surname)

    @allure.step("Заполнить поле адреса: {address}")
    def fill_address(self, address):
        self.send_keys_to_input(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step("Заполнить поле станция метро: {station}")
    def fill_metro_station(self, station):
        self.click_on_element(OrderPageLocators.METRO_STATION_INPUT)
        self.send_keys_to_input(OrderPageLocators.METRO_STATION_INPUT, station)
        self.wait_for_element(OrderPageLocators.STATION_LIST_ITEM(station))
        self.click_on_element(OrderPageLocators.STATION_LIST_ITEM(station))

    @allure.step("Заполнить поле телефона: {phone}")
    def fill_phone(self, phone):
        self.send_keys_to_input(OrderPageLocators.PHONE_INPUT, phone)


    @allure.step("Кликнуть на кнопку 'Далее'")
    def click_next_button(self):
        self.click_on_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить поле 'Дата' значением '{date}'")
    def fill_delivery_date(self, date):
        self.send_keys_to_input(OrderPageLocators.DATE_INPUT, date)

    @allure.step("Выбрать срок аренды '{period}'")
    def select_rental_period(self, period):
        self.click_on_element(OrderPageLocators.DROPDOWN_RENTAL_PERIOD)
        period_locator = OrderPageLocators.rental_period_option(period)
        self.click_on_element(period_locator)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ в модальном окне")
    def confirm_order(self):
        self.wait_for_element(OrderPageLocators.CONFIRMATION_MODAL)
        self.click_on_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Получить текст 'Заказ оформлен'")
    def get_success_message(self):
        self.wait_for_element(OrderPageLocators.SUCCESS_MESSAGE)
        return self.get_text_on_element(OrderPageLocators.SUCCESS_MESSAGE)




