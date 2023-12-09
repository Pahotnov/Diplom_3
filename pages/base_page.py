import time
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class BasePage:
    constructor_button = (By.XPATH, '//p[contains(text(), "Конструктор")]/parent::a')
    list_of_orders_button = (By.XPATH, '//p[contains(text(), "Лента Заказов")]/parent::a')
    personal_account_button = (By.XPATH, '//p[contains(text(), "Личный Кабинет")]/parent::a')

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик на кнопку "Личный Кабинет')
    def click_on_personal_account_button(self):
        from pages.stellar_burgers_login_page import StellarBurgersLoginPage
        self.click_on(self.personal_account_button)
        return StellarBurgersLoginPage(self.driver)

    @allure.step('Перейти в раздел "Конструктор"')
    def go_to_constructor(self):
        from pages.stellar_burgers_main_page import StellarBurgersMainPage
        self.click_on(self.constructor_button)
        return StellarBurgersMainPage(self.driver)

    @allure.step('Перейти в раздел "Лента Заказов"')
    def go_to_list_of_orders(self):
        from pages.stellar_burgers_list_of_orders_page import StellarBurgersListOfOrdersPage
        self.click_on(self.list_of_orders_button)
        return StellarBurgersListOfOrdersPage(self.driver)

    @allure.step('Перейти в раздел "Личный Кабинет"')
    def go_to_personal_account(self):
        from pages.stellar_burgers_personal_account_page import StellarBurgersPersonalAccountPage
        self.click_on(self.personal_account_button)
        return StellarBurgersPersonalAccountPage(self.driver)

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('Получить ссылку текущей страницы')
    def get_url(self):
        time.sleep(1)
        return self.driver.current_url

    # Добавил явное ожидание исчезновения перекрывающей модалки, из-за которой падали тесты в Firefox
    @allure.step('Кликнуть по элементу')
    def click_on(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located((By.XPATH, '(//div[contains(@class, "Modal_modal_overlay")])[2]')))
        self.find_element(locator).click()

    @allure.step('Заполнить поле')
    def fill_field(self, locator, data):
        self.find_element(locator).send_keys(data)

    @allure.step('Проверка отсутствия элемента')
    def check_element_is_invisible(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Получить текст элемента')
    def get_element_text(self, locator):
        return self.find_element(locator).text
