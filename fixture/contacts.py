from selenium.webdriver.support.ui import Select
from model.contacts import Contact


class ContactsHelper:
    def __init__(self, app):
        self.app = app

    def open_add_new(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create_new(self, contacts):
        wd = self.app.wd
        self.open_add_new()
        # init contacts  creation
        wd.find_element_by_name("firstname").click()
        self.fill_contact_form(contacts)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None


    def fill_contact_form(self, contacts):
        wd = self.app.wd
        self.change_fieled_value("firstname", contacts.firstname)
        self.change_fieled_value("middlename", contacts.middlename)
        self.change_fieled_value("lastname", contacts.lastname)
        self.change_fieled_value("nickname", contacts.nickname)
        self.change_fieled_value("title", contacts.title)
        self.change_fieled_value("company", contacts.company)
        self.change_fieled_value("address", contacts.address)
        self.change_fieled_value("home", contacts.home_number)
        self.change_fieled_value("mobile", contacts.mobile_number)
        self.change_fieled_value("work", contacts.work_number)
        self.change_fieled_value("fax", contacts.fax)
        self.change_fieled_value("email", contacts.email)
        self.change_fieled_value("email2", contacts.email2)
        self.change_fieled_value("email3", contacts.email3)
        self.change_fieled_value("homepage", contacts.homepage)
        self.change_fieled1_value("bday", contacts.bday)
        self.change_fieled1_value("bmonth", contacts.bmonth)
        self.change_fieled_value("byear", contacts.byear)
        self.change_fieled1_value("aday", contacts.aday)
        self.change_fieled1_value("amonth", contacts.amonth)
        self.change_fieled_value("ayear", contacts.ayear)
        self.change_fieled_value("address2", contacts.address2)
        self.change_fieled_value("phone2", contacts.phone2)
        self.change_fieled_value("notes", contacts.notes)

    def change_fieled_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_fieled1_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def modify_first_contact(self, new_contacts_data):
        wd = self.app.wd
        self.app.open_home_page()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contacts_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                third_cell = cells[2]
                self.contact_cache.append(Contact(id=id, firstname=third_cell.text))

        return list(self.contact_cache)

