class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, login, password):
        wd = self.app.wd
        wd.get("http://localhost:8080/addressbook/index.php")
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()
