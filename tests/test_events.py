import time

from selenium.webdriver.common.by import By

from pages.address import Address
from pages.chekout import Checkout
from pages.events import Events, event_doc
from utilities.logger import BaseClass


class Test_events(BaseClass):
    def test_events(self, setup):
        logger = self.test_logger()

        #create object of Checkout page
        checkout = Checkout(self.driver)

        #Create object of Events page
        events = Events(self.driver)

        address = Address(self.driver)

        # profile icon
        address.profile_icon()

        # Click on My address
        address.my_address_tab()

        # remove php debugger
        checkout.php()

        # Remove all previous addresses skip if none found
        address.address_deletion()

        # Click on create new address
        address.create_address()

        # New Address details

        # Write address alias
        address.address_alias()

        # Write Address line 1
        address.address_1()

        # Write Address line 2
        address.address_2()

        # Select United States From Country Dropdown
        address.country_dropdown()

        # Select Tennessee from Province Dropdown
        address.province_dropdown()

        # Write city in address
        address.address_city()

        # Enter Zip Code
        address.address_zip()

        # Enter Phone
        address.address_phone()

        # time.sleep(20)

        # Click on Create Button
        address.create_submit_button()

        events.trainingicon()

        checkout.shadow_close()

        events.events_menu()

        events.Assertion()
        logger.info("pagination assertion successful")

        events.buy_ticket()

        events.addParticipant()

        events.pName()
        events.pEmail()
        events.size()
        events.countryDropDown()
        events.pPhone()
        events.pSave()

        # Click on Proceed to checkout
        checkout.proceed_button()
        logger.info("Proceed to checkout clicked successfully")

        # # Select Illinois Billing address
        # checkout.ship_billing_select()
        # logger.info("Illinois Billing address selected successfully")

        # Write the Business Name
        checkout.business()
        logger.info("Business Name entered successfully")

        # select credit card payment method
        checkout.pay_creditcardEvents()
        logger.info("Credit card payment method selected successfully")

        self.driver.find_element(By.XPATH,"//span[@id='pnc']").click()

        # Enter cc number
        checkout.cc_number_input()
        logger.info("Credit card number entered successfully")

        # Enter Expiry Date
        checkout.cc_expiry_input()
        logger.info("Credit card expiry date entered successfully")

        # Enter cvc
        checkout.cc_cvc_input()
        logger.info("Credit card cvc entered successfully")

        # Save future payment
        checkout.save_button()
        logger.info("Future payment saved successfully")

        # Click on pay now button
        checkout.pay_button()
        logger.info("Pay now button clicked successfully")
        logger.info("Order placed successfully")
        time.sleep(30)

    def test_calendar(self):
        self.driver.get("https://staging.profoam.com/profoam-event/profoam-3-12-day-training-class-rutledge-ga/22")
        logger = self.test_logger()

        # create object of Checkout page
        checkout = Checkout(self.driver)

        # Create object of Events page
        events = Events(self.driver)

        events.calendarMenu()

        events.googleOption()
        time.sleep(5)

        events.newWindow()
        time.sleep(10)

    





