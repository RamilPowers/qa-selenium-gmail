import time
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from GmailPages import LoginHelper, PasswordHelper, EmailWriteHelper
from environment_variables import EMAIL_TEST


@pytest.fixture(scope="session")
def browser():
    # driver = webdriver.Chrome()
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True}
    )
    yield driver
    driver.quit()


@allure.feature('Gmail Test')
@allure.story('Google Authorization')
def test_gmail(browser):
    login_page = LoginHelper(browser)
    login_page.go_to_site()
    login_page.enter_field()
    login_page.next_button()
    with allure.step('Take the screenshot'):
        allure.attach(
            browser.get_screenshot_as_png(),
            name='Log Enter',
            attachment_type=AttachmentType.PNG
        )
    password = PasswordHelper(browser)
    password.enter_field()
    password.next_button()
    with allure.step('Take the screenshot'):
        allure.attach(
            browser.get_screenshot_as_png(),
            name='Password Enter',
            attachment_type=AttachmentType.PNG
        )
    assert "Gmail" in browser.title, f'The real title is: {browser.title}'


@allure.feature('Gmail Test')
@allure.story('Searching for emails and writing the mail')
def test_email(browser):
    email = EmailWriteHelper(browser)
    items = email.search_emails()
    email.write_email_button_click()
    email.enter_email_to_field(items[0])
    # email.enter_email_to_field(EMAIL_TEST)
    email.enter_subject_field('Тестовое задание Садыков')
    email.enter_body_field(f'Поступило писем от вас: {items[1]}')
    with allure.step('Take the screenshot'):
        allure.attach(
            browser.get_screenshot_as_png(),
            name='Mail',
            attachment_type=AttachmentType.PNG
        )
    email.send_button_click()
    time.sleep(5)
    assert items[1] == 2, f'Messages found: {items[1]}'
