import allure
import pytest
from locators.list_orders_page_locators import ListOrdersPageLocators as LO


class TestListOrders:
    @allure.title('Проверяем открытие окна с деталями заказа кликом на заказ')
    def test_open_details_order(self, driver, main_page, list_orders_page):
        main_page.wait_main_page()
        main_page.click_list_order_button()
        list_orders_page.click_first_order_in_list()
        assert list_orders_page.check_open_popup_with_details_order()

    @allure.title('Проверяем: заказы пользователя из «История заказов» отображаются на странице «Лента заказов»')
    def test_displaying_in_list_orders_new_order_from_history(self, driver, main_page, login_page, list_orders_page,
                                                              user_account_page, authorized_user):
        main_page.click_sign_in_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_make_order_page()
        main_page.create_order()
        main_page.click_user_account_button()
        user_account_page.wait_user_account_page()
        user_account_page.click_order_history_button()
        id_last_order = user_account_page.get_id_last_order()
        user_account_page.click_list_order_button()
        list_orders_page.wait_list_orders_page()
        assert list_orders_page.check_id_order_user_in_list_orders(id_last_order)

    @allure.title('Проверяем, что при создании нового заказа счётчик "Выполнено за всё время"/"Выполнено за сегодня"'
                  ' увеличивается')
    @pytest.mark.parametrize('counter', [LO.COUNT_ORDERS_FOR_ALL_TIME,
                                         LO.COUNT_ORDERS_TODAY])
    def test_count_of_orders_increasing_with_new_order(self, driver, main_page, login_page, list_orders_page,
                                                       authorized_user, counter):
        main_page.click_sign_in_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_make_order_page()
        main_page.click_list_order_button()
        count_orders = list_orders_page.get_count_orders(counter)
        list_orders_page.click_constructor_button()
        main_page.create_order()
        main_page.click_list_order_button()
        count_orders_new = list_orders_page.get_count_orders(counter)
        assert count_orders_new > count_orders

    @allure.title('Проверяем, что после оформления заказа его номер появляется в разделе "В работе"')
    def test_new_order_displaying_in_progress_block(self, driver, main_page, login_page, list_orders_page,
                                                    authorized_user):
        main_page.click_sign_in_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_make_order_page()
        main_page.move_ingredient_bun_to_constructor_burger()
        main_page.click_make_order_button()
        main_page.check_open_popup_with_order()
        id_order = main_page.get_id_order_in_popup()
        main_page.close_popup_with_order_details()
        main_page.click_list_order_button()
        id_order_in_processing = list_orders_page.get_id_order_in_processing()
        assert id_order == id_order_in_processing