from selenium.webdriver.common.by import By


class PasswordForgotPageLocators:
    # заголовок в форме восстановления пароля
    HEADER_PASSWORD_FORGOT_FORM = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']/h2")
    # поле email в форме восстановления пароля
    USER_EMAIL_FIELD = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
    # кнопка "Восстановить" на странице восстановления пароля
    RECOVERY_BUTTON = (By.XPATH, ".//button[text() = 'Восстановить']")
    # кнопка "Показать/скрыть пароль"
    SHOW_OR_HIDE_PASSWORD_BUTTON = (By.XPATH, ".//div[contains(@class, 'input__icon-action')]")
    # поле "Пароль" в активном состоянии
    PASSWORD_FIELD_ACTIVE = (By.CSS_SELECTOR, '.input.input_status_active')
    # кнопка "Сохранить" в форме сброса пароля
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")