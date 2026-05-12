from selenium.webdriver.common.by import By


class ListOrdersPageLocators:
    # заголовок "Выполнено за все время" на странице "Лента заказов"
    ORDERS_FOR_ALL_TIME = (By.XPATH, ".//p[contains(text(), 'Выполнено за все время')]")
    # количестово заказов за всё время на странице "Лента заказов"
    COUNT_ORDERS_FOR_ALL_TIME = (By.XPATH, ".//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    # количестово заказов за сегодня на странице "Лента заказов"
    COUNT_ORDERS_TODAY = (By.XPATH, ".//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    # заголовок "Лента заказов" на странице "Лента заказов"
    LIST_ORDERS_HEADER = (By.XPATH, ".//div[contains(@class, 'OrderFeed')]/h1[contains(@class, 'mt-10 mb-5')]")
    # первый/верхний заказ в истории заказов на странице "Лента заказов"
    FIRST_ORDER_IN_LIST = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]")
    # попап с деталями заказа на странице "Лента заказов"
    ORDER_POPUP_DETAILS = (By.XPATH, ".//p[text() = 'Cостав']/ancestor::div[contains(@class, 'container__Wo2l')]")
    # кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")
    # заказ в разделе "В работе"
    ORDER_IN_PROCESSING = (By.XPATH, ".//ul[contains(@class, 'orderListReady')]/li[contains(@class, 'default mb-2')]")

    # метод, возвращающий локатор для поиска заказа пользователя по id в "Ленте заказов"
    @staticmethod
    def search_order_by_id(id_order):
        return By.XPATH, f'.//ul[contains(@class, "OrderFeed_list")]//p[text() = "{id_order}"]'