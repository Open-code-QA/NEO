import time

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_class_name("sign-form__form__input").click()
        wd.find_element_by_class_name("sign-form__form__input").clear()
        wd.find_element_by_class_name("sign-form__form__input").send_keys(username)
        wd.find_element_by_xpath("/html/body/div/main/section/div[2]/form/div[2]/input").click()
        wd.find_element_by_xpath("/html/body/div/main/section/div[2]/form/div[2]/input").clear()
        wd.find_element_by_xpath("/html/body/div/main/section/div[2]/form/div[2]/input").send_keys(password)
        wd.find_element_by_xpath("/html/body/div/main/section/div[2]/form/button").click()

    def open_neo(self):
        wd = self.app.wd
        wd.find_element_by_class_name("home-tab").click()

    def home_button(self):
        wd = self.app.wd
        wd.find_element_by_class_name("navigation__nav-link").click()

    def logout_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/header/div[3]/button").click()