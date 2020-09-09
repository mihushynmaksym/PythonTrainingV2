from model.group import Group


def test_modify_first_group(app):
    group = Group(name='param1', header='param2', footer='param3')
    if app.group.count() == 0:
        app.group.create(group)  # precondition rule for test, if group doesn't exist, create group.
    old_groups = app.group.get_group_list()
    group.id = old_groups[0].id
    app.group.modify(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
