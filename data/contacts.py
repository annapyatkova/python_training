from model.contact import Contact
import random
import string


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
            photo="C:\\Users\Ann\Downloads\cat.jpg", title=random_string("title", 10),
            company=random_string("company", 10), address=random_string("address", 10), home_phone=random_phones(6), mobile_phone=random_phones(10),
            work_phone=random_phones(6), fax=random_phones(3), email_1=random_emails(10, "@test.ru"),
            email_2=random_emails(10, "@test.ru"), email_3=random_emails(10, "@test.ru"), homepage="test.ru", bday="1", byear="1911", aday="2",
            ayear="1922", bmonth="March", amonth="January") for i in range(2)
]