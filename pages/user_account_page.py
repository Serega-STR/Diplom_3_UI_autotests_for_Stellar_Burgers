import allure
from pages.base_page import BasePage
from locators.user_account_locators import UserAccountPageLocators as UA


class UserAccountPage(BasePage):
    @allure.step('Ждем, пока загрузится личный кабинет пользователя')
    def wait_user_account_page(self):
        self.find_and_wait_element_until_visible(UA.SAVE_BUTTON)

    @allure.step('Клик по кнопке "История заказов" в личном кабинете пользователя')
    def click_order_history_button(self):
        self.find_and_wait_element_until_visible(UA.ORDER_HISTORY_BUTTON)
        self.click_element(UA.ORDER_HISTORY_BUTTON)

    @allure.step('Клик по кнопке "Выход" в личном кабинете пользователя')
    def click_logout_button(self):
        self.find_and_wait_element_until_visible(UA.LOGOUT_BUTTON)
        self.click_element(UA.LOGOUT_BUTTON)

    @allure.step('Получаем id последнего заказа пользователя')
    def get_id_last_order(self):
        self.find_and_wait_element_until_visible(UA.ID_LAST_ORDER_IN_HISTORY)
        return self.get_element_text(UA.ID_LAST_ORDER_IN_HISTORY)

    @allure.step('Клик по кнопке "Лента заказов" в личном кабинете пользователя')
    def click_list_order_button(self):
        self.find_and_wait_element_until_visible(UA.LIST_ORDER_BUTTON)
        self.click_element(UA.LIST_ORDER_BUTTON)