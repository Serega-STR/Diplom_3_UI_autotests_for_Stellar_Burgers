import pytest
from collections import namedtuple
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium import webdriver
from url import URL

from pages.main_page import MainPage as Main
from pages.login_page import LoginPage as Login
from pages.password_forgot_page import PasswordForgotPage as PF
from pages.user_account_page import UserAccountPage as UA
from pages.list_orders_page import ListOrdersPage as LO
from helper import FakeData, Body, Request


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = None
    if request.param == 'chrome':
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('--headless=new')          # раскомментировать, если нужен запуск без графического отображения браузера
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1920, 1080)
    elif request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        profile = FirefoxProfile()
        firefox_options.add_argument('--headless')      # раскомментировать , если нужен запуск без графического отображения браузера
        profile.set_preference("browser.privatebrowsing.autostart", True)
        firefox_options.profile = profile
        driver = webdriver.Firefox(options=firefox_options)
        driver.set_window_size(1920, 1080)
    driver.get(URL.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    main_page = Main(driver)
    return main_page


@pytest.fixture
def login_page(driver):
    login_page = Login(driver)
    return login_page


@pytest.fixture
def password_forgot_page(driver):
    password_forgot_page = PF(driver)
    return password_forgot_page


@pytest.fixture
def user_account_page(driver):
    user_account_page = UA(driver)
    return user_account_page


@pytest.fixture
def list_orders_page(driver):
    list_orders_page = LO(driver)
    return list_orders_page


@pytest.fixture
def authorized_user():
    email = FakeData.email()
    password = FakeData.password()
    name = FakeData.name()
    user_body = Body.build_user_body(email, password, name)
    Request.create_user(user_body)
    login_pass_body = Body.build_login_pass_body(email, password)
    response = Request.login_user(login_pass_body)
    token = response.json()['accessToken']
    UserData = namedtuple('UserData', ['email', 'password', 'name', 'token'])
    yield UserData(email, password, name, token)
    Request.delete_user(token)