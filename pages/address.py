import time

from selenium.webdriver.common.by import By

from utilities.logger import BaseClass
from utilities.addressGenerator import AddressGenerator


class Address(BaseClass):

    #address generator object
    gen = AddressGenerator()

    profile= (By.XPATH,"//i[@class='fa fa-user']")
    my_address= (By.XPATH,"//a[@aria-controls='address']")
    create = (By.XPATH,"//a[@class='btn btn-danger']")

    # Address details:
    alias = (By.XPATH,"//input[@id='alias']")
    add_1 = (By.XPATH,"//input[@id='address_1']")
    add_2 = (By.XPATH,"//input[@id='address_2']")
    add_city = (By.XPATH,"//input[@id='city']")
    add_zip = (By.XPATH,"//input[@id='zip']")
    add_phone = (By.XPATH,"//input[@id='phone']")
    create_submit = (By.XPATH,"//button[@class='btn btn-primary']")

    # Delete an address
    Addresses = (By.XPATH,"//a[@class= 'btn btn-border-fill btn-danger border-2 btn-xs rounded-0']")

    # delete any previous addresses
    address =(By.XPATH,"//a[@class='btn btn-border-fill btn-danger border-2 btn-xs rounded-0']")

    def __init__(self, driver):
        self.driver = driver

    def profile_icon(self):
        return self.driver.find_element(*Address.profile).click()

    def my_address_tab(self):
        self.driver.execute_script("window.scrollBy(0, 200);")
        return self.driver.find_element(*Address.my_address).click()

    def create_address(self):
        return self.driver.find_element(*Address.create).click()

    def address_alias(self):
        alias_value = self.gen.generate_address()["alias"]
        return self.driver.find_element(*Address.alias).send_keys(alias_value)

    def address_1(self):
        address_1 = self.gen.generate_address()["address_line_1"]
        return self.driver.find_element(*Address.add_1).send_keys(address_1)



    def address_2(self):
        address_2 = self.gen.generate_address()["address_line_2"]
        return self.driver.find_element(*Address.add_2).send_keys(address_2)

    def country_dropdown(self):
        dropdown_options = self.driver.find_elements(By.TAG_NAME, value = "Option")
        for option in dropdown_options:
            if option.text == 'United States':
                print(option.text)
                option.click()
                break
        time.sleep(2)
        return

    def province_dropdown(self):
        province = self.gen.generate_address()["province"]
        dropdown_options = self.driver.find_elements(By.TAG_NAME, value = "Option")
        for option in dropdown_options:
            if option.text == province:
                print(option.text)
                option.click()
                break
        time.sleep(2)
        return

    def address_city(self):
        city = self.gen.generate_address()["city"]
        return self.driver.find_element(*Address.add_city).send_keys(city)

    def address_zip(self):
        zip = self.gen.generate_address()["zipcode"]
        return self.driver.find_element(*Address.add_zip).send_keys(zip)


    def address_phone(self):
        phone = self.gen.generate_address()["phone"]
        return self.driver.find_element(*Address.add_phone).send_keys(phone)

    def create_submit_button(self):
        return self.driver.find_element(*Address.create_submit).click()



    # def address_delete(self):
    #     addresses = self.driver.find_elements(*Address.Addresses)
    #     for address in addresses:
    #         print(address.text)
    #
    #     return

    def address_deletion(self):
        try:
            addresses = self.driver.find_elements(*Address.address)

            if not addresses:
                return

            for address in addresses:
                address.click()
                alert = self.driver.switch_to.alert
                alert.accept()
                time.sleep(5)
                alert.accept()
                time.sleep(2)
                self.driver.switch_to.default_content()

        except Exception as e:
            print(f"An error occurred: {e}")
            return

        return