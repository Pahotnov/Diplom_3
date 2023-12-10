import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class StellarBurgersListOfOrdersPage(BasePage):
    order_list_card = (By.XPATH, '(//a[contains(@class, "OrderHistory_link")])[1]')
    opened_order_list_details_card = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]')
    order_id = (By.XPATH, '(//div[contains(@class, "OrderHistory")]/p)[1]')
    completed_all_time_counter = (By.XPATH, '(//p[contains(text(), "Выполнено за все время:")]/following::p)[1]')
    completed_today_counter = (By.XPATH, '(//p[contains(text(), "Выполнено за сегодня:")]/following::p)[1]')
    order_id_in_work_list = (By.XPATH, '(//div[contains(@class, "orderStatusBox")]/ul)[2]/li')

    @allure.step('Открыть модальное окно с деталями заказа')
    def open_order_list_details_card(self):
        self.click_on(self.order_list_card)

    @allure.step('Проверка наличия модального окна с деталями заказа')
    def check_order_list_details_card_is_opened(self):
        return self.find_element(self.opened_order_list_details_card)

    @allure.step('Получить номер заказа')
    def get_order_id(self):
        return self.get_element_text(self.order_id)

    @allure.step('Получить значение счётчика "Выполнено за всё время"')
    def check_completed_all_time_counter(self):
        return int(self.get_element_text(self.completed_all_time_counter))

    @allure.step('Получить значение счётчика "Выполнено за сегодня"')
    def check_completed_today_counter(self):
        return int(self.get_element_text(self.completed_today_counter))

    @allure.step('Проверка наличия номера заказа в разделе "В работе"')
    def check_order_in_work(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.text_to_be_present_in_element(self.order_id_in_work_list, "0"))
        order_id = self.find_element(self.order_id_in_work_list).text
        return int(order_id.replace("", ''))
3