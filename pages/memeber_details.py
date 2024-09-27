import time

from selenium.webdriver.common.by import By

from utilities.logger import BaseClass


class Member_details(BaseClass):
    profile = (By.XPATH, "//i[@class='fa fa-user']")
    editprofile = (By.XPATH, "//i[@class='fa fa']")
    # Profile details form
    salutation = (By.XPATH, "//input[@id='salutation_prof']")
    fname = (By.XPATH, "//input[@id='first_name']")
    lname = (By.XPATH, "//input[@id='last_name']")
    email = (By.XPATH, "//input[@id='email']")
    mobile = (By.XPATH, "//input[@id='mobile_number']")
    business = (By.XPATH, "//input[@id='business_name']")
    del_business = (By.XPATH, "//a[@class='close remove-member-business']")
    add1 = (By.XPATH, "//input[@id='address1']")
    add2 = (By.XPATH, "//input[@id='address2']")
    city = (By.XPATH, "//input[@id='city']")
    postal = (By.XPATH, "//input[@id='postal_code']")
    update = (By.XPATH, "//input[@class='btn btn-primary profile-btn']")

    def __init__(self, driver):
        self.driver = driver

    def profile_icon(self):
        return self.driver.find_element(*Member_details.profile).click()

    def edit_profile(self):
        return self.driver.find_element(By.XPATH, "//a[@href='/members/edit/1300']").click()

    def salutation_button(self):
        return self.driver.find_element(*Member_details.salutation).click()

    def first_name(self):
        element = self.driver.find_element(*Member_details.fname)
        element.clear()
        element.send_keys("Shabaz")
        return

    def last_name(self):
        element = self.driver.find_element(*Member_details.lname)
        element.clear()
        element.send_keys("Ahmed")
        return

    def email_address(self):
        element = self.driver.find_element(*Member_details.email)
        element.clear()
        element.send_keys("testsa@yopmail.com")
        return

    def mobile_number(self):
        element = self.driver.find_element(*Member_details.mobile)
        element.clear()
        element.send_keys("7567567566")
        return

    def business_name(self):
        element = self.driver.find_element(*Member_details.business)
        element.clear()
        element.send_keys("Arnvee Agency")
        return

    def delete_businessName(self):
        business_names = self.driver.find_elements(*Member_details.del_business)
        for name in business_names:
            name.click()
            break
        return

    def addressLine1(self):
        element = self.driver.find_element(*Member_details.add1)
        element.clear()
        element.send_keys("5752 Thunder Hill Rd")
        return

    def addressLine2(self):
        element = self.driver.find_element(*Member_details.add2)
        element.clear()
        element.send_keys("Columbia")
        return

    def country_dropdown(self):
        dropdown_options = self.driver.find_elements(By.TAG_NAME, value="Option")
        for option in dropdown_options:
            if option.text == 'United States':
                print(option.text)
                option.click()
                break
        time.sleep(2)
        return

    def province_dropdown(self):
        dropdown_options = self.driver.find_elements(By.TAG_NAME, value="Option")
        for option in dropdown_options:
            if option.text == 'Maryland':
                print(option.text)
                option.click()
                break
        time.sleep(2)
        return

    def city_input(self):
        element = self.driver.find_element(*Member_details.city)
        element.clear()
        element.send_keys("Columbia")
        return

    def postal_code(self):
        element = self.driver.find_element(*Member_details.postal)
        element.clear()
        element.send_keys("21045")
        return

    def update_button(self):
        self.driver.execute_script("window.scrollBy(0, 350);")
        return self.driver.find_element(*Member_details.update).click()
