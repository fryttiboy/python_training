from model.contacts import Contact


def test_modify_contact_firstname(app):
    app.contacts.modify_first_contact(Contact(firstname="Egor"))


def test_modify_contact_lastname(app):
    app.contacts.modify_first_contact(Contact(lastname="Nod"))