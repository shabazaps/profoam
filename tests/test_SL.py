import time

from pages.chekout import Checkout
from utilities.logger import BaseClass
from pages.address import Address


class Test_Checkout(BaseClass):

    def test_checkout(self, setup):
        logger = self.test_logger()


        # HomePage
        checkout = Checkout(self.driver)
        #address Page
        address = Address(self.driver)

        # profile icon
        # address.profile_icon()
        #
        # # Click on My address
        # address.my_address_tab()
        #
        # # remove php debugger
        # checkout.php()
        #
        # # Remove all previous addresses skip if none found
        # address.address_deletion()
        #
        # # Click on create new address
        # address.create_address()
        #
        # # New Address details
        #
        # # Write address alias
        # address.address_alias()
        #
        # # Write Address line 1
        # address.address_1()
        #
        # # Write Address line 2
        # address.address_2()
        #
        # # Select United States From Country Dropdown
        # address.country_dropdown()
        #
        # # Select Tennessee from Province Dropdown
        # address.province_dropdown()
        #
        # # Write city in address
        # address.address_city()
        #
        # # Enter Zip Code
        # address.address_zip()
        #
        # # Enter Phone
        # address.address_phone()
        #
        #
        # # Click on Create Button
        # address.create_submit_button()

        # Shop Icon
        checkout.shop_icon()
        logger.info("Shop Icon clicked successfully")

        # PHP Debugger
        checkout.php()

        # Shop All Link
        checkout.shop_all_link()
        logger.info("Shop All link clicked successfully")

        # Switch to Category all
        checkout.new_window()
        logger.info("Switched to Category all successfully")

        # Foam Guns
        checkout.foam_guns()
        logger.info("Foam Guns from side menu clicked successfully")

        # Selecting Carlisle ST1 Air Purge D-02 Spray Gun
        checkout.foam_gun_product()
        logger.info("Carlisle ST1 Air Purge D-02 Spray Gun selected successfully")

        # Add Spray Gun to cart
        checkout.shadow_close()
        checkout.cart_add_button()
        logger.info("Carlisle ST1 Air Purge D-02 Spray Gun added to cart successfully")

        # # Click on shop button for liquid items
        # checkout.shop_icon()
        # logger.info("Shop Icon clicked successfully for liquid items")
        #
        # # Click on shop all link for liquid items
        # checkout.shop_all_link()
        # logger.info("Shop All link clicked successfully for liquid items")
        #
        # # Again handle new Window
        # checkout.new_window()
        # logger.info("Switched to Category all for liquid items successfully")
        #
        # # Click on Cleaning solvent
        # checkout.cleaning_solvent_option()
        # logger.info("Cleaning solvent option clicked successfully")
        #
        # # Click on cleaning solvent product
        # checkout.cleaning_solvents()
        # logger.info("Cleaning solvent product selected successfully")
        #
        # # Click on add to cart button for liquid product
        # checkout.add_cart_liquid()
        # logger.info("Cleaning solvent added to cart successfully")


        # Click on Proceed to checkout
        checkout.proceed_button()
        logger.info("Proceed to checkout clicked successfully")

        time.sleep(5)
        # Select Billing address
        checkout.ship_billing_select()
        logger.info("Billing address selected successfully")

        # Write the Business Name
        checkout.business()
        logger.info("Business Name entered successfully")

        # Select Pickup address
        checkout.pickup_address_select()
        logger.info("Pickup address selected successfully")



        # Select 1st Shipping method
        # checkout.shipping_method_select()
        time.sleep(5)
        checkout.Total()

        logger.info("Everything amount is displayed Correctly")



        # select credit card payment method
        checkout.pay_creditcard()
        logger.info("Credit card payment method selected successfully")

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
        # checkout.pay_button()
        # logger.info("Pay now button clicked successfully")
        # logger.info("Order placed successfully")
        #
