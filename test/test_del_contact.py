from model.contacts import Contact
import random


def test_delele_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contacts.create_new(Contact(firstname="Test_contact"))
    old_contacts = db.get_contact_list()
    print("old contacts")
    print(old_contacts)
    contact = random.choice(old_contacts)
    print("contact")
    print(contact)
    app.contacts.delete_contact_by_id(contact.id)
    def clean(contact):
        return  Contact(id=contact.id, firstname=contact.firstname.strip())
    new_contact = db.get_contact_list()
    print("new_contacts")
    print(new_contact)
    assert len(old_contacts) - 1 == len(new_contact)
    old_contacts.remove(contact)
    assert old_contacts == new_contact
    if check_ui:
         assert sorted(map(clean, new_contact), key=Contact.id_or_max) == sorted(app.contacts.get_contact_list(),
                                                                              key=Contact.id_or_max)