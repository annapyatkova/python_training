from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, photo=None, title=None, company=None, address=None, home_phone=None,
                       mobile_phone=None, work_phone=None, fax=None, email_1=None, email_2=None, email_3=None, homepage=None, bday=None, byear=None, aday=None, ayear=None,
                       bmonth=None, amonth=None, id = None, all_phones_from_home_page = None, all_emails_from_home_page = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.homepage = homepage
        self.bday = bday
        self.byear = byear
        self.aday = aday
        self.ayear = ayear
        self.bmonth = bmonth
        self.amonth = amonth
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page


    def __repr__(self):
        return "(%s)%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == self.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize