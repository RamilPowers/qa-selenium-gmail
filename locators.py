from selenium.webdriver.common.by import By


class LoginLocators:
    LOCATOR_LOGIN_FIELD = (By.ID, 'identifierId')
    LOCATOR_LOGIN_NEXT_BUTTON = (By.ID, 'identifierNext')
    LOCATOR_PASSWORD_FIELD = (By.NAME, 'password')
    LOCATOR_PASSWORD_NEXT_BUTTON = (By.ID, 'passwordNext')


class EmailLocators:
    LOCATOR_SEARCH_EMAIL = (By.NAME, 'farit.valiahmetov')
    LOCATOR_WRITE_EMAIL_BUTTON = (By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div')
    LOCATOR_EMAIL_TO_FIELD = (By.NAME, 'to')
    LOCATOR_EMAIL_SUBJECT_FIELD = (By.NAME, 'subjectbox')
    LOCATOR_EMAIL_BODY_FIELD = (By.XPATH, '//*[@role="textbox"]')
    LOCATOR_SEND_EMAIL_BUTTON = (By.XPATH, '//*[@role="button" and contains(text(), "Отправить")]')