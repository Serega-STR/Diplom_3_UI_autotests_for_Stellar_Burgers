import allure
from locators.login_page_locators import LoginPageLocators as LP
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Ждем когда загрузится страница с формой авторизации')
    def wait_login_page(self):
        self.find_and_wait_element_until_visible(LP.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_password_recovery_button(self):
        self.find_and_wait_element_until_clickable(LP.PASSWORD_RECOVERY_BUTTON)
        self.click_element(LP.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Ввод текста в поле email формы авторизации')
    def set_email(self, email):
        self.find_and_wait_element_until_clickable(LP.USER_EMAIL_FIELD)
        self.set_text_to_element(LP.USER_EMAIL_FIELD, email)

    @allure.step('Ввод текста в поле "Пароль" формы авторизации')
    def set_password(self, password):
        self.find_and_wait_element_until_clickable(LP.USER_PASSWORD_FIELD)
        self.set_text_to_element(LP.USER_PASSWORD_FIELD, password)

    @allure.step('Клик по кнопке "Войти" в форме авторизации')
    def click_login_button(self):
        self.click_element(LP.LOGIN_BUTTON)

    @allure.step('Авторизуемся')
    def login_user(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    @allure.step('Клик по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.find_and_wait_element_until_clickable(LP.CONSTRUCTOR_BUTTON)
        self.click_element(LP.CONSTRUCTOR_BUTTON)