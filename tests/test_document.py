import time

from pages.chekout import Checkout
from utilities.logger import BaseClass


class Test_Document(BaseClass):

    def test_doc_search(self,setup):
        logger = self.test_logger()

        doc = Checkout(self.driver)

        #Click on the Document link
        doc.document_link()

        #Enter Graco Fusion in search input
        doc.searchInput()

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

    def test_doc_tag(self,setup):
        logger = self.test_logger()

        doc = Checkout(self.driver)


        self.driver.get("https://staging.profoam.com/document/")
        # Click on the Document link
        doc.document_link()

        #Select Accufoam from tag dropdown
        doc.Tag()

        #Click on Search Button
        doc.SearchButton()

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







