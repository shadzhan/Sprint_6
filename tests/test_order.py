import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Data
from curl import main_site
from locators.main_page_locators import MainPageLocators
from helper import generate_registration_data



@allure.feature("Заказ самоката")
class TestOrder:

    @pytest.mark.parametrize("button_locator", [
        MainPageLocators.ORDER_BUTTON_TOP,
        MainPageLocators.ORDER_BUTTON_BOTTOM
    ], ids=["top_button", "bottom_button"])
    def test_order_flow(self, driver, button_locator):
        with allure.step("Инициализация страниц и данных"):
            main_page = MainPage(driver)
            order_page = OrderPage(driver)
            user_data = Data.get_test_user()

        with allure.step("1. Принимаем куки"):
            main_page.click_on_cookia_button()

        button_info = {
            MainPageLocators.ORDER_BUTTON_TOP: "Верхняя кнопка 'Заказать'",
            MainPageLocators.ORDER_BUTTON_BOTTOM: "Нижняя кнопка 'Заказать'"
        }

        with allure.step(f"2. Нажимаем {button_info[button_locator]}"):
            main_page.click_order_button(button_locator)

        with allure.step("3. Заполняем форму 'Для кого самокат'"):
            order_page.fill_recipient_form(user_data)

        with allure.step("4. Нажимаем кнопку 'Далее'"):
            order_page.click_next_button()

        with allure.step("5. Заполняем форму 'Про аренду'"):
            order_page.fill_rental_details(user_data)

        with allure.step("6. Нажимаем кнопку 'Заказать'"):
            order_page.click_order_button()

        with allure.step("7. Подтверждаем заказ"):
            order_page.click_confirm_button()

        with allure.step("8. Проверяем подтверждение заказа"):
            assert order_page.verify_order_confirmation()

        with allure.step("9. Нажимаем кнопку 'Посмотреть статус'"):
            order_page.click_view_status_button()