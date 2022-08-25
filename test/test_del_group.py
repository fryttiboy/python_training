import random

from model.group import Group
import random


def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    print(old_groups)
    group = random.choice(old_groups)
    print("group")
    print(group)
    app.group.delete_group_by_id(group.id)

    def clean(group):
        return  Group(id=group.id, name=group.name.strip())
    new_groups = db.get_group_list()
    print("new_groups")
    print(new_groups)
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(map(clean,new_groups), key=Group.id_or_max) == sorted(db.get_group_list(), key=Group.id_or_max)


