import allure
from locators.main_page_locators import MainPageLocators as MP
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Ждем загрузки страницы')
    def wait_main_page(self):
        self.find_and_wait_element_until_visible(MP.SIGN_IN_BUTTON)

    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_sign_in_button(self):
        self.find_and_wait_element_until_visible(MP.SIGN_IN_BUTTON)
        self.click_element(MP.SIGN_IN_BUTTON)

    @allure.step('Клик по кнопке "Личный кабинет"')
    def click_user_account_button(self):
        self.find_and_wait_element_until_visible(MP.USER_ACCOUNT_BUTTON)
        self.click_element(MP.USER_ACCOUNT_BUTTON)

    @allure.step('Ждем загрузки страницы после авторизации')
    def wait_make_order_page(self):
        self.find_and_wait_element_until_visible(MP.MAKE_ORDER_BUTTON)

    @allure.step('Получаем текст заголовка "Соберите бургер"')
    def get_make_burger_text(self):
        self.wait_main_page()
        return self.get_element_text(MP.MAKE_BURGER)

    @allure.step('Клик по кнопке "Лента Заказов"')
    def click_list_order_button(self):
        self.find_and_wait_element_until_visible(MP.LIST_ORDER_BUTTON)
        self.click_element(MP.LIST_ORDER_BUTTON)

    @allure.step('Клик по ингредиенту булка')
    def click_ingredient_bun(self):
        self.find_and_wait_element_until_visible(MP.FLUORESCENT_BUN)
        self.click_element(MP.FLUORESCENT_BUN)

    @allure.step('Закрываем окно с деталями ингредиента')
    def close_popup_with_ingredient_details(self):
        self.find_and_wait_element_until_visible(MP.CLOSE_INGREDIENT)
        self.click_element(MP.CLOSE_INGREDIENT)

    @allure.step('Получаем число со счетчика ингредиента булки')
    def get_count_ingredient_bun(self):
        count = int(self.get_element_text(MP.COUNTER_FLUORESCENT_BUN))
        return count

    @allure.step('Ждем, когда ингредиент булка появится в конструкторе бургера')
    def wait_ingredient_bun_to_constructor_burger(self):
        self.find_and_wait_element_until_visible(MP.FLUORESCENT_BUN_IN_BURGER)

    @allure.step('Перемещение ингредиента булка в конструктор бургера')
    def move_ingredient_bun_to_constructor_burger(self):
        self.move_element(MP.FLUORESCENT_BUN, MP.CONSTRUCTOR_BURGER)
        self.wait_ingredient_bun_to_constructor_burger()

    @allure.step('Клик по кнопке "Заказать бургер"')
    def click_make_order_button(self):
        self.wait_make_order_page()
        self.click_element(MP.MAKE_ORDER_BUTTON)

    @allure.step('Получаем id заказа со всплывающего окна с оформленным заказом')
    def get_id_order_in_popup(self):
        self.wait_text_element_to_change(MP.ID_ORDER, '9999')
        id_order = self.get_element_text(MP.ID_ORDER)
        return f"0{id_order}"

    @allure.step('Закрыть окно с деталями заказа')
    def close_popup_with_order_details(self):
        self.wait_text_element_to_change(MP.ID_ORDER, '9999')
        self.find_and_wait_element_until_clickable(MP.CLOSE_ORDER_DETAILS)
        self.click_element(MP.CLOSE_ORDER_DETAILS)

    @allure.step('Создать заказ')
    def create_order(self):
        self.wait_make_order_page()
        self.move_ingredient_bun_to_constructor_burger()
        self.click_make_order_button()
        self.check_open_popup_with_order()
        self.close_popup_with_order_details()

    @allure.step('Проверяем, что появилось всплывающее окно с деталями игридиента')
    def check_open_popup_with_details_ingredient_bun(self):
        self.find_and_wait_element_until_visible(MP.INGREDIENT_POPUP_TITLE)
        return self.check_displaying_of_element(MP.INGREDIENT_POPUP_TITLE)

    @allure.step('Проверяем, что окно с деталями ингредиента закрылось')
    def check_not_displaying_of_popup_details_ingredient(self):
        self.wait_close_element(MP.INGREDIENT_POPUP_TITLE)
        return self.check_invisibility(MP.INGREDIENT_POPUP_TITLE)

    @allure.step('Проверяем, что появилось всплывающее окно с оформленным заказом')
    def check_open_popup_with_order(self):
        self.find_and_wait_element_until_visible(MP.ORDER_IS_PREPARING)
        return self.check_displaying_of_element(MP.ORDER_IS_PREPARING)

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.find_and_wait_element_until_visible(locator).is_displayed()