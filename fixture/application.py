from selenium import webdriver

from fixture.session import SessionHelper
from test.authorization_case.assert_authorization import AssertHelper



class Application:

    def __init__(self):
<<<<<<< HEAD
        self.wd = webdriver.Firefox(executable_path="C:/Devel/NEO/driver/geckodriver.exe")
=======
<<<<<<< Updated upstream
        self.wd = webdriver.Firefox(executable_path="C:/Users/polinkevich/PycharmProjects/NEO1/driver1/geckodriver.exe")
=======
        self.wd = webdriver.Firefox(executable_path="driver/geckodriver.exe")
>>>>>>> Stashed changes
>>>>>>> Polinkevich
        self.wd.maximize_window()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.assert_helper = AssertHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://10.10.1.222/signIn")

    def destroy(self):
        self.wd.quit()
