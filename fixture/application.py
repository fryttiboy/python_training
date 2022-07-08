from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contacts import ContactsHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contacts = ContactsHelper(self)

    def is_valid(self):
        try:
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()


