import time

from pages.chekout import Checkout
from utilities.logger import BaseClass


class Test_Document(BaseClass):

    def test_doc_search(self, setup):
        logger = self.test_logger()

        doc = Checkout(self.driver)

        #Click on the Document link
        doc.document_link()

        #Enter Graco Fusion in search input
        doc.searchInput().send_keys("Graco Fusion")

        #Click on search Button
        doc.SearchButton()
        time.sleep(5)
        # click on the 1st Graco Fusion
        doc.gracoFusion()

        #Click on the download Button
        # doc.downloadButton()

        # Verify the send Document button
        doc.sendDocButton()

        # Form pops up to send Document
        #Enter name
        doc.sendName()

        #Enter email
        doc.sendEmail()

        #Enter Mobile Number
        doc.sendMobile()

        #Click on send Email only
        doc.DocSendEmail()

        #click on the Send Button

        doc.SendButton()
        time.sleep(4)

    def test_doc_tag(self, setup):
        logger = self.test_logger()

        doc = Checkout(self.driver)

        self.driver.get("https://staging.profoam.com/documents/")
        # Click on the Document link
        doc.document_link()

        #Select Accufoam from tag dropdown
        doc.Tag()
        time.sleep(20)

        #Click on Search Button
        doc.SearchButton()

        time.sleep(20)

        #Click on 1st Accufoam document
        doc.Document_Accufoam()

        #Click on Send Document
        doc.sendDocButton()

        #Enter Details
        doc.sendName()
        doc.sendEmail()
        doc.sendMobile()

        #Click on Send Email only
        doc.DocSendEmail()

        #Click on Send Button
        doc.SendButton()
        time.sleep(4)

    def test_Category_Pagination(self, setup):
        logger = self.test_logger()

        page = Checkout(self.driver)

        self.driver.get("https://staging.profoam.com/documents/")

        page.php()

        page.categoryDropDown()

        page.SearchButton()

        page.Ebooks_Items()

        page.ebookPageTitle()

        pages_title = page.Ebooks_Items()  # Capture the pages_title returned
        title_product = page.ebookPageTitle()
        page.asserting(pages_title, title_product)
        logger.info("Assertion successful for pagination")

    def test_wrong_search(self):
        logger = self.test_logger()

        page = Checkout(self.driver)

        self.driver.get("https://staging.profoam.com/documents/")

        page.php()

        page.searchInput().send_keys("Voltas")

        page.SearchButton()

        page.InvalidDoc()
        print("Asertion successful for Wrong search")





