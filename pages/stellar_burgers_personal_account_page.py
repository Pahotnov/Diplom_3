import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class StellarBurgersPersonalAccountPage(BasePage):
    profile_button = (By.CSS_SELECTOR, 'a[href="/account/profile"]')
    orders_history_link = (By.CSS_SELECTOR, 'a[href*="account/order-history"]')
    exit_button_link = (By.XPATH, '//button[text()="Выход"]')
    order_id = (By.XPATH, '(//div[contains(@class, "OrderHistory")]/p)[1]')

    @allure.step('Клик на кнопку "Профиль"')
    def click_on_profile_button(self):
        self.click_on(self.profile_button)

    @allure.step('Клик на кнопку "История заказов"')
    def click_on_orders_history_button(self):
        self.click_on(self.orders_history_link)

    @allure.step('Клик на кнопку "Выход"')
    def click_on_exit_button(self):
        from .stellar_burgers_login_page import StellarBurgersLoginPage
        self.click_on(self.exit_button_link)
        return StellarBurgersLoginPage(self.driver)

    @allure.step('Получить номер заказа')
    def get_order_id(self):
        return self.get_element_text(self.order_id)
