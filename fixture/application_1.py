from selenium import webdriver
from fixture.session1 import Session1Helper
from fixture.contacts import ContactsHelper


class Application1:

    def __init__(self):
        self.wd = webdriver.Chrome()

        self.wd.implicitly_wait(30)
        self.session1 = Session1Helper(self)
        self.contacts = ContactsHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()