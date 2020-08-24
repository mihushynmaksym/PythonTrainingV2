class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        # fill form new contact
        wd = self.app.wd
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
        wd.find_element_by_link_text("home page").click()

    def modify(self, contact):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@alt='Edit']").click()
        # modify form contact
        wd = self.app.wd
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
        # modify form contact
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").send_keys(contact.adress2)
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_xpath("//*[@value='Update']").click()
        wd.find_element_by_link_text("home page").click()

    def delete(self):
        # delete first value contact
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@name='selected[]']").click()
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        wd.switch_to.alert.accept()
