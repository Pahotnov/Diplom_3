import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.stellar_burgers_reset_password_page import StellarBurgersResetPasswordPage


class StellarBurgersForgotPasswordPage(BasePage):
    email_input_field = (By.CSS_SELECTOR, 'input[name]')
    restore_button = (By.XPATH, '//button[text()="Восстановить"]')

    @allure.step('Заполнить поле "Email"')
    def fill_email_input_field(self, email):
        self.fill_field(self.email_input_field, email)

    @allure.step('Клик на кнопку "Восстановить"')
    def click_on_restore_button(self):
        self.click_on(self.restore_button)
        return StellarBurgersResetPasswordPage(self.driver)
