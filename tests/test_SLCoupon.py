from pages.chekout import Checkout
from utilities.logger import BaseClass

class Test_slcoupon(BaseClass):
    def test_sl_coupon(self, setup):
        logger = self.test_logger()
        """
        In this test by checking out SI and Liquid item with save99 coupon code
        """
        slcoupon = Checkout(self.driver)

        # Shop Icon
        slcoupon.shop_icon()
        logger.info("Shop Icon clicked successfully")

        # PHP Debugger
        slcoupon.php()

        # Shop All Link
        slcoupon.shop_all_link()
        logger.info("Shop All link clicked successfully")

        # Switch to Category all
        slcoupon.new_window()
        logger.info("Switched to Category all successfully")

        # Foam Guns
        slcoupon.foam_guns()
        logger.info("Foam Guns from side menu clicked successfully")

        # Selecting Carlisle ST1 Air Purge D-02 Spray Gun
        slcoupon.foam_gun_product()
        logger.info("Carlisle ST1 Air Purge D-02 Spray Gun selected successfully")

        # Add Spray Gun to cart
        slcoupon.shadow_close()
        slcoupon.cart_add_button()
        logger.info("Carlisle ST1 Air Purge D-02 Spray Gun added to cart successfully")

        # # Click on shop button for liquid items
        # slcoupon.shop_icon()
        # logger.info("Shop Icon clicked successfully for liquid items")
        #
        # # Click on shop all link for liquid items
        # slcoupon.shop_all_link()
        # logger.info("Shop All link clicked successfully for liquid items")
        #
        # # Again handle new Window
        # slcoupon.new_window()
        # logger.info("Switched to Category all for liquid items successfully")
        #
        # # Click on Cleaning solvent
        # slcoupon.cleaning_solvent_option()
        # logger.info("Cleaning solvent option clicked successfully")
        #
        # # Click on cleaning solvent product
        # slcoupon.cleaning_solvents()
        # logger.info("Cleaning solvent product selected successfully")
        #
        # # Click on add to cart button for liquid product
        # slcoupon.add_cart_liquid()
        # logger.info("Cleaning solvent added to cart successfully")

        # Click on Proceed to checkout
        slcoupon.proceed_button()
        logger.info("Proceed to checkout clicked successfully")

        # Select Illinois Billing address
        slcoupon.ship_billing_select()
        logger.info("Illinois Billing address selected successfully")

        # Select Pickup address
        slcoupon.pickup_address_select()
        logger.info("Pickup address selected successfully")

        # Write the Business Name
        slcoupon.business()
        logger.info("Business Name entered successfully")



        # Select 1st Shipping method
        # checkout.shipping_method_select()


        # Click on available coupons
        slcoupon.save99_coupon()


        # select credit card payment method
        slcoupon.pay_creditcard()
        logger.info("Credit card payment method selected successfully")

        # Enter cc number
        slcoupon.cc_number_input()
        logger.info("Credit card number entered successfully")

        # Enter Expiry Date
        slcoupon.cc_expiry_input()
        logger.info("Credit card expiry date entered successfully")

        # Enter cvc
        slcoupon.cc_cvc_input()
        logger.info("Credit card cvc entered successfully")

        # Save future payment
        slcoupon.save_button()
        logger.info("Future payment saved successfully")

        # Click on pay now button
        slcoupon.pay_button()
        logger.info("Pay now button clicked successfully")
        logger.info("Order placed successfully with save99 coupon code")


