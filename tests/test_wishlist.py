import time

from pages.chekout import Checkout
from pages.wishlist import Wishlist
from utilities.logger import BaseClass


class Test_Wishlist(BaseClass):
    def test_wishlist(self, setup):
        logger = self.test_logger()

        wish = Wishlist(self.driver)

        # Create object for checkout page
        checkout = Checkout(self.driver)

        #Click on the profile icon
        wish.profile_icon()

        #click on the WishList option from side menu
        wish.wishlist_option()

        checkout.php()

        # Select all the products in the page
        wish.selectCheckbox()

        #Click on add to cart button
        wish.addCart()

        #Click on cart icon
        wish.cart_icon()


        #close svg
        checkout.shadow_close()


        #Click on proceed to checkout button
        wish.wishproceedButton()

        # Select Illinois Billing address
        checkout.ship_billing_select()


        time.sleep(25)
        # Select Pickup address
        checkout.pickup_address_select()

        # select credit card payment method
        checkout.pay_creditcard()

        # Enter cc number
        checkout.cc_number_input()

        # Enter Expiry Date
        checkout.cc_expiry_input()

        # Enter cvc
        checkout.cc_cvc_input()

        # Save future payment
        checkout.save_button()

        # Click on pay now button
        checkout.pay_button()
