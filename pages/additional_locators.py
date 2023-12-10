from selenium.webdriver.common.by import By


class AdditionalLocators:
    modal_overlay = (By.XPATH, '(//div[contains(@class, "Modal_modal_overlay")])[2]')
    order_id_9999 = (By.XPATH, '//h2[text()="9999"]')
