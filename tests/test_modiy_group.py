from model.group import Group
import time


def test_modify_first_group(app):
    app.session.login(login='admin', password='secret')
    app.group.modify(Group(name='param1', header='param2', footer='param3'))
    app.session.logout()
    time.sleep(1)
