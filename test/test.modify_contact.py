from model.contacts import Contact


def test_modify_contact_name(app):
    app.group.modify_first_contact(Contact(firstname="Egor"))


def test_modify_contact_header(app):
    app.group.modify_first_contact(Contact(lastname="Nod"))