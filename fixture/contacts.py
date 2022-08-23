from selenium.webdriver.support.ui import Select
from model.contacts import Contact
import re


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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_contact(self, index):
        self.modify_contact_by_index(index)

    def modify_contact_by_index(self, index, new_contacts_data):
        wd = self.app.wd
        self.app.open_home_page()
        # open modification form
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contacts_data)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None



    def modify_contact_by_id(self,id, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
        # open modification form
        wd.find_elements_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
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
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_email = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname, address=address,
                                                  all_emails_from_home_page=all_email,  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home_number = wd.find_element_by_name("home").get_attribute("value")
        mobile_number = wd.find_element_by_name("mobile").get_attribute("value")
        work_number = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, home_number=home_number, mobile_number=mobile_number, work_number=work_number, phone2=phone2,address = address,email = email,email2 =email2,email3 = email3, id=id)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        raw = wd.find_elements_by_name("entry")[index]
        cell = raw.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        raw = wd.find_elements_by_name("entry")[index]
        cell = raw.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_number = re.search("H: (.*)", text).group(1)
        mobile_number = re.search("M: (.*)", text).group(1)
        work_number = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_number=home_number, mobile_number=mobile_number,
                       work_number=work_number, phone2=phone2)

