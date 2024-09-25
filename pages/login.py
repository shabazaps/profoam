from selenium.webdriver.common.by import By


class Login:
    login_button = (By.XPATH, "//span[normalize-space()='Login']")
    username = (By.XPATH, "//input[@id='email']")
    pas = (By.XPATH, "//input[@id='password']")
    rem_me = (By.XPATH, "//label[@class='form-check-label']")
    log_submit = (By.XPATH, "//button[@name = 'login']")

    def __init__(self, driver):
        self.driver = driver

    def home(self):
        return self.driver.find_element(*Login.login_button).click()

    def login(self):
        return self.driver.find_element(*Login.username).send_keys("testsa@yopmail.com")

    #
    def password(self):
        return self.driver.find_element(*Login.pas).send_keys("Mindfire@123")

    def remember(self):
        self.driver.execute_script("window.scrollBy(0, 300);")
        return self.driver.find_element(*Login.rem_me).click()

    def login_submit(self):
        return self.driver.find_element(*Login.log_submit).click()
