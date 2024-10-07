import time

from pages.chekout import Checkout
from pages.wishlist import Wishlist, negativewish, negativecart
from utilities.logger import BaseClass


class Test_Wishlist_negative(BaseClass):
    def test_Wishlist_negative(self, setup):
        logger = self.test_logger()

        wish = Wishlist(self.driver)

        checkout = Checkout(self.driver)

        # Click on the profile icon
        wish.profile_icon()

        # click on the WishList option from side menu
        wish.wishlist_option()

        checkout.php()

        wish.negativeWishItems()

        # Select all the products in the page
        wish.selectCheckbox()

        # Click on add to cart button
        wish.addCart()

        # Click on cart icon
        wish.cart_icon()

        # close svg
        checkout.shadow_close()

        wish.negativeCartItems()

        assert negativewish == negativecart

        logger.info("WishList products were added to cart")

        # self.driver.close()

    def test_viewWishList(self, setup):

        self.driver.get("https://staging.profoam.com/")
        logger = self.test_logger()

        wish = Wishlist(self.driver)

        checkout = Checkout(self.driver)

        # Click on the profile icon
        wish.profile_icon()

        # click on the WishList option from side menu
        wish.wishlist_option()

        # checkout.php()
        checkout.shadow_close()

        wish.shareWishlistButton()


        wish.viewWishlistButton()

        time.sleep(5)











