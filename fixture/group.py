class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        # fill group form
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("group page").click()
