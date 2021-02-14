from BaseApp import BasePage
from locators import EmailLocators, LoginLocators
from environment_variables import EMAIL, PSWD


class LoginHelper(BasePage):
    """
    Page Object.

    Login Page.

    """
    def __init__(self, driver):
        super().__init__(driver)
        self.field_locator = LoginLocators.LOCATOR_LOGIN_FIELD
        self.button_locator = LoginLocators.LOCATOR_LOGIN_NEXT_BUTTON
        self.key = EMAIL

    def enter_field(self):
        field = self.find_element(self.field_locator)
        field.send_keys(self.key)
        return field

    def next_button(self):
        return self.find_element(self.button_locator).click()


class PasswordHelper(LoginHelper):
    """
    Page Object.

    Password Page.

    """
    def __init__(self, driver):
        super().__init__(driver)
        self.field_locator = LoginLocators.LOCATOR_PASSWORD_FIELD
        self.button_locator = LoginLocators.LOCATOR_PASSWORD_NEXT_BUTTON
        self.key = PSWD


class EmailWriteHelper(BasePage):
    """
    Page Object.

    Mails Page.

    """
    def __init__(self, driver):
        super().__init__(driver)
        self.email_field = EmailLocators.LOCATOR_SEARCH_EMAIL
        self.write_email_button = EmailLocators.LOCATOR_WRITE_EMAIL_BUTTON
        self.send_button = EmailLocators.LOCATOR_SEND_EMAIL_BUTTON
        self.email_to_field = EmailLocators.LOCATOR_EMAIL_TO_FIELD
        self.subject_field = EmailLocators.LOCATOR_EMAIL_SUBJECT_FIELD
        self.body_field = EmailLocators.LOCATOR_EMAIL_BODY_FIELD

    def search_emails(self):
        emails = self.find_elements(self.email_field, time=20)
        if emails:
            count = len(emails) // 2
            email = emails[0].get_attribute('email')
            return email, count
        return None

    def button_decorator(func):
        def wrapper(self):
            return self.find_element(func(self)).click()
        return wrapper

    def field_decorator(func):
        def wrapper(self, key):
            field = self.find_element(func(self, key)[0])
            field.send_keys(key)
            return field
        return wrapper

    @button_decorator
    def write_email_button_click(self):
        return self.write_email_button

    @button_decorator
    def send_button_click(self):
        return self.send_button

    @field_decorator
    def enter_email_to_field(self, key):
        return self.email_to_field, key

    @field_decorator
    def enter_subject_field(self, key):
        return self.subject_field, key

    @field_decorator
    def enter_body_field(self, key):
        return self.body_field, key








