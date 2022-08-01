from model.contacts import Contact
from random import randrange


def test_modify_contact_firstname(app):
    old_contacts = app.contacts.get_contact_list()
    if app.contacts.count() == 0:
        app.contacts.create_new(Contact(firstname="test"))
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Egor")
    contact.id = old_contacts[0].id
    app.contacts.modify_contact_by_index(index, contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact



#def test_modify_contact_lastname(app):
 #   old_contacts = app.contacts.get_contact_list()
  #  if app.contacts.count() == 0:
   #     app.contacts.create_new(Contact(firstname="test"))
    #app.contacts.modify_first_contact(Contact(lastname="Nod"))
   # new_contacts = app.contacts.get_contact_list()
    #assert len(old_contacts)  == len(new_contacts)


