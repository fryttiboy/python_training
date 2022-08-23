from model.contacts import Contact
import  random


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        contact = Contact(firstname="test1")
        app.contacts.create_new(contact)
    contact = Contact(firstname="Egor")
    old_contacts = db.get_group_list()
    contact_choosed = random.choice(old_contacts)
    app.contacts.modify_contact_by_id(contact_choosed.id, contact)
    new_contacts = db.get_contact_list
    assert len(old_contacts) == new_contacts
    old_contacts.remove(contact_choosed)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)


#def test_modify_contact_lastname(app):
 #   old_contacts = app.contacts.get_contact_list()
  #  if app.contacts.count() == 0:
   #     app.contacts.create_new(Contact(firstname="test"))
    #app.contacts.modify_first_contact(Contact(lastname="Nod"))
   # new_contacts = app.contacts.get_contact_list()
    #assert len(old_contacts)  == len(new_contacts)


