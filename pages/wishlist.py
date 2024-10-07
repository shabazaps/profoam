import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from utilities.logger import BaseClass


negativewish = []
negativecart = []
class Wishlist(BaseClass):

    profile = (By.XPATH,"//i[@class='fa fa-user']")
    wishlist = (By.XPATH,"//a[@aria-controls='member-wishlist']")
    products = (By.XPATH,"//input[@type='checkbox']")
    addcart = (By.XPATH,"//button[@id='add-to-cart-btn']")
    cart = (By.XPATH,"//i[@class='linearicons-cart']")
    wishproceed = (By.XPATH,"//a[@class='btn btn-fill-out btn-proceed']")

    sharewishlist = (By.XPATH,"//button[@id='share-wishlist']")
    viewWishList = (By.XPATH,"//a[@class='btn btn-success btn-sm wishlist-url']")
    sharedwishlist = (By.XPATH,"//p[@class='mt-2']/a")
    delete=(By.XPATH,"//button[@onclick='confirmDeleteWishlist(this);']")



    #negative elements
    wishItems = (By.XPATH,"//tr[td[@class='product-thumbnail'] and td[@class='product-name']]/td[@class='product-name']/a")
    cartItems = (By.XPATH,"//tr[td[@class='product-name']]/td[@class='product-name']/div/a")




    def __init__(self, driver):
        self.driver = driver

    def profile_icon(self):
        return self.driver.find_element(*Wishlist.profile).click()

    def wishlist_option(self):
        self.driver.execute_script("window.scroll(0,100);")
        return self.driver.find_element(*Wishlist.wishlist).click()

    def selectCheckbox(self):
        boxes = self.driver.find_elements(*Wishlist.products)
        for box in boxes:
            self.driver.execute_script("window.scroll(0,200);")
            box.click()
            time.sleep(1)
        return

    def addCart(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.driver.find_element(*Wishlist.addcart).click()
        time.sleep(10)
        return

    def cart_icon(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(Wishlist.cart)
        )
        self.driver.find_element(*Wishlist.cart).click()
        return

    def wishproceedButton(self):
        self.driver.execute_script("window.scroll(0,300);")
        return self.driver.find_element(*Wishlist.wishproceed).click()

    def negativeWishItems(self):
        negativewish = self.driver.find_elements(*Wishlist.wishItems)
        for item in negativewish:
            print(item.text)
        return

    def negativeCartItems(self):
        negativecart = self.driver.find_elements(*Wishlist.cartItems)
        for item in negativecart:
            print(item.text)
        return

    def shareWishlistButton(self):
        return self.driver.find_element(*Wishlist.sharewishlist).click()

    def viewWishlistButton(self):
        return self.driver.find_element(*Wishlist.viewWishList).click()

    def sharedWishlistButton(self):
        return self.driver.find_element(*Wishlist.sharedwishlist).click()

    def deleteWishlistButton(self):
        buttons = self.driver.find_elements(*Wishlist.delete)
        for button in buttons:
            button.click()
        return




