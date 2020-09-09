from model.group import Group
from random import randrange


def test_modify_first_group(app):
    group = Group(name='param1', header='param2', footer='param3')
    if app.group.count() == 0:
        app.group.create(group)  # precondition rule for test, if group doesn't exist, create group.
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))  # index random param by modify
    group.id = old_groups[index].id  # index random param by modify
    app.group.modify_group_by_index(index, group)  # index random param by modify
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group  # index random param by modify
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
