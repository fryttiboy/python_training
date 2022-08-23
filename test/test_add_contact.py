# -*- coding: utf-8 -*-
from model.contacts import Contact


def test_add_contact(app, db,  json_contact):
    contact = json_contact
    old_contacts = db.get_group_list()
    app.contacts.create_new(contact)
    new_contacts = db.get_group_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
