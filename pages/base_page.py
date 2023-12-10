import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from pages.additional_locators import AdditionalLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('Получить ссылку текущей страницы')
    def get_url(self):
        return self.driver.current_url

    # Добавил явное ожидание исчезновения перекрывающей модалки, из-за которой падали тесты в Firefox
    @allure.step('Кликнуть по элементу')
    def click_on(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(AdditionalLocators.modal_overlay))
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
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located(AdditionalLocators.order_id_9999))
        return self.find_element(locator).text
