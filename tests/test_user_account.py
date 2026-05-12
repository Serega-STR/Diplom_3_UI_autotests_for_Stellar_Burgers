import allure
from url import URL


class TestUserAccount:
    @allure.title('Проверяем переход в личный кабинет пользователя по клику на кнопку "Личный кабинет"')
    def test_open_user_account(self, driver, main_page, login_page, user_account_page, authorized_user):
        main_page.click_sign_in_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_make_order_page()
        main_page.click_user_account_button()
        user_account_page.wait_user_account_page()
        assert user_account_page.get_current_url() == URL.ACCOUNT_PROFILE

    @allure.title('Проверяем переход в историю заказов в личном кабинете')
    def test_open_order_history(self, driver, main_page, login_page, user_account_page, authorized_user):
        main_page.click_sign_in_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_make_order_page()
        main_page.click_user_account_button()
        user_account_page.wait_user_account_page()
        user_account_page.click_order_history_button()
        assert user_account_page.get_current_url() == URL.ORDER_HISTORY

    @allure.title('Проверяем выход из аккаунта по клику на кнопку "Выход" в личном кабинете')
    def test_logout(self, driver, main_page, login_page, user_account_page, authorized_user):
        main_page.click_sign_in_button()
        login_page.login_user(authorized_user.email, authorized_user.password)
        main_page.wait_make_order_page()
        main_page.click_user_account_button()
        user_account_page.wait_user_account_page()
        user_account_page.click_logout_button()
        login_page.wait_login_page()
        assert login_page.get_current_url() == URL.LOGIN