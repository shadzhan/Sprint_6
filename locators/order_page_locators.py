from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Шаг 1: Заполнение формы "Для кого самокат"
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Шаг 2: Заполнение формы об аренде
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DROPDOWN_RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")

    # Модальное окно подтверждения
    CONFIRMATION_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")

    # Динамические локаторы
    @staticmethod
    def metro_station_option(station_name: str):
        return (By.XPATH, f"//div[contains(@class, 'select-search__select')]//*[text()='{station_name}']")

    @staticmethod
    def rental_period_option(period: str):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']")

    @staticmethod
    def color_checkbox(color: str):
        return (By.ID, f"{color}")