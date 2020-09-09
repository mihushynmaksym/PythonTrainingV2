from model.group import Group
from random import randrange


def test_delete_first_group(app):
    if app.group.count() == 0:  # precondition rule for test, if group doesn't exist, create group.
        app.group.create(Group(name='param1', header='param2', footer='param3'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)  # index random param by delete
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []  # index random param by delete
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
