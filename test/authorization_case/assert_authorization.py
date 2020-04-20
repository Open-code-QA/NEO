class AssertAuthorization:

    def __init__(self, app):
        self.app = app

    def assert_login(self):
        wd = self.app.wd
        text_title = wd.find_element_by_class_name("text")
        return text_title.text
