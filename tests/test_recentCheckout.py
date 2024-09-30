import time

from pages.chekout import Checkout
from pages.memeber_details import Member_details
from pages.chekout import Checkout
from utilities.logger import BaseClass


class Test_recentCheckout(BaseClass):

    def test_checkout(self, setup):
        logger = self.test_logger()

        recent = Member_details(self.driver)
        checkout = Checkout(self.driver)

        # Click on profile icon
        recent.profile_icon()

        # Scroll to Recent items
        self.driver.execute_script("window.scrollBy(0, 350);")

        # Click on My recent items
        recent.recent_purchase()

        # Click on the most recent item ordered
        recent.recent_purchased_items()

        # time.sleep(10)

        checkout.php()

        # Close the Assistant menu(Shadow DOM)
        checkout.shadow_close()

        # Add product to cart
        checkout.cart_add_button()

        # Click on Proceed to checkout
        checkout.proceed_button()

        # Choose Illinois Billing address
        checkout.ship_billing_select()

        #Choose pickup address
        checkout.pickup_address_select()

        # Click on pay credit card option
        checkout.pay_creditcard()

        #Enter CC Number
        checkout.cc_number_input()

        #Enter CC Expiry
        checkout.cc_expiry_input()

        # Enter CC CVV
        checkout.cc_cvc_input()

        # Save future payment
        checkout.save_button()

        # Click on Pay Now button
        checkout.pay_button()

        # Log the test outcome
        logger.info("Checkout test passed")





