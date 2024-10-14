import time

from selenium.webdriver.common.by import By

from pages.address import Address
from pages.chekout import Checkout
from pages.events import Events, event_doc
from utilities.logger import BaseClass


class Test_events(BaseClass):
    def test_event_unclick(self, setup):
        """
        In this test we will navigate to an event page.
        we will deselect the event and click on buy Ticket
        It will give error "Please select at least one event from the list"
        """
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

        events.uncheckEvent()

        events.buy_ticket()

        time.sleep(2)

        events.assertEvent()

        time.sleep(10)

