import allure
from pages.stellar_burgers_main_page import StellarBurgersMainPage
from urls import Urls


class TestMainFunctionality:

    @allure.title('Проверка основного функционала. Переход по клику на «Конструктор»')
    def test_go_to_constructor_section(self, driver):
        stellar_burgers_main_page = StellarBurgersMainPage(driver)
        stellar_burgers_main_page.go_to_constructor()
        assert stellar_burgers_main_page.check_constructor_button_is_active()
        assert stellar_burgers_main_page.check_burger_ingredients_section_on_page()
        assert stellar_burgers_main_page.check_burger_constructor_section_on_page()

    @allure.title('Проверка основного функционала. Переход по клику на «Лента заказов»')
    def test_go_to_list_of_orders_section(self, driver):
        stellar_burgers_main_page = StellarBurgersMainPage(driver)
        stellar_burgers_main_page.go_to_list_of_orders()
        assert stellar_burgers_main_page.get_url() == Urls.STELLAR_BURGERS_LIST_OF_ORDERS_URL
        assert stellar_burgers_main_page.check_list_of_orders_button_is_active()
        assert stellar_burgers_main_page.check_list_of_orders_section_on_page()

    @allure.title('Проверка основного функционала. Проверка появления окна "Детали ингредиента"')
    def test_open_ingredient_modal_window(self, driver):
        stellar_burgers_main_page = StellarBurgersMainPage(driver)
        stellar_burgers_main_page.click_on_bun_ingredient()
        assert stellar_burgers_main_page.check_ingredient_modal_window_is_opened()

    @allure.title('Проверка основного функционала. Проверка закрытия окна "Детали ингредиента" по крестику')
    def test_close_ingredient_modal_window(self, driver):
        stellar_burgers_main_page = StellarBurgersMainPage(driver)
        stellar_burgers_main_page.click_on_bun_ingredient()
        stellar_burgers_main_page.close_opened_ingredient_modal_window()
        assert stellar_burgers_main_page.check_ingredient_modal_window_is_closed()

    @allure.title('Проверка основного функционала. Проверка увеличения счётчика ингрдиента')
    def test_ingredient_counter(self, driver):
        stellar_burgers_main_page = StellarBurgersMainPage(driver)
        stellar_burgers_main_page.add_bun_ingredient_to_order()
        assert stellar_burgers_main_page.check_ingredient_counter() == 2

    @allure.title('Проверка основного функционала. Проверка возможности оформления заказа залогиненным пользователем')
    def test_create_order_with_authorized_user(self, get_user_name_email_password, login):
        user_data = get_user_name_email_password
        stellar_burgers_main_page = login(user_data['email'], user_data['password'])
        stellar_burgers_main_page.click_on_create_order_button()
        assert stellar_burgers_main_page.check_order_created()
