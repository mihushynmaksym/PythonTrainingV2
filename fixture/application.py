from selenium import webdriver
from fixture.session import SessionHelper
from fixture.contact import ContactHelper
from fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)

    def destroy(self):
        self.wd.quit()
