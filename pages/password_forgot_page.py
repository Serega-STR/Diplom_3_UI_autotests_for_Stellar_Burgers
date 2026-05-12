import allure
from locators.password_forgot_page_locators import PasswordForgotPageLocators as PF
from pages.base_page import BasePage
from helper import FakeData


class PasswordForgotPage(BasePage):
    @allure.step('Ждем, когда загрузится страница с формой восстановления пароля')
    def wait_password_forgot_page(self):
        self.find_and_wait_element_until_visible(PF.HEADER_PASSWORD_FORGOT_FORM)

    @allure.step('Вводим текст в поле email формы восстановления пароля')
    def set_email(self):
        self.find_and_wait_element_until_clickable(PF.USER_EMAIL_FIELD)
        self.set_text_to_element(PF.USER_EMAIL_FIELD, FakeData.email())

    @allure.step('Клик по кнопке "Восстановить"')
    def click_recovery_button(self):
        self.scroll_to_element(PF.RECOVERY_BUTTON)
        self.click_element(PF.RECOVERY_BUTTON)

    @allure.step('Клик по кнопке "Показать/скрыть пароль"')
    def click_show_or_hide_password_button(self):
        self.find_and_wait_element_until_clickable(PF.SHOW_OR_HIDE_PASSWORD_BUTTON)
        self.click_element(PF.SHOW_OR_HIDE_PASSWORD_BUTTON)

    @allure.step('Ждем пока кнопка "Сохранить" станет кликабельна в форме сброса пароля')
    def wait_save_button_clickable(self):
        self.find_and_wait_element_until_clickable(PF.SAVE_BUTTON)

    @allure.step('Проверяем, что поле "Пароль" активно')
    def check_password_field_active(self):
        return self.find_and_wait_element_until_visible(PF.PASSWORD_FIELD_ACTIVE)