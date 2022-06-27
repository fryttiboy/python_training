# -*- coding: utf-8 -*-
import pytest
from contacts import Contact
from applying import Applying


@pytest.fixture
def app(request):
    fixture = Applying()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new(app):
    app.login(username="admin", password="secret")
    app.create_new_contacts(Contact(firstname="wrtertfe", middlename="swdwdef", lastname="efwafrar", nickname="rfarfwefa", title="gbfshsrt", company="rragsrehgrt",
                                        address= "sdgthebtbgs", home_number="dfbsthet", mobile_number="dfvrvgr", work_number="scecdc", fax="ececcsc", email="scwferfrcd", email2="scweferv",
                                        email3= "cdevrvdc", homepage= "scefefcs", bday= "11", bmonth= "August", byear= "5655", aday= "13", amonth= "September", ayear= "677", address2= "uykyg",
                                        phone2="yglugyg", notes= "iblhbhjvkj"))
    app.logout()



def test_add_null_new(app):
    app.login(username="admin", password="secret")
    app.create_new_contacts(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                        address="", home_number="", mobile_number="", work_number="", fax="", email="", email2="",
                                        email3="", homepage="", bday="11", bmonth= "August", byear= "5655", aday= "13", amonth= "September", ayear= "677", address2= "",
                                        phone2="", notes=""))
    app.logout()
