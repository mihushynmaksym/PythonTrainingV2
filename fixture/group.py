from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    group_cache = None  # option Cash = None

    def return_to_home_page(self, wd):
        if not len(wd.find_elements_by_xpath("//*[@value='Send e-Mail']")) > 0 \
                and (wd.current_url.endswith("/index.php")):
            return
        wd.find_element_by_link_text("home").click()

    def groups_page(self, wd):
        if len(wd.find_elements_by_xpath("//*[@value='New group']")) > 0 \
                and (wd.current_url.endswith("/group.php")) \
                and len(wd.find_elements_by_xpath("//*[@value='Delete group(s)']")) > 0:
            return
        wd.find_element_by_link_text("groups").click()

    def fill_group(self, group, wd):
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def create(self, group):
        # fill group form
        wd = self.app.wd
        self.groups_page(wd)
        wd.find_element_by_name("new").click()
        self.fill_group(group, wd)
        wd.find_element_by_name("submit").click()
        self.return_to_home_page(wd)
        self.group_cache = None  # option Cash = None

    def modify_first_group(self):
        self.modify_group_by_index(0)

    def modify_group_by_index(self, index, group):
        # fill group form
        wd = self.app.wd
        self.groups_page(wd)
        self.select_group_by_index(index)
        wd.find_element_by_xpath("//*[@value='Edit group']").click()
        self.fill_group(group, wd)
        wd.find_element_by_xpath("//*[@name='update']").click()
        self.return_to_home_page(wd)
        self.group_cache = None  # option Cash = None

    def modify_group_by_id(self, id, group):
        wd = self.app.wd
        self.groups_page(wd)
        self.select_group_by_id(id)
        wd.find_element_by_xpath("//*[@value='Edit group']").click()
        self.fill_group(group, wd)
        wd.find_element_by_xpath("//*[@name='update']").click()
        self.return_to_home_page(wd)
        self.group_cache = None  # option Cash = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        self.groups_page(wd)
        wd.find_elements_by_xpath("//*[@name='selected[]']")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        self.groups_page(wd)
        wd.find_element_by_css_selector("input[value='{0}'".format(id)).click()

    def delete_group_by_index(self, index):
        # take first group value and delete
        wd = self.app.wd
        self.groups_page(wd)
        self.select_group_by_index(index)
        wd.find_element_by_xpath("//*[@value='Delete group(s)']").click()
        self.return_to_home_page(wd)
        self.group_cache = None  # option Cash = None

    def delete_group_by_id(self, id):
        # take first group value and delete
        wd = self.app.wd
        self.groups_page(wd)
        self.select_group_by_id(id)
        wd.find_element_by_xpath("//*[@value='Delete group(s)']").click()
        self.return_to_home_page(wd)
        self.group_cache = None  # option Cash = None

    def count(self):
        wd = self.app.wd
        self.groups_page(wd)
        return len(wd.find_elements_by_xpath("//*[@name='selected[]']"))

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.groups_page(wd)
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
