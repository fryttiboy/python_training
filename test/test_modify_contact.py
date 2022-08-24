from model.contacts import Contact
import  random
from  random import randrange


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test_contact", middlename="", lastname="", nickname="", title="",
                                   company="", address="", home_number="", mobile_number="", work_number="", fax="", email="",
                                   email2="", email3="", homepage="", bday="5", bmonth="July", byear="2022", aday="5",
                                   amonth="July", ayear="2022", address2="", phone2="", notes=""))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Test_contact", middlename="", lastname="", nickname="", title="",
                      company="", address="", home_number="", mobile_number="", work_number="", fax="", email="",
                      email2="", email3="", homepage="", bday="5", bmonth="July", byear="2022", aday="5",
                      amonth="July", ayear="2022", address2="", phone2="", notes="")
    contact.id = old_contacts[index].id
    app.contacts.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



#def test_modify_contact_lastname(app):
 #   old_contacts = app.contacts.get_contact_list()
  #  if app.contacts.count() == 0:
   #     app.contacts.create_new(Contact(firstname="test"))
    #app.contacts.modify_first_contact(Contact(lastname="Nod"))
   # new_contacts = app.contacts.get_contact_list()
    #assert len(old_contacts)  == len(new_contacts)


