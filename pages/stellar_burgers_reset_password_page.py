import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class StellarBurgersResetPasswordPage(BasePage):
    password_input_field = (By.CSS_SELECTOR, 'div[class*="input_type_password"]')
    show_or_hide_password_button = (By.CSS_SELECTOR, 'div[class*="icon-action"]')
    active_password_input_field = (By.CSS_SELECTOR, 'div[class*="input_status_active"]')

    @allure.step('Заполнить поле "Пароль"')
    def fill_password_input_field(self, password):
        self.fill_field(self.password_input_field, password)

    @allure.step('Клик на "Показать/скрыть пароль"')
    def click_on_show_or_hide_button(self):
        self.click_on(self.show_or_hide_password_button)

    @allure.step('Проверка активности поля "Пароль"')
    def check_password_field_is_active(self):
        return self.find_element(self.active_password_input_field)
