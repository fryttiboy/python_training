from model.contacts import Contact


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                    address="", home_number="", mobile_number="", work_number="", fax="", email="", email2="",
                                    email3="", homepage="", bday="11", bmonth= "August", byear= "5655", aday= "13", amonth= "September", ayear= "677", address2= "",
                                    phone2="", notes="")] + [Contact(firstname=("firstname",10), middlename=("middlename",20), lastname=("lastname",20), nickname=("nickname",10), title=("title",10), company=("company",10),
                                    address= ("address",20), home_number=("home_number",20), mobile_number=("mobile_number",20), work_number=("work_number",20), fax=("fax",15), email=("email",20), email2=("email2",20),
                                    email3=("email3",20), homepage= ("homepage",20), bday="11", bmonth="August", byear="13", aday="20", amonth= "September", ayear="10", address2=("address2",20),
                                    phone2=("phone2",20), notes=("notes",20))
                                    for i in range(5)
                                                             ]