from model.contacts import Contact
import random


def test_delete_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
         app.contacts.create_new(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contacts.delete_contact_by_id(contact.id)
    def clean(contact):
      return Contact(id=contact.id, firstname=contact.firstname.strip())
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(map(clean,new_contacts), key=Contact.id_or_max) == sorted(app.contacts.get_group_list(), key=Contact.id_or_max)
