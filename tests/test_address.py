import time

from pages.address import Address
from pages.chekout import Checkout
from utilities.logger import BaseClass



class Test_create_address(BaseClass):
    def test_create_address(self, setup):
        logger = self.test_logger()

        address = Address(self.driver)
        checkout = Checkout(self.driver)


        # profile icon
        address.profile_icon()

        # Click on My address
        address.my_address_tab()

        #remove php debugger
        checkout.php()

        #Remove all previous addresses skip if none found
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

        time.sleep(20)

        # Click on Create Button
        address.create_submit_button()

        # delete the new address
        # address.address_delete()





