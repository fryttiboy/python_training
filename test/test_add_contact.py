# -*- coding: utf-8 -*-
from model.contacts import Contact
import pytest
import string
import random


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                    address="", home_number="", mobile_number="", work_number="", fax="", email="", email2="",
                                    email3="", homepage="", bday="11", bmonth= "August", byear= "5655", aday= "13", amonth= "September", ayear= "677", address2= "",
                                    phone2="", notes="")] + [Contact(firstname=random_string("firstname",10), middlename=random_string("middlename",20), lastname=random_string("lastname",20), nickname=random_string("nickname",10), title=random_string("title",10), company=random_string("company",10),
                                    address= random_string("address",20), home_number=random_string("home_number",20), mobile_number=random_string("mobile_number",20), work_number=random_string("work_number",20), fax=random_string("fax",15), email=random_string("email",20), email2=random_string("email2",20),
                                    email3=random_string("email3",20), homepage= random_string("homepage",20), bday="11", bmonth="August", byear="13", aday="20", amonth= "September", ayear="10", address2=random_string("address2",20),
                                    phone2=random_string("phone2",20), notes=random_string("notes",20))
                                    for i in range(5)
                                                             ]




@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contacts.get_contact_list()
    app.contacts.create_new(contact)
    assert len(old_contacts) + 1 == app.contacts.count()
    new_contacts = app.contacts.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
