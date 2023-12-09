import allure
from urls import Urls


class TestPersonalAccount:

    @allure.title('Личный Кабинет. Переход по клику на «Личный Кабинет»')
    def test_go_to_personal_account(self, driver, get_user_name_email_password, login):
        user_data = get_user_name_email_password
        stellar_burgers_main_page = login(user_data['email'], user_data['password'])
        stellar_burgers_personal_account_page = stellar_burgers_main_page.go_to_personal_account()
        assert Urls.STELLAR_BURGERS_PERSONAL_ACCOUNT_PROFILE_URL == stellar_burgers_personal_account_page.get_url()

    @allure.title('Личный Кабинет. Переход в раздел «История заказов»')
    def test_go_to_orders_history(self, get_user_name_email_password, login):
        user_data = get_user_name_email_password
        stellar_burgers_main_page = login(user_data['email'], user_data['password'])
        stellar_burgers_personal_account_page = stellar_burgers_main_page.go_to_personal_account()
        stellar_burgers_personal_account_page.click_on_orders_history_button()
        assert Urls.STELLAR_BURGERS_ORDERS_HISTORY_URL == stellar_burgers_personal_account_page.get_url()

    @allure.title('Личный Кабинет. Выход из аккаунта')
    def test_exit_from_personal_account(self, get_user_name_email_password, login):
        user_data = get_user_name_email_password
        stellar_burgers_main_page = login(user_data['email'], user_data['password'])
        stellar_burgers_personal_account_page = stellar_burgers_main_page.go_to_personal_account()
        stellar_burgers_login_page = stellar_burgers_personal_account_page.click_on_exit_button()
        assert Urls.STELLAR_BURGERS_LOGIN_PAGE_URL == stellar_burgers_login_page.get_url()
