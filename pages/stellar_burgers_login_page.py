import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.stellar_burgers_forgot_password_page import StellarBurgersForgotPasswordPage


class StellarBurgersLoginPage(BasePage):
    enter_title = (By.XPATH, '//h2[text()="Вход"]')
    forgot_password_link = (By.CSS_SELECTOR, 'a[href="/forgot-password"]')
    email_input_field = (By.XPATH, './/label[text()="Email"]/following-sibling::input')
    password_input_field = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input')
    sign_in_button = (By.XPATH, './/button[text()="Войти"]')

    @allure.step('Клик на заголовок "Вход"')
    def click_on_enter_title(self):
        self.click_on(self.enter_title)

    @allure.step('Клик на ссылку "Восстановить пароль"')
    def click_on_forgot_password_link(self):
        self.click_on(self.forgot_password_link)
        return StellarBurgersForgotPasswordPage(self.driver)

    @allure.step('Заполнить поле "Email"')
    def fill_email_input_field(self, email):
        self.fill_field(self.email_input_field, email)

    @allure.step('Заполнить поле "Пароль"')
    def fill_password_input_field(self, password):
        self.fill_field(self.password_input_field, password)

    @allure.step('Клик на кнопку "Войти"')
    def click_on_sign_in_button(self):
        self.click_on(self.sign_in_button)
