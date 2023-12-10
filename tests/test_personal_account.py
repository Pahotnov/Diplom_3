import allure

from pages.stellar_burgers_login_page import StellarBurgersLoginPage
from pages.stellar_burgers_personal_account_page import StellarBurgersPersonalAccountPage
from urls import Urls


class TestPersonalAccount:

    @allure.title('Личный Кабинет. Переход по клику на «Личный Кабинет»')
    def test_go_to_personal_account(self, driver, get_user_name_email_password, login):
        user_data = get_user_name_email_password
        stellar_burgers_main_page = login(user_data['email'], user_data['password'])
        stellar_burgers_main_page.click_on_personal_account_button()
        stellar_burgers_personal_account_page = StellarBurgersPersonalAccountPage(driver)
        stellar_burgers_personal_account_page.click_on_profile_button()
        assert Urls.STELLAR_BURGERS_PERSONAL_ACCOUNT_PROFILE_URL == stellar_burgers_personal_account_page.get_url()

    @allure.title('Личный Кабинет. Переход в раздел «История заказов»')
    def test_go_to_orders_history(self, driver, get_user_name_email_password, login):
        user_data = get_user_name_email_password
        stellar_burgers_main_page = login(user_data['email'], user_data['password'])
        stellar_burgers_main_page.click_on_personal_account_button()
        stellar_burgers_personal_account_page = StellarBurgersPersonalAccountPage(driver)
        stellar_burgers_personal_account_page.click_on_orders_history_button()
        assert Urls.STELLAR_BURGERS_ORDERS_HISTORY_URL == stellar_burgers_personal_account_page.get_url()

    @allure.title('Личный Кабинет. Выход из аккаунта')
    def test_exit_from_personal_account(self, driver, get_user_name_email_password, login):
        user_data = get_user_name_email_password
        stellar_burgers_main_page = login(user_data['email'], user_data['password'])
        stellar_burgers_main_page.click_on_personal_account_button()
        stellar_burgers_personal_account_page = StellarBurgersPersonalAccountPage(driver)
        stellar_burgers_personal_account_page.click_on_exit_button()
        stellar_burgers_login_page = StellarBurgersLoginPage(driver)
        stellar_burgers_login_page.click_on_enter_title()
        assert Urls.STELLAR_BURGERS_LOGIN_PAGE_URL == stellar_burgers_login_page.get_url()
