from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_home_page(self, wd):
        if len(wd.find_elements_by_xpath("//*[@value='Send e-Mail']")) > 0 \
                and (wd.current_url.endswith("/index.php")):
            return
        wd.find_element_by_link_text("home").click()

    def fill_contact_form(self, contact, wd):
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # take date from UI
        wd.find_element_by_xpath("//option[@value='5']").click()
        wd.find_element_by_xpath("//option[@value='May']").click()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        # take date from UI
        wd.find_element_by_xpath("(//option[@value='5'])[2]").click()
        wd.find_element_by_xpath("(//option[@value='May'])[2]").click()
        # fill form new contact
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.adress2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def create(self, contact):
        # create form new contact
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact, wd)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page(wd)

    def modify(self, contact):
        wd = self.app.wd
        # modify form contact
        self.return_to_home_page(wd)
        wd.find_element_by_xpath("//*[@alt='Edit']").click()
        self.fill_contact_form(contact, wd)
        wd.find_element_by_xpath("//*[@value='Update']").click()
        self.return_to_home_page(wd)

    def delete(self):
        # delete first value contact
        wd = self.app.wd
        self.return_to_home_page(wd)
        wd.find_element_by_xpath("//*[@name='selected[]']").click()
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        wd.switch_to.alert.accept()  # work with pop-up option
        wd.find_element_by_css_selector("div.msgbox")  # waiter for delete option
        self.return_to_home_page(wd)

    def count(self):
        wd = self.app.wd
        self.return_to_home_page(wd)
        return len(wd.find_elements_by_xpath("//*[@name='selected[]']"))

    def get_contact_list(self):
        wd = self.app.wd
        self.return_to_home_page(wd)
        list_contact = []
        for element in wd.find_elements_by_xpath("//*[@name='entry']"):
            param = element.find_elements_by_tag_name("td")
            lastname = param[1].text  # take lastname text value
            firstname = param[2].text  # take firstname text value
            id = element.find_element_by_name("selected[]").get_attribute("value")
            list_contact.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list_contact
