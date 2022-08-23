import random
from model.group import Group


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        group = Group(name="test1")
        app.group.create(group)
    group = Group(name="testr")
    old_groups = db.get_group_list()
    group_choosed = random.choice(old_groups)
    app.group.modify_group_by_id(group_choosed.id, group)
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    old_groups.remove(group_choosed)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(db.get_group_list(), key=Group.id_or_max)

#def test_modify_group_header(app):
 #   old_groups = app.group.get_group_list()
  #  if app.group.count() == 0:
   #     app.group.create(Group(name="test"))
    #app.group.modify_first_group(Group(header="New header"))
    #new_groups = app.group.get_group_list()
   # assert len(old_groups)  == len(new_groups)
#def test_modify_group_name(app):
    #    old_groups = app.group.get_group_list()
    #if app.group.count() == 0:
    #    app.group.create(Group(name="test"))
    #index = randrange(len(old_groups))
    #group = Group(name="New group")
    #group.id = old_groups[index].id
    #app.group.modify_group_by_index(index, group)
    #    new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
    #old_groups[index] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)





