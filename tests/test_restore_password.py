import allure

from pages.stellar_burgers_login_page import StellarBurgersLoginPage
from pages.stellar_burgers_main_page import StellarBurgersMainPage
from personal_info_data import PersonalInfoData


class TestRestorePassword:

    @allure.title('Восстановление пароля. Проверка восстановления пароля')
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль». '
                        'Ввод почты и клик по кнопке «Восстановить». '
                        'Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_restore_password(self, driver):
        email = PersonalInfoData.EMAIL
        stellar_burgers_main_page = StellarBurgersMainPage(driver)
        stellar_burgers_main_page.click_on_personal_account_button()
        stellar_burgers_main_page.click_on_personal_account_button()
        stellar_burgers_login_page = StellarBurgersLoginPage(driver)
        stellar_burgers_forgot_password_page = stellar_burgers_login_page.click_on_forgot_password_link()
        stellar_burgers_forgot_password_page.fill_email_input_field(email)
        stellar_burgers_reset_password_page = stellar_burgers_forgot_password_page.click_on_restore_button()
        stellar_burgers_reset_password_page.click_on_show_or_hide_button()
        assert stellar_burgers_reset_password_page.check_password_field_is_active()
