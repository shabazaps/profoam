import time

from pages.memeber_details_negative import Member_details

from utilities.logger import BaseClass


class Test_profile(BaseClass):
    def test_editprofile(self, setup):
        logger = self.test_logger()

        profile = Member_details(self.driver)

        # Click on profile icon
        profile.profile_icon()
        logger.info("Profile icon clicked successfully")

        #Click on edit profile
        profile.edit_profile()
        logger.info("Edit profile clicked successfully")

        # Select Salutation as Professor
        profile.salutation_button()
        logger.info("Salutation selected as Professor")

        # Enter First Name
        profile.first_name()
        logger.info("First Name entered successfully")

        #enter Last Name
        profile.last_name()
        logger.info("Last Name entered successfully")

        # Enter Email
        profile.email_address()
        logger.info("Email entered successfully")

        # Enter Mobile Number
        profile.mobile_number()
        logger.info("Mobile Number entered successfully")

        # Enter Business name
        profile.business_name()
        logger.info("Business Name entered successfully")

        #Delete Business Name
        # profile.delete_businessName()
        # logger.info("Business Name deleted successfully")

        # Enter address line 1
        profile.addressLine1()
        logger.info("Address Line 1 entered successfully")

        # Enter address line 2
        profile.addressLine2()
        logger.info("Address Line 2 entered successfully")

        # Select Country
        profile.country_dropdown()
        logger.info("Country selected successfully")

        # Select province
        profile.province_dropdown()
        logger.info("Province selected successfully")

        # Enter City
        profile.city_input()
        logger.info("City entered successfully")

        # Enter Postal Code
        profile.postal_code()
        logger.info("Postal Code entered successfully")

        # Click on Update button
        profile.update_button()
        logger.info("Update button clicked successfully")
