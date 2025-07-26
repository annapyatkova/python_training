from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phones(maxlen):
    return random.choice(["+", ""]) + "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


def random_emails(maxlen, postfix):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + postfix


testdata = [
    Contact(firstname=random_string("firstname", 5), middlename=random_string("middlename", 5),
            lastname=random_string("lastname", 5), nickname=random_string("nickname", 5),
            photo="C:\\Users\\Ann\\Downloads\\cat.jpg", title=random_string("title", 10),
            company=random_string("company", 10), address=random_string("address", 10), home_phone=random_phones(6), mobile_phone=random_phones(10),
            work_phone=random_phones(6), fax=random_phones(3), email_1=random_emails(10, "@test.ru"),
            email_2=random_emails(10, "@test.ru"), email_3=random_emails(10, "@test.ru"), homepage="test.ru", bday="1", byear="1911", aday="2",
            ayear="1922", bmonth="March", amonth="January") for i in range(2)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))