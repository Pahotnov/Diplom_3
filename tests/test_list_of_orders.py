import allure

from pages.stellar_burgers_list_of_orders_page import StellarBurgersListOfOrdersPage
from pages.stellar_burgers_main_page import StellarBurgersMainPage
from pages.stellar_burgers_personal_account_page import StellarBurgersPersonalAccountPage


class TestListOfOrders:

    @allure.title('Раздел "Лента заказов". Проверка открытия модального окно с деталями заказа')
    def test_check_order_details(self, driver, get_user_name_email_password, login):
        user_data = get_user_name_email_password
        stellar_burgers_main_page = login(user_data['email'], user_data['password'])
        stellar_burgers_main_page.go_to_list_of_orders()
        stellar_burgers_list_of_orders_page = StellarBurgersListOfOrdersPage(driver)
        stellar_burgers_list_of_orders_page.open_order_list_details_card()
        assert stellar_burgers_list_of_orders_page.check_order_list_details_card_is_opened()

    @allure.title('Раздел "Лента заказов". Проверка отображения заказов пользователя на странице «Лента заказов» из раздела «История заказов»')
    def test_check_history_of_orders_in_list_of_orders(self, driver, get_user_name_email_password, login):
        user_data = get_user_name_email_password
        stellar_burgers_main_page = login(user_data['email'], user_data['password'])
        stellar_burgers_main_page.add_bun_ingredient_to_order()
        stellar_burgers_main_page.click_on_create_order_button()
        stellar_burgers_main_page.close_opened_ingredient_modal_window()
        stellar_burgers_main_page.click_on_personal_account_button()
        stellar_burgers_personal_account_page = StellarBurgersPersonalAccountPage(driver)
        stellar_burgers_personal_account_page.click_on_orders_history_button()
        order_id = stellar_burgers_personal_account_page.get_order_id()
        stellar_burgers_main_page.go_to_list_of_orders()
        stellar_burgers_list_of_orders_page = StellarBurgersListOfOrdersPage(driver)
        assert stellar_burgers_list_of_orders_page.get_order_id() == order_id

    @allure.title('Раздел "Лента заказов". Проверка увеличения счётчика "Выполнено за всё время" при создании нового заказа')
    def test_check_completed_all_time_counter(self, driver, get_user_name_email_password, login):
        user_data = get_user_name_email_password
        stellar_burgers_main_page = login(user_data['email'], user_data['password'])
        stellar_burgers_main_page.go_to_list_of_orders()
        stellar_burgers_list_of_orders_page = StellarBurgersListOfOrdersPage(driver)
        all_time_counter_value = stellar_burgers_list_of_orders_page.check_completed_all_time_counter()
        stellar_burgers_main_page = StellarBurgersMainPage(driver)
        stellar_burgers_main_page.go_to_constructor()
        stellar_burgers_main_page.add_bun_ingredient_to_order()
        stellar_burgers_main_page.click_on_create_order_button()
        stellar_burgers_main_page.close_opened_ingredient_modal_window()
        stellar_burgers_main_page.go_to_list_of_orders()
        stellar_burgers_list_of_orders_page = StellarBurgersListOfOrdersPage(driver)
        assert stellar_burgers_list_of_orders_page.check_completed_all_time_counter() == (all_time_counter_value + 1)

    @allure.title('Раздел "Лента заказов". Проверка увеличения счётчика "Выполнено за сегодня" при создании нового заказа')
    def test_check_completed_today_counter(self, driver, get_user_name_email_password, login):
        user_data = get_user_name_email_password
        stellar_burgers_main_page = login(user_data['email'], user_data['password'])
        stellar_burgers_main_page.go_to_list_of_orders()
        stellar_burgers_list_of_orders_page = StellarBurgersListOfOrdersPage(driver)
        today_counter_value = stellar_burgers_list_of_orders_page.check_completed_today_counter()
        stellar_burgers_main_page.go_to_constructor()
        stellar_burgers_main_page = StellarBurgersMainPage(driver)
        stellar_burgers_main_page.add_bun_ingredient_to_order()
        stellar_burgers_main_page.click_on_create_order_button()
        stellar_burgers_main_page.close_opened_ingredient_modal_window()
        stellar_burgers_main_page.go_to_list_of_orders()
        stellar_burgers_list_of_orders_page = StellarBurgersListOfOrdersPage(driver)
        assert stellar_burgers_list_of_orders_page.check_completed_today_counter() == today_counter_value + 1

    @allure.title('Раздел "Лента заказов". Проверка появления номера заказа в разделе "В работе"')
    def test_check_order_id_in_work_list(self, driver, get_user_name_email_password, login):
        user_data = get_user_name_email_password
        stellar_burgers_main_page = login(user_data['email'], user_data['password'])
        stellar_burgers_main_page.add_bun_ingredient_to_order()
        stellar_burgers_main_page.click_on_create_order_button()
        order_id = stellar_burgers_main_page.get_order_id()
        stellar_burgers_main_page.close_opened_ingredient_modal_window()
        stellar_burgers_main_page.go_to_list_of_orders()
        stellar_burgers_list_of_orders_page = StellarBurgersListOfOrdersPage(driver)
        assert stellar_burgers_list_of_orders_page.check_order_in_work() == order_id
