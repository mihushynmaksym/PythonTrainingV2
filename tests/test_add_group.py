from model.group import Group


def test_create_new_group(app):
    app.session.login(login='admin', password='secret')
    app.group.create(Group(name='param1', header='param2', footer='param3'))
    app.session.logout()
