from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")


    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DROPDOWN_RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")


    CONFIRMATION_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")


    @staticmethod
    def rental_period_option(period: str):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']")

    @staticmethod
    def STATION_LIST_ITEM(station: str):
        return (By.XPATH, f"//div[contains(text(), '{station}')]")