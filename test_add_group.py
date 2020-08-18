# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()

    def test_untitled_test_case(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/index.php")
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").send_keys("asd1")
        wd.find_element_by_name("group_header").send_keys("asd1")
        wd.find_element_by_name("group_footer").send_keys("asd1")
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
