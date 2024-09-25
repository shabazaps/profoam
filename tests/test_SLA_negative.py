import time

from pages.chekout import Checkout
from utilities.logger import BaseClass


class Test_NSL(BaseClass):
    def test_checkout(self, setup):
        logger = self.test_logger()
        # HomePage
        checkout = Checkout(self.driver)

        # Shop Icon
        checkout.shop_icon()

        # PHP Debugger
        checkout.php()

        # Shop All Link
        checkout.shop_all_link()

        # Switch to Category all
        checkout.new_window()

        # Foam Guns
        checkout.foam_guns()

        # Selecting Carlisle ST1 Air Purge D-02 Spray Gun
        checkout.foam_gun_product()

        # Add Spray Gun to cart
        checkout.cart_add_gun()

        # # Click on shop button for liquid items
        # checkout.shop_icon()
        #
        # # Click on shop all link for liquid items
        # checkout.shop_all_link()
        #
        # # Again handle new Window
        # checkout.new_window()
        #
        # # Click on Cleaning solvent
        # checkout.cleaning_solvent_option()
        #
        # # Click on cleaning solvent product
        # checkout.cleaning_solvents()
        #
        # # Click on add to cart button for liquid product
        # checkout.add_cart_liquid()
        #
        # # Click on shop button for NCFI Items
        # checkout.shop_icon()
        #
        # # Click on shop all link for NCFI items
        # checkout.shop_all_link()
        #
        # # Again handle new Window for NCFI Items
        # checkout.new_window()
        #
        # # Click on NCFI from dropdown menu
        # checkout.brand_dropdown()
        #
        # # Click on a NCFI Item
        # checkout.ncfi_items_select()
        #
        # # Add NCFI item to cart
        # checkout.add_cart_ncfi()
        #
        # Click on Proceed to checkout
        checkout.proceed_button()

        # Select Illinois Billing address
        checkout.ship_billing_select()

        self.driver.execute_script("window.scrollBy(0, 1200);")

        # Click on pay now button without any ship information
        checkout.pay_button_negative()

        # Check assertion
        checkout.Npay_now()
