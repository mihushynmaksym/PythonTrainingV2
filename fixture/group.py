class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def fill_group(self, group, wd):
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def create(self, group):
        # fill group form
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        self.fill_group(group, wd)
        wd.find_element_by_name("submit").click()
        self.return_to_home_page(wd)

    def modify(self, group):
        # fill group form
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_xpath("//*[@name='selected[]']").click()
        wd.find_element_by_xpath("//*[@value='Edit group']").click()
        self.fill_group(group, wd)
        wd.find_element_by_xpath("//*[@name='update']").click()
        self.return_to_home_page(wd)

    def delete(self):
        # take first group value and delete
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_xpath("//*[@name='selected[]']").click()
        wd.find_element_by_xpath("//*[@value='Delete group(s)']").click()
        self.return_to_home_page(wd)
