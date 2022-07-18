from model.contacts import Contact


def test_modify_contact_firstname(app):
    old_contacts = app.contacts.get_contact_list()
    if app.contacts.count() == 0:
        app.contacts.create_new(Contact(firstname="test"))
    contact = Contact(firstname="Egor")
    contact.id = old_contacts[0].id
    app.contacts.modify_first_contact(contact)
    new_contacts = app.contacts.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact



#def test_modify_contact_lastname(app):
 #   old_contacts = app.contacts.get_contact_list()
  #  if app.contacts.count() == 0:
   #     app.contacts.create_new(Contact(firstname="test"))
    #app.contacts.modify_first_contact(Contact(lastname="Nod"))
   # new_contacts = app.contacts.get_contact_list()
    #assert len(old_contacts)  == len(new_contacts)


