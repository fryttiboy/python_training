from model.contacts import Contact
from random import randrange


def test_delete_first_contact(app):
    if app.contacts.count() == 0:
        app.contacts.create_new(Contact(firstname="test"))
    old_contacts = app.contacts.get_contact_list()
    index = randrange(len(old_contacts))
    app.contacts.delete_contact_by_index(index)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts