import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import Data
from curl import main_site
from locators.main_page_locators import MainPageLocators


class TestFaqSection:
    @allure.title("Проверка текста при раскрытии вопросов в FAQ")
    @pytest.mark.parametrize("number, expected_text", Data.accordion_names)
    def test_faq_answers(self, driver, number, expected_text):
        main_page = MainPage(driver)
        main_page.scroll_to_element(MainPageLocators.faq_questions_items[number])
        main_page.click_on_faq_question(number)
        main_page.wait_for_faq_answer(number)
        actual_text = main_page.get_faq_answer_text(number)
        assert actual_text == expected_text