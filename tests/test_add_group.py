from model.group import Group


def test_create_new_group(app):
    app.group.create(Group(name='param1', header='param2', footer='param3'))
