import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Data
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators



@allure.feature("Заказ самоката")
class TestOrder:
    @pytest.mark.parametrize("name,surname,address,station,phone,date,period", [
        (   "Михаил",
            "Волков",
            "ул. Лермонтова, 27",
            "Фрунзенская",
            "89171234598",
            "21.05.2025",
            "трое суток"
        ),
        (
            "Петр",
            "Фёдоров",
            "ул. Пушкина, 49",
            "Кремлевская",
            "89054223665",
            "20.05.2025",
            "сутки"
        )
    ])
    def test_order_flow(self, driver, name, surname, address, station, phone, date, period):
        with allure.step("1. Открытие главной страницы"):
            main_page = MainPage(driver)
            main_page.open(Data.main_site)

        with allure.step("2. Принятие куки"):
            main_page.accept_cookies()

        with allure.step("3. Нажатие на кнопку 'Заказать'"):
            main_page.click_order_button()

        with allure.step("4. Заполнение формы 'Для кого самокат'"):
            order_page = OrderPage(driver)
            order_page.fill_name(name)
            order_page.fill_surname(surname)
            order_page.fill_address(address)
            order_page.fill_metro_station(station)
            order_page.fill_phone(phone)

        with allure.step("5. Нажатие кнопки 'Далее'"):
            order_page.click_next_button()

        with allure.step("6. Заполнение формы 'Про аренду'"):
            order_page.fill_delivery_date(date)
            order_page.select_rental_period(period)

        with allure.step("7. Нажатие кнопки 'Заказать'"):
            order_page.click_order_button()

        with allure.step("8. Подтверждение заказа"):
            order_page.confirm_order()

        with allure.step("9. Проверка подтверждения заказа"):
            assert "Заказ оформлен" in order_page.get_success_message()