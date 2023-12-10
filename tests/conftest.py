import pytest
import requests
from selenium import webdriver

from helpers import Helpers
from pages.stellar_burgers_login_page import StellarBurgersLoginPage
from pages.stellar_burgers_main_page import StellarBurgersMainPage
from personal_info_data import PersonalInfoData
from urls import Urls


# Настройки драйвера
@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    global driver
    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.delete_all_cookies()
        driver.get(Urls.STELLAR_BURGERS_MAIN_PAGE_URL)
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.delete_all_cookies()
        driver.get(Urls.STELLAR_BURGERS_MAIN_PAGE_URL)

    yield driver
    driver.quit()


# Создание нового пользователя через API
@pytest.fixture()
def get_user_name_email_password():
    user_data = {}
    name = PersonalInfoData.NAME
    email = Helpers.fake_email()
    password = Helpers.password()

    payload = {
        "name": name,
        "email": email,
        "password": password
    }
    response = requests.post(Urls.USER_REGISTRATION_API_URL, data=payload)

    if response.status_code == 200 and response.json()['success'] is True:
        user_data['name'] = name
        user_data['email'] = email
        user_data['password'] = password

        return user_data
    raise Exception('Не удалось зарегистрировать пользователя')


# Логин по почте и паролю
@pytest.fixture()
def login(driver):
    def _login(email, password):
        stellar_burgers_main_page = StellarBurgersMainPage(driver)
        stellar_burgers_main_page.click_on_personal_account_button()
        stellar_burgers_login_page = StellarBurgersLoginPage(driver)
        stellar_burgers_login_page.fill_email_input_field(email)
        stellar_burgers_login_page.fill_password_input_field(password)
        stellar_burgers_login_page.click_on_sign_in_button()
        stellar_burgers_main_page = StellarBurgersMainPage(driver)
        return stellar_burgers_main_page
    return _login
