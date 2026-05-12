import allure
from url import URL

class TestPasswordRecovery:
    @allure.title('Проверяем переход на страницу восстановления пароля по клику на кнопку "Восстановить пароль"')
    def test_open_forgot_password_by_password_recovery_button(self, driver, main_page,
                                                              login_page, password_forgot_page):
        main_page.click_sign_in_button()
        login_page.click_password_recovery_button()
        password_forgot_page.wait_password_forgot_page()
        assert password_forgot_page.get_current_url() == URL.FORGOT_PASSWORD

    @allure.title('Проверяем переход на форму сброса пароля по кнопке "Восстановить"')
    @allure.description('''Заполняем поле email в форме восстановления пароля, кликаем на кнопку "Восстановить", 
                        проверяем, что перешли на форму сброса пароля''')
    def test_open_reset_password_by_recovery_button(self, driver, main_page,
                                                    login_page, password_forgot_page):
        main_page.click_sign_in_button()
        login_page.click_password_recovery_button()
        password_forgot_page.set_email()
        password_forgot_page.click_recovery_button()
        password_forgot_page.wait_save_button_clickable()
        assert password_forgot_page.get_current_url() == URL.RESET_PASSWORD

    @allure.title('Нажатие на кнопку "показать/скрыть пароль" делает поле активным в форме сброса пароля')
    @allure.description('''Заполняем поле email в форме восстановления пароля, кликаем на кнопку "Восстановить", 
                            в форме сброса пароля кликаем по кнопке "Скрыть/показать пароль", проверяем,
                            что поле "Пароль" становится активным"''')
    def test_active_password_field_by_show_hide_password_button(self, driver, main_page, login_page,
                                                                password_forgot_page):
        main_page.click_sign_in_button()
        login_page.click_password_recovery_button()
        password_forgot_page.set_email()
        password_forgot_page.click_recovery_button()
        password_forgot_page.click_show_or_hide_password_button()
        assert password_forgot_page.check_password_field_active()