

class ContactsHelper:
    def __init__(self, app):
        self.app = app

    def open_add_new(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create_new(self, contacts):
        wd = self.app.wd
        self.open_add_new()
        # init contacts  creation
        wd.find_element_by_name("firstname").click()
        self.fill_contact_form(contacts)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def fill_contact_form(self, contacts):
        wd = self.app.wd
        self.change_fieled_value("firstname", contacts)
        self.change_fieled_value("middlename", contacts)
        self.change_fieled_value("lastname", contacts)
        self.change_fieled_value("nickname", contacts)
        self.change_fieled_value("title", contacts)
        self.change_fieled_value("company", contacts)
        self.change_fieled_value("address", contacts)
        self.change_fieled_value("home", contacts)
        self.change_fieled_value("mobile", contacts)
        self.change_fieled_value("work", contacts)
        self.change_fieled_value("fax", contacts)
        self.change_fieled_value("email", contacts)
        self.change_fieled_value("email2", contacts)
        self.change_fieled_value("email3", contacts)
        self.change_fieled_value("homepage", contacts)
        self.change_fieled_value("bday", contacts)
        self.change_fieled_value("bmonth", contacts)
        self.change_fieled_value("byear", contacts)
        self.change_fieled_value("aday", contacts)
        self.change_fieled_value("amonth", contacts)
        self.change_fieled_value("ayear", contacts)
        self.change_fieled_value("address2", contacts)
        self.change_fieled_value("phone2", contacts)
        self.change_fieled_value("notes", contacts)

    def change_fieled_value(self, field_name, text):
        wd = self.app.wd
        if text.firstname is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text.firstname)

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()