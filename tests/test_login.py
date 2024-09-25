from pages.login import Login
from utilities.logger import BaseClass


class Test_login(BaseClass):
    def test_login(self,setup):
        logger = self.test_logger()
        login = Login(self.driver)
        login.home()

        # Login Page
        login.login()
        login.password()
        login.remember()
        login.login_submit()