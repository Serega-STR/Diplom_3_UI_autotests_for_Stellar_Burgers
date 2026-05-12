from selenium.webdriver.common.by import By


class UserAccountPageLocators:
    # Кнопка "Сохранить" в личном кабинете пользователя
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")
    # Кнопка "История заказов" в личном кабинете пользователя
    ORDER_HISTORY_BUTTON = (By.XPATH, ".//a[@href = '/account/order-history']")
    # Кнопка "Выход" в личном кабинете пользователя
    LOGOUT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")
    # id последнего/нижнего заказа в истории заказов
    ID_LAST_ORDER_IN_HISTORY = (By.XPATH, ".//ul[contains(@class, 'OrderHistory')]/li[last()]//"
                                       "div[contains(@class, 'Box__3lgbs mb-6')]/p[contains(@class, 'digits-default')]")
    # кнопка "Лента заказов"
    LIST_ORDER_BUTTON = (By.XPATH, ".//p[text() = 'Лента Заказов']")