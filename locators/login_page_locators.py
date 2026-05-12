from selenium.webdriver.common.by import By


class LoginPageLocators:
    # кнопка "Восстановить пароль" на странице авторизации
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, ".//a[text() = 'Восстановить пароль']")
    # Поле email в форме авторизации
    USER_EMAIL_FIELD = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
    # Поле 'Пароль' в форме авторизации
    USER_PASSWORD_FIELD = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")
    # кнопка "Войти" в форме авторизации
    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")
    # кнопка "Конструктор" на странице авторизации
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")