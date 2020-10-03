from model.group import Group
import random


def test_modify_first_group(app, db):
    group = Group(name='param1', header='param2', footer='param3')
    if len(db.get_group_list()) == 0:
        app.group.create(group)  # precondition rule for test, if group doesn't exist, create group.
    old_groups = db.get_group_list()
    group = random.choice(old_groups)  # index random param by modify
    app.group.modify_group_by_id(group.id, group)  # index random param by modify
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
