from tests.pages.base_page import BasePage
from playwright.sync_api import Page, expect

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # в кострукторе реализуем локаторы класса
        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')
        self.login_button = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_test_id('login-page-registration-link')
        self.wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    # с помошью методов реализуем действия со страницей
    def fill_login_form(self,email: str, password: str):

        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)
        
        self.password_input.fill(password)
        expect(self.email_input).to_have_value(email)

    # наименование метода = действие(заполнение)_контекст(с чем взаимодействием)_объект(кнопка) 
    def click_login_button(self):
        self.login_button.click()

    def click_registration_link(self):
        self.registration_link.click()

    def check_visible_wrong_email_or_password_alert(self):
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text("Wrong email or password")
 