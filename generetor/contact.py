import jsonpickle
from model.contacts import Contact
import random
import string
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
                                    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))