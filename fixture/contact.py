import re
from model.contact import Contact
import time


class ContactHelper:
    def __init__(self, app):
        self.app = app

    contact_cache = None

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
        self.contact_cache = None

    def modify_by_index(self, index, contact):
        wd = self.app.wd
        # modify form contact
        self.return_to_home_page(wd)
        self.select_contact_for_edit_by_index(index)
        self.fill_contact_form(contact, wd)
        wd.find_element_by_xpath("//*[@value='Update']").click()
        self.return_to_home_page(wd)
        self.contact_cache = None

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        # modify form contact
        self.return_to_home_page(wd)
        self.select_contact_for_edit_by_id(id)
        self.fill_contact_form(contact, wd)
        wd.find_element_by_xpath("//*[@id='content']/form[1]/input[22]").click()
        self.group_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='{0}'".format(id)).click()

    def delete_contact_by_id(self, id):
        # delete first value contact
        wd = self.app.wd
        self.return_to_home_page(wd)
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        wd.switch_to.alert.accept()  # work with pop-up option
        wd.find_element_by_css_selector("div.msgbox")  # waiter for delete option
        self.return_to_home_page(wd)

    def delete_contact_by_index(self, index):
        # delete first value contact
        wd = self.app.wd
        self.return_to_home_page(wd)
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//*[@value='Delete']").click()
        wd.switch_to.alert.accept()  # work with pop-up option
        wd.find_element_by_css_selector("div.msgbox")  # waiter for delete option
        self.return_to_home_page(wd)
        self.contact_cache = None

    def select_first_contact_for_edit_by_index(self):
        self.select_contact_for_edit_by_index(0)

    def select_contact_for_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//*[@alt='Edit']")[index].click()

    def select_contact_for_edit_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='edit.php?id={0}']/img[@alt='Edit']".format(id)).click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//*[@name='selected[]']")[index].click()

    def select_first_contact_for_delete_by_index(self):
        self.select_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.return_to_home_page(wd)
        return len(wd.find_elements_by_xpath("//*[@name='selected[]']"))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page(wd)
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//*[@name='entry']"):
                param = element.find_elements_by_tag_name("td")
                lastname = param[1].text  # take lastname text value
                firstname = param[2].text  # take firstname text value
                adress = param[3].text
                all_emails = param[4].text
                all_phones = param[5].text
                id = param[0].find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id, address=adress,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def add_contact_in_group(self, contact_id, group_id):
        wd = self.app.wd
        self.return_to_home_page(wd)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_xpath("//*[@name='to_group']/option[@value='{0}']".format(group_id)).click()
        wd.find_element_by_xpath("//*[@type='submit']").click()
        self.return_to_home_page(wd)

    def dell_contact_in_group(self, contact_id, group_id):
        wd = self.app.wd
        self.return_to_home_page(wd)
        wd.get("http://localhost/addressbook/index.php?group={0}".format(group_id))
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[3]/input")
        self.select_contact_by_id(contact_id)
        wd.find_element_by_xpath("//*[@id='content']/form[2]/div[3]/input").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.return_to_home_page(wd)
        self.select_contact_for_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name('firstname').get_attribute("value")
        lastname = wd.find_element_by_name('lastname').get_attribute("value")
        address = wd.find_element_by_name('address').text
        email1 = wd.find_element_by_name('email').get_attribute("value")
        email2 = wd.find_element_by_name('email2').get_attribute("value")
        email3 = wd.find_element_by_name('email3').get_attribute("value")
        home_phone = wd.find_element_by_name('home').get_attribute("value")
        mobile_phone = wd.find_element_by_name('mobile').get_attribute("value")
        work_phone = wd.find_element_by_name('work').get_attribute("value")
        secondary_phone = wd.find_element_by_name('phone2').get_attribute("value")
        id = id
        return Contact(firstname=firstname, lastname=lastname, address=address, email=email1, email2=email2,
                       email3=email3, home=home_phone, mobile=mobile_phone, work=work_phone, phone2=secondary_phone,
                       id=id)

    def clear_signs(self, s):
        return re.sub("[()-,?!@#$%:;'\"]", "", s)

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear_signs(x),
                                    filter(lambda x: x is not None,
                                           [contact.home, contact.mobile, contact.work, contact.phone2]))))

    def merge_email_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear_signs(x),
                                    filter(lambda x: x is not None,
                                           [contact.email, contact.email2, contact.email3]))))
