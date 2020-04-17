from selenium import webdriver

from fixture.session import SessionHelper
from test.authorization_case.assert_authorization import AssertHelper



class Application:

    def __init__(self):
        self.wd = webdriver.Firefox(executable_path="C:/Devel/NEO/driver/geckodriver.exe")
        self.wd.maximize_window()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.assert_helper = AssertHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://10.10.1.222/signIn")

    def destroy(self):
        self.wd.quit()
