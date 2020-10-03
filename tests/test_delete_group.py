from model.group import Group
import random


def test_delete_random_group(app, db):
    if len(db.get_group_list()) == 0:  # precondition rule for test, if group doesn't exist, create group.
        app.group.create(Group(name='param1', header='param2', footer='param3'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)  # index random param by delete
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
