from selenium import webdriver
from group import Group
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()

    def test_create_group(self):
        wd = self.wd
        self.login(wd, login='admin', password='secret')
        self.create_new_group(wd, Group(name='param1', header='param2', footer='param3'))
        self.logout(wd)

    def test_create_group_with_empty_param(self):
        wd = self.wd
        self.login(wd, login='admin', password='secret')
        self.create_new_group(wd, Group(name='', header='', footer=''))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_new_group(self, wd, group):
        # fill group form
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()

    def login(self, wd, login, password):
        wd.get("http://localhost:8080/addressbook/index.php")
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
