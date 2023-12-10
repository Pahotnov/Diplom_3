import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.additional_locators import AdditionalLocators
from pages.base_page import BasePage
from selenium.webdriver import ActionChains


class StellarBurgersMainPage(BasePage):
    constructor_button = (By.XPATH, '//p[contains(text(), "Конструктор")]/parent::a')
    list_of_orders_button = (By.XPATH, '//p[contains(text(), "Лента Заказов")]/parent::a')
    personal_account_button = (By.XPATH, '//p[contains(text(), "Личный Кабинет")]/parent::a')
    active_constructor_button = (By.XPATH, '//p[contains(text(), "Конструктор")]/parent::a[contains(@class, "link_active")]')
    burger_ingredients_section = (By.CSS_SELECTOR, 'section[class*="BurgerIngredients"]')
    burger_constructor_section = (By.CSS_SELECTOR, 'section[class*="BurgerConstructor"]')
    create_order_button = (By.XPATH, './/button[text()="Оформить заказ"]')
    active_list_of_orders_button = (By.XPATH, '//p[contains(text(), "Лента Заказов")]/parent::a[contains(@class, "link_active")]')
    list_of_orders_section = (By.XPATH, '(//div[contains(@class,"OrderFeed")])[1]')
    bun_ingredient = (By.XPATH, '//img[contains(@alt, "Краторная булка N-200i")]/parent::a')
    bun_ingredient_counter = (By.XPATH, '//img[contains(@alt, "Краторная булка")]/parent::a/div/p')
    opened_ingredient_modal_window = (By.CSS_SELECTOR, 'section[class*="Modal_modal_opened"]')
    close_ingredient_modal_window_button = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//button')
    success_create_order_modal_window = (By.XPATH, '//p[text()="идентификатор заказа"]/parent::div')
    close_success_create_order_modal_window_button = (By.XPATH, '//p[text()="идентификатор заказа"]/following::button')
    order_id = (By.XPATH, '//p[text()="идентификатор заказа"]/parent::div/h2')

    @allure.step('Клик на кнопку "Личный Кабинет')
    def click_on_personal_account_button(self):
        self.click_on(self.personal_account_button)

    @allure.step('Перейти в раздел "Конструктор"')
    def go_to_constructor(self):
        self.click_on(self.constructor_button)

    @allure.step('Перейти в раздел "Лента Заказов"')
    def go_to_list_of_orders(self):
        self.click_on(self.list_of_orders_button)

    @allure.step('Проверка активности раздела "Конструктор"')
    def check_constructor_button_is_active(self):
        return self.find_element(self.active_constructor_button)

    @allure.step('Проверить наличие секции "Соберите бургер" на странице')
    def check_burger_ingredients_section_on_page(self):
        return self.find_element(self.burger_ingredients_section)

    @allure.step('Проверить наличие секции создания бургера')
    def check_burger_constructor_section_on_page(self):
        return self.find_element(self.burger_constructor_section)

    @allure.step('Проверка активности раздела "Лента Заказов"')
    def check_list_of_orders_button_is_active(self):
        return self.find_element(self.active_list_of_orders_button)

    @allure.step('Проверить, что раздел "Конструктор" активен')
    def check_list_of_orders_section_on_page(self):
        return self.find_element(self.list_of_orders_section)

    @allure.step('Клик на ингредиент')
    def click_on_bun_ingredient(self):
        self.click_on(self.bun_ingredient)

    @allure.step('Проверка появления модального окна "Детали ингредиента"')
    def check_ingredient_modal_window_is_opened(self):
        return self.find_element(self.opened_ingredient_modal_window)

    @allure.step('Закрыть модальное окно "Детали ингредиента"')
    def close_opened_ingredient_modal_window(self):
        self.click_on(self.close_ingredient_modal_window_button)

    @allure.step('Проверить отсутствие модального окна "Детали ингредиента"')
    def check_ingredient_modal_window_is_closed(self):
        return self.check_element_is_invisible(self.opened_ingredient_modal_window)

    @allure.step('Получить значение счётчика ингредиента')
    def check_ingredient_counter(self):
        return int(self.find_element(self.bun_ingredient_counter).text)

    # В Firefox эта функция упорно не хочет добавлять ингредиент в заказ
    # В Chrome работает
    @allure.step('Добавить булки в конструктор')
    def add_bun_ingredient_to_order(self):
        element = self.find_element(self.bun_ingredient)
        target = self.find_element(self.burger_constructor_section)

        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    @allure.step('Клик на кнопку "Оформить заказ"')
    def click_on_create_order_button(self):
        self.click_on(self.create_order_button)

    @allure.step('Проверка создания заказа')
    def check_order_created(self):
        return self.find_element(self.success_create_order_modal_window)

    @allure.step('Закрыть модальное окно оформления заказа')
    def close_success_create_order_modal_window(self):
        self.click_on(self.close_success_create_order_modal_window_button)

    @allure.step('Получить номер заказа')
    def get_order_id(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located(AdditionalLocators.order_id_9999))
        return int(self.find_element(self.order_id).text)
