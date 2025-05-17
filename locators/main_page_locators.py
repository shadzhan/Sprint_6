from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_BUTTON_TOP = (By.CSS_SELECTOR, "button.Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    COOKIE_BUTTON = (By.XPATH, "//div[contains(@class, 'App_CookieText__1sbqp')]")

    SCOOTER_LOGO = (By.CSS_SELECTOR, "img[src='/assets/scooter.svg'][alt='Scooter']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "img[src='/assets/ya.svg'][alt='Yandex']")

    @staticmethod
    def faq_questions_items(number):
        return By.ID, f"accordion__heading-{number}"

    @staticmethod
    def faq_answers_items(number):
        return By.ID, f"accordion__panel-{number}"


