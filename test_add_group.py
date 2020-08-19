from selenium import webdriver
from group import Group
from contact import Contact
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()

    def test_create_group(self):
        wd = self.wd
        self.login(wd, login='admin', password='secret')
        self.create_new_group(wd, Group(name='param1', header='param2', footer='param3'))
        self.logout(wd)

    def test_create_new_contact(self):
        wd = self.wd
        self.login(wd, login='admin', password='secret')
        self.create_new_contact(wd, Contact(firstname='firstname',
                                            middlename='midlename',
                                            lastname='lastname',
                                            nickname='nickname',
                                            title='title',
                                            company='company',
                                            address='adress',
                                            home='home',
                                            mobile='mobile',
                                            work='work',
                                            fax='fax',
                                            email='email',
                                            email2='email2',
                                            email3='email3',
                                            homepage='homepage',
                                            byear='byear',
                                            ayear='ayear',
                                            adress2='adress2',
                                            phone2='phone2',
                                            notes='notes'))

    def create_new_contact(self, wd, contact):
        # fill form new contact
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # take date from UI
        wd.find_element_by_xpath("//option[@value='5']").click()
        wd.find_element_by_xpath("//option[@value='May']").click()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        # take date from UI
        wd.find_element_by_xpath("(//option[@value='5'])[2]").click()
        wd.find_element_by_xpath("(//option[@value='May'])[2]").click()
        # fill form new contact
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").send_keys(contact.adress2)
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

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
