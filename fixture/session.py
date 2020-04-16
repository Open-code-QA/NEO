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
        time.sleep(3)
        wd.find_element_by_xpath("/html/body/div/main/section/div[2]/form/div[2]/input").click()
        wd.find_element_by_xpath("/html/body/div/main/section/div[2]/form/div[2]/input").clear()
        wd.find_element_by_xpath("/html/body/div/main/section/div[2]/form/div[2]/input").send_keys(password)
        time.sleep(3)
        wd.find_element_by_xpath("/html/body/div/main/section/div[2]/form/button").click()
        time.sleep(3)
