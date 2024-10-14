import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities import logger
from utilities.logger import BaseClass

event_doc = ""


class Events(BaseClass):
    training = (By.XPATH, "//a[@id='3']")
    events = (By.XPATH, "//div[@class='event_box_title']/a")
    page_doc = (By.XPATH, "//h2[@class='blog_title']")
    uncheck = (By.XPATH, "//span[@class='checkmark']")
    eventxt = (By.XPATH, "//div[@id='booking_error']")
    buy = (By.XPATH, "//input[@type='submit']")
    participant = (By.XPATH,"//a[@class='btn btn-fill-out add_dynamic_participant_btn']")
    pname = (By.XPATH,"//input[@id='participant_name_671[0]']")
    pemail = (By.XPATH,"//input[@id='participant_email_671[0]']")
    pphone = (By.XPATH,"//input[@id='phone_671[0]']")
    psave = (By.XPATH,"//a[@class='btn-sm btn-fill-out save_participant_btn']")
    calendar = (By.XPATH,"//a[@class='atcb-link']")
    google = (By.XPATH,"//a[text()='Google Calendar']")
    gInput = (By.XPATH,"//input[@value='Profoam 3 1/2 Day Training Class - Rutledge, GA']")

    def __init__(self, driver):
        self.driver = driver

    def trainingicon(self):
        return self.driver.find_element(*Events.training).click()

    def events_menu(self):
        global event_doc
        items = self.driver.find_elements(*Events.events)
        for item in items:
            event_doc = item.text
            item.click()
            break
        return event_doc

    def Assertion(self):
        global event_doc
        pagination = self.driver.find_element(*Events.page_doc).text
        assert event_doc == pagination

    def uncheckEvent(self):
        self.driver.find_element(*Events.uncheck).click()


    def assertEvent(self):
        expected = "Please select at least one event from the list"

        actual = ""
        items = self.driver.find_elements(*Events.eventxt)
        for item in items:
            actual = item.text
            break
        assert actual == expected
        print("Assertion Successful")
    def buy_ticket(self):
        element = self.driver.find_element(*Events.buy)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("window.scrollBy(0, -200);")
        time.sleep(3)
        element.click()

    def addParticipant(self):
        return self.driver.find_element(*Events.participant).click()

    def pName(self):
        return self.driver.find_element(*Events.pname).send_keys("John Doe")

    def pEmail(self):
        return self.driver.find_element(*Events.pemail).send_keys("john.doe@example.com")

    def size(self):
        dropdown_options = self.driver.find_elements(By.TAG_NAME, value="Option")
        for option in dropdown_options:
            if option.text == 'L':
                print(option.text)
                option.click()
                break
        time.sleep(2)
        return

    def countryDropDown(self):
        dropdown_options = self.driver.find_elements(By.TAG_NAME, value="Option")
        for option in dropdown_options:
            if option.text == 'US (+1)':
                option.click()
                break
        time.sleep(2)
        return

    def pPhone(self):
        return self.driver.find_element(*Events.pphone).send_keys("7183523800")

    def pSave(self):
        return self.driver.find_element(*Events.psave).click()

    def calendarMenu(self):
        return self.driver.find_element(*Events.calendar).click()

    def googleOption(self):
        return self.driver.find_element(*Events.google).click()

    def newWindow(self):
        window_handles = self.driver.window_handles
        return self.driver.switch_to.window(window_handles[-1])
