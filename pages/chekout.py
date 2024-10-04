import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from utilities.logger import BaseClass


class Checkout(BaseClass):
    login_button = (By.XPATH, "//span[normalize-space()='Login']")
    username = (By.XPATH, "//input[@id='email']")
    pas = (By.XPATH, "//input[@id='password']")
    rem_me = (By.XPATH, "//label[@class='form-check-label']")
    log_submit = (By.XPATH, "//button[@name = 'login']")

    shop_button = (By.XPATH, "//a[@id='6']")
    php_debugger = (By.XPATH, "//a[@class='phpdebugbar-close-btn']")
    shop_all = (By.XPATH, "//span[contains(.,'Shop All Products (Click here)')]")
    foam_gun = (By.XPATH, "//a[.='Foam Guns']")
    foam_product = (By.XPATH, "//a[normalize-space()='Carlisle ST1 Air Purge D-02 Spray Gun']")
    avatar_close = (By.XPATH, "//*[name()='svg']")
    add_cart_button = (By.XPATH, "//button[@class='product_details_main_cart_btn btn-fill-out btn-addtocart']")

    cleaning_solvent = (By.XPATH, "//a[.='Cleaning Solvents']")
    cleaning_product = (By.XPATH, "//a[normalize-space()='Dynasolve CU-6 1g']")
    proceed_checkout = (By.XPATH, "//a[@class='btn btn-fill-out btn-proceed']")
    billing_address = (By.XPATH, "//label[@for='1228']")
    pickup_address = (By.XPATH, "//input[@name='shipping_method_sp']")
    business_name_close = (By.XPATH, "//input[@type='search']")
    business_name = (By.XPATH, "//input[@id='business_name']")
    shipping_method = (By.XPATH, "//input[@name='shipping_method_ups'][1]")
    pay_cc = (By.XPATH, "//span[@id='pnc']")
    num_frame = (By.XPATH, "//iframe[@title='Secure card number input frame']")
    cc_number = (By.XPATH, "//input[@data-elements-stable-field-name='cardNumber']")
    exp_frame = (By.XPATH, "//iframe[@title='Secure expiration date input frame']")
    cc_expiry = (By.XPATH, "//input[@data-elements-stable-field-name='cardExpiry']")
    cvc_frame = (By.XPATH, "//iframe[@title='Secure CVC input frame']")
    cc_cvc = (By.XPATH, "//input[@data-elements-stable-field-name='cardCvc']")
    save_future = (By.XPATH, "//input[@id='remembercc']")
    pay_now = (By.XPATH, "//button[@id='pay_using_new_card']")

    brand_drop = (By.ID, 'profoambrand')
    ncfi_item = (By.XPATH, "//a[normalize-space() = 'NCFI 2.0# HFO Closed Cell Fast Foam']")

    accufoam_product = (By.XPATH, "//a[normalize-space()='Accufoam 1.7# HFC Closed Cell Foam']")
    accufoam_cart_button = (By.XPATH, "//button[@class='product_details_main_cart_btn btn-fill-out btn-addtocart']")
    accufoam_residential = (By.XPATH, "//input[@value='residential']")
    accufoam_lift = (By.XPATH, "//input[@id='lgd_yes']")
    accufoam_shipcharge = (
        By.XPATH, "//input[@value='SOUTHEASTERN FREIGHT LINES, INC. (Logistics Fox, Inc (TSM)) - 338.38']")

    ship_daddress = (By.XPATH, "//label[@class='form-check-label label_info']")
    ship_fname = (By.XPATH, "//input[@name='different_shipping_fname']")
    ship_lname = (By.XPATH, "//input[@name='different_shipping_lname']")
    ship_add1 = (By.XPATH, "//input[@id='different_shipping_address']")
    ship_add2 = (By.XPATH, "//input[@id='different_shipping_address2']")
    ship_city = (By.XPATH, "//input[@id='different_shipping_city']")
    ship_zip = (By.XPATH, "//input[@id='different_shipping_zipcode']")

    #////////////////////////
    # Negative test case
    select_ups = (By.XPATH, "//span[text()='Please select a ups shipping charge.']")

    # available coupon button
    coupon = (By.XPATH, "//a[@id='checkout-view-member-coupons']")
    save99 = (By.XPATH, "//button[@data-coupon_code='save99']")
    coupon_message = (By.XPATH, "//td[.='Coupon code is applied successfully']")

    #/////////////////////////
    #Document test case variables
    doc = (By.XPATH, "//a[@href='/documents']")
    graco_fusion = (By.XPATH, "//a[text()='Graco Fusion ProConnect Gun Exploded Parts Diagram']")
    input_search = (By.XPATH, "//input[@name='keyword']")
    search_button = (By.XPATH, "//button[text()='Search']")
    download = (By.XPATH, "//a[text()='Download']")
    send_doc = (By.XPATH, "//a[text()='Send Document']")

    #////////////////////////////////////////////////////////////////
    #Tag DropDown
    tag = (By.XPATH, "//select[@id='sel_tag']")
    docaccufoam = (By.XPATH, "//a[text()='Accufoam Closed Cell High Yield Foam Product Sheet']")

    #////////////////////////
    #Send Document opens a popup

    docname = (By.XPATH, "//input[@name='name']")
    docemail = (By.XPATH, "//input[@name='email']")
    docmobile = (By.XPATH, "//input[@name='mobile_number']")
    docSendMail = (By.XPATH, "//label[@for='to_email']")
    docSendbutton = (By.XPATH, "//button[@id='document_send']")

    def __init__(self, driver):
        self.driver = driver

    def shop_icon(self):
        return self.driver.find_element(*Checkout.shop_button).click()

    def php(self):
        return self.driver.find_element(*Checkout.php_debugger).click()

    def shop_all_link(self):
        # shop_all_element = self.driver.find_element(By.XPATH, "(//span[normalize-space()='Shop All Products (Click here)'])")
        # self.driver.execute_script("arguments[0].scrollIntoView();", shop_all_element)
        # shop_all_element.click()
        self.driver.execute_script("window.scrollBy(0, 850);")
        return self.driver.find_element(*Checkout.shop_all).click()

    def new_window(self):
        window_handles = self.driver.window_handles
        # Switch to the new window (the last one in the list)
        return self.driver.switch_to.window(window_handles[-1])

    def foam_guns(self):
        return self.driver.find_element(*Checkout.foam_gun).click()

    def foam_gun_product(self):
        return self.driver.find_element(*Checkout.foam_product).click()

    def shadow_close(self):
        shadow_host = self.driver.find_element(By.CSS_SELECTOR, "chat-widget[location-id='ezamnLIXmzsU7b44Ya21']")
        shadow_root = shadow_host.shadow_root  # Access the shadow root directly
        close_button = shadow_root.find_element(By.CSS_SELECTOR, "button.lc_text-widget_prompt--prompt-close")
        close_button.click()
        return

    def cart_add_button(self):
        return self.driver.find_element(*Checkout.add_cart_button).click()

    def cleaning_solvent_option(self):
        return self.driver.find_element(*Checkout.cleaning_solvent).click()

    def cleaning_solvents(self):
        return self.driver.find_element(*Checkout.cleaning_product).click()

    def add_cart_liquid(self):
        return self.driver.find_element(*Checkout.add_cart_button).click()

    def proceed_button(self):
        buttons = self.driver.find_elements(*Checkout.proceed_checkout)
        for button in buttons:
            button.click()
            break
        return
        # return self.driver.find_element(*Checkout.proceed_checkout).click()

    def ship_billing_select(self):
        return self.driver.find_element(*Checkout.billing_address).click()

    def pickup_address_select(self):
        self.driver.execute_script("window.scroll(0,600);")
        # return self.driver.find_element(*Checkout.pickup_address).click()
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='shipping_method_sp']"))
        ).click()
        return

    # Business method for SI and Liquid
    def business(self):
        self.driver.find_element(*Checkout.business_name_close).click()
        return self.driver.find_element(*Checkout.business_name).send_keys("SILIQUID")

    def shipping_method_select(self):
        return self.driver.find_element(*Checkout.shipping_method).click()

    def pay_creditcard(self):
        wait = WebDriverWait(self.driver, 10)  # Adjust timeout as necessary
        pay_button = wait.until(EC.element_to_be_clickable(Checkout.pay_cc))  # Corrected line
        pay_button.click()
        # return self.driver.find_element(*Checkout.pay_cc).click()

    def cc_number_input(self):
        cc_iframe = self.driver.find_element(*Checkout.num_frame)
        self.driver.switch_to.frame(cc_iframe)
        self.driver.find_element(By.XPATH, "//input[@data-elements-stable-field-name='cardNumber']").send_keys(
            "4242424242424242")
        self.driver.switch_to.default_content()
        time.sleep(3)
        return

    def cc_expiry_input(self):
        cc_iframe = self.driver.find_element(*Checkout.exp_frame)
        self.driver.switch_to.frame(cc_iframe)
        self.driver.find_element(By.XPATH, "//input[@data-elements-stable-field-name='cardExpiry']").send_keys("04/28")
        self.driver.switch_to.default_content()
        return

    def cc_cvc_input(self):
        cc_iframe = self.driver.find_element(*Checkout.cvc_frame)
        self.driver.switch_to.frame(cc_iframe)
        self.driver.find_element(By.XPATH, "//input[@data-elements-stable-field-name='cardCvc']").send_keys("123")
        self.driver.switch_to.default_content()
        return

    def save_button(self):
        time.sleep(20)
        return self.driver.find_element(*Checkout.save_future).click()

    def pay_button(self):
        self.driver.find_element(*Checkout.pay_now).click()
        expected_message = "Thank you for your order! Your order is being processed and will be completed within 3-6 hours. You will receive an email confirmation when your order is completed."

        return

    def brand_dropdown(self):
        dropdown_options = self.driver.find_elements(By.TAG_NAME, value="Option")
        for option in dropdown_options:
            if option.text == 'NCFI':
                print(option.text)
                option.click()
                break
        time.sleep(4)
        return

    def ncfi_items_select(self):
        return self.driver.find_element(*Checkout.ncfi_item).click()

    def add_cart_ncfi(self):
        return self.driver.find_element(*Checkout.add_cart_button).click()

    def business_NSL(self):
        self.driver.find_element(*Checkout.business_name_close).click()
        return self.driver.find_element(*Checkout.business_name).send_keys("NSL")

    def accufoam_select(self):
        return self.driver.find_element(*Checkout.accufoam_product).click()

    def add_cart_accufoam(self):
        return self.driver.find_element(*Checkout.accufoam_cart_button).click()

    def accufoam_all_extras(self):
        self.driver.find_element(*Checkout.accufoam_residential).click()
        self.driver.find_element(*Checkout.accufoam_lift).click()
        self.driver.find_element(*Checkout.accufoam_shipcharge).click()
        return

    def diff_address(self):
        return self.driver.find_element(*Checkout.ship_daddress).click()

    def ship_fname_input(self):
        return self.driver.find_element(*Checkout.ship_fname).send_keys("John")

    def ship_lname_input(self):
        return self.driver.find_element(*Checkout.ship_lname).send_keys("Doe")

    def ship_country(self):
        dropdown_options = self.driver.find_elements(By.TAG_NAME, value="Option")
        for option in dropdown_options:
            if option.text == 'United States':
                print(option.text)
                option.click()
                break
        time.sleep(2)
        return

    def ship_province(self):
        dropdown_options = self.driver.find_elements(By.TAG_NAME, value="Option")
        for option in dropdown_options:
            if option.text == 'Maryland':
                print(option.text)
                option.click()
                break
        time.sleep(2)
        return

    def ship_add_1(self):
        return self.driver.find_element(*Checkout.ship_add1).send_keys("123 Main St")

    def ship_add_2(self):
        return self.driver.find_element(*Checkout.ship_add2).send_keys("Apt 4B")

    def ship_city_input(self):
        return self.driver.find_element(*Checkout.ship_city).send_keys("Baltimore")

    def ship_zip_input(self):
        return self.driver.find_element(*Checkout.ship_zip).send_keys("21224")

    def Npay_now(self):
        expected = "Please select a ups shipping charge."
        actual = self.driver.find_element(*Checkout.select_ups).text
        assert expected == actual, f"Expected: {expected}, Actual: {actual}"
        return

    def pay_button_negative(self):
        self.driver.find_element(*Checkout.pay_cc).click()
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='pay_using_new_card']"))
        )
        element.click()
        return

    def coupon_button(self):
        self.driver.find_element(*Checkout.coupon).click()
        logger = self.test_logger()
        logger.info("Clicked on coupon button Successfully")

    # //button[@data-coupon_code='save99']

    def save99_coupon(self):

        self.driver.find_element(By.XPATH, "//a[text()='Available Coupons']").click()
        self.driver.find_element(By.XPATH, "//button[@data-coupon_code='save99']").click()
        time.sleep(10)

        logger = self.test_logger()
        #
        # # Enter the coupon code into the input field
        # self.driver.find_element(By.XPATH, "//input[@id='coupon_code']").send_keys("save99")
        # logger.info("Entered coupon code: save99")
        #
        # # Click the 'Apply Coupon' button
        # self.driver.find_element(By.XPATH, "//button[@id='order_review_apply_coupon']").click()
        # logger.info("Clicked on 'Apply Coupon' button")
        #
        # Handle the alert
        time.sleep(3)
        try:
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            logger.info(f"Alert says: {alert_text}")
            alert.accept()
            logger.info("Alert accepted")
        except TimeoutException:
            logger.error("No alert appeared after applying the coupon")
            return

        # Validate the success message
        # expected_message = "Coupon code is applied successfully"
        # actual_message = self.driver.find_element(*Checkout.coupon_message).text
        # assert expected_message == actual_message, f"Expected: {expected_message}, Actual: {actual_message}"
        logger.info("Coupon applied successfully")
        self.driver.switch_to.default_content()
        return

    def document_link(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self.driver.find_element(*Checkout.doc).click()

    def gracoFusion(self):
        self.driver.execute_script("window.scrollTo(0,350);")
        return self.driver.find_element(*Checkout.graco_fusion).click()

    def searchInput(self):
        self.driver.execute_script("window.scrollTo(0,300);")
        return self.driver.find_element(*Checkout.input_search).send_keys("Graco Fusion")

    def SearchButton(self):
        searches = self.driver.find_elements(*Checkout.search_button)
        for search in searches:
            search.click()
            break

    def downloadButton(self):
        return self.driver.find_element(*Checkout.download).click()

    def sendDocButton(self):
        return self.driver.find_element(*Checkout.send_doc).click()

    def sendName(self):
        return self.driver.find_element(*Checkout.docname).send_keys("John Doe")

    def sendEmail(self):
        return self.driver.find_element(*Checkout.docemail).send_keys("john.doe@example.com")

    def sendMobile(self):
        return self.driver.find_element(*Checkout.docmobile).send_keys("5615557689")

    def DocSendEmail(self):
        return self.driver.find_element(*Checkout.docSendMail).click()

    def SendButton(self):
        return self.driver.find_element(*Checkout.docSendbutton).click()

    def Tag(self):
        self.driver.execute_script("window.scrollTo(0,300);")
        dropdown_options = self.driver.find_elements(By.TAG_NAME, value="Option")
        for option in dropdown_options:
            if option.text == 'Accufoam':
                print(option.text)
                option.click()
                break
        time.sleep(2)

    def Document_Accufoam(self):
        self.driver.execute_script("window.scrollTo(0,300);")
        return self.driver.find_element(*Checkout.docaccufoam).click()
