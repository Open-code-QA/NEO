class AssertHelper:

    def __init__(self, app):
        self.app = app

    def assert_login(self):
        wd = self.app.wd
        text_title = wd.find_element_by_xpath("/html/body/div/main/section/div[2]")
        return text_title.text
