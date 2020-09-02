from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:  # precondition rule for test
        app.group.create(Group(name='param1', header='param2', footer='param3'))
    app.group.delete()
