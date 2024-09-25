from pages.chekout import Checkout
from utilities.logger import BaseClass


class Test_Checkout(BaseClass):

    def test_checkout(self, setup):
        logger = self.test_logger()


        # HomePage
        checkout = Checkout(self.driver)

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
        checkout.cart_add_gun()
        logger.info("Carlisle ST1 Air Purge D-02 Spray Gun added to cart successfully")

        # Click on shop button for liquid items
        checkout.shop_icon()
        logger.info("Shop Icon clicked successfully for liquid items")

        # Click on shop all link for liquid items
        checkout.shop_all_link()
        logger.info("Shop All link clicked successfully for liquid items")

        # Again handle new Window
        checkout.new_window()
        logger.info("Switched to Category all for liquid items successfully")

        # Click on Cleaning solvent
        checkout.cleaning_solvent_option()
        logger.info("Cleaning solvent option clicked successfully")

        # Click on cleaning solvent product
        checkout.cleaning_solvents()
        logger.info("Cleaning solvent product selected successfully")

        # Click on add to cart button for liquid product
        checkout.add_cart_liquid()
        logger.info("Cleaning solvent added to cart successfully")


        # Click on Proceed to checkout
        checkout.proceed_button()
        logger.info("Proceed to checkout clicked successfully")

        # Select Illinois Billing address
        checkout.ship_billing_select()
        logger.info("Illinois Billing address selected successfully")

        # Write the Business Name
        checkout.business()
        logger.info("Business Name entered successfully")

        # Select Pickup address
        checkout.pickup_address_select()
        logger.info("Pickup address selected successfully")



        # Select 1st Shipping method
        # checkout.shipping_method_select()

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
        checkout.pay_button()
        logger.info("Pay now button clicked successfully")
        logger.info("Order placed successfully")

