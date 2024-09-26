import time

from pages.chekout import Checkout
from utilities.logger import BaseClass


class Test_NSL(BaseClass):
    # def test_si_negative(self, setup):
    #     """
    #     In this test we will select just the billing address, credit card radio button and pay now button
    #     this will trigger an error that please select ups shipping method above credit card option
    #     """
    #     logger = self.test_logger()
    #     # HomePage
    #     checkout = Checkout(self.driver)
    #
    #     # Shop Icon
    #     checkout.shop_icon()
    #
    #     # PHP Debugger
    #     checkout.php()
    #
    #     # Shop All Link
    #     checkout.shop_all_link()
    #
    #     # Switch to Category all
    #     checkout.new_window()
    #
    #     # Foam Guns
    #     checkout.foam_guns()
    #
    #     # Selecting Carlisle ST1 Air Purge D-02 Spray Gun
    #     checkout.foam_gun_product()
    #
    #     # Add Spray Gun to cart
    #     checkout.cart_add_gun()
    #
    #     # # Click on shop button for liquid items
    #     # checkout.shop_icon()
    #     #
    #     # # Click on shop all link for liquid items
    #     # checkout.shop_all_link()
    #     #
    #     # # Again handle new Window
    #     # checkout.new_window()
    #     #
    #     # # Click on Cleaning solvent
    #     # checkout.cleaning_solvent_option()
    #     #
    #     # # Click on cleaning solvent product
    #     # checkout.cleaning_solvents()
    #     #
    #     # # Click on add to cart button for liquid product
    #     # checkout.add_cart_liquid()
    #     #
    #     # # Click on shop button for NCFI Items
    #     # checkout.shop_icon()
    #     #
    #     # # Click on shop all link for NCFI items
    #     # checkout.shop_all_link()
    #     #
    #     # # Again handle new Window for NCFI Items
    #     # checkout.new_window()
    #     #
    #     # # Click on NCFI from dropdown menu
    #     # checkout.brand_dropdown()
    #     #
    #     # # Click on a NCFI Item
    #     # checkout.ncfi_items_select()
    #     #
    #     # # Add NCFI item to cart
    #     # checkout.add_cart_ncfi()
    #     #
    #     # Click on Proceed to checkout
    #     checkout.proceed_button()
    #
    #     # Select Illinois Billing address
    #     checkout.ship_billing_select()
    #
    #     self.driver.execute_script("window.scrollBy(0, 1200);")
    #
    #     # Click on pay now button without any ship information
    #     checkout.pay_button_negative()
    #
    #     # Check assertion
    #     checkout.Npay_now()

    def test_Liquid_negative(self, setup):
        """
                In this test we will not select any billing or shipping info and try to checkout by clicking on pay now button

        """

        logger = self.test_logger()
        # Create Object of Checkout
        liquid = Checkout(self.driver)

        # Shop Icon
        liquid.shop_icon()
        logger.info("Shop Icon clicked successfully")

        # PHP Debugger
        liquid.php()
        logger.info("PHP Debugger clicked successfully")

        # Click on shop button for liquid items
        liquid.shop_icon()
        logger.info("Shop Icon clicked successfully")

        # Click on shop all link for liquid items
        liquid.shop_all_link()
        logger.info("Shop All link clicked successfully")

        # handle new Window
        liquid.new_window()
        logger.info("New window handled ")

        # Click on Cleaning solvent
        liquid.cleaning_solvent_option()
        logger.info("Cleaning solvent option clicked successfully")

        # Click on cleaning solvent product
        liquid.cleaning_solvents()
        logger.info("Cleaning solvent product clicked successfully")

        # Close the Shadow host button
        liquid.shadow_close()
        logger.info("Shadow host button closed successfully")

        # Click on add to cart button for liquid product
        liquid.cart_add_button()
        logger.info("Add to cart button clicked successfully")

        # Click on Proceed to checkout
        liquid.proceed_button()
        logger.info("Proceed to checkout button clicked successfully")

        self.driver.execute_script("window.scrollBy(0, 1200);")

        # Click on pay now button without any billing or ship information
        logger.info("pay now button not visible as no billing info is provided")
        liquid.pay_button_negative()







