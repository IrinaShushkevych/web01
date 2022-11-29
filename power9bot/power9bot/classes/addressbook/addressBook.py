from collections import UserDict
from shutil import get_terminal_size
from classes.addressbook.birthday import Birthday
from classes.addressbook.email import Email
from classes.addressbook.record import Record


class AddressBook(UserDict):

    def iterator(self):
        for record in self.data.values():
            yield record

    def add_address(self, name, addr):
        """
        Adding <address> to the contact <name>
        """
        if name not in self.data:
            raise ValueError(f'Contact {name} has not been found')
        if self.data[name].address:
            raise ValueError(
                f'Contact already have address. Did you want to change it? Use change address command instead')
        self.data[name].address = addr

    def add_birthday(self, name, birthday):
        """
        Adding <birthday> to the contact <name>
        """
        if name not in self.data:
            raise ValueError(f'Contact {name} has not been found')
        if self.data[name].birthday:
            raise ValueError(
                f'Contact already have birthday. Did you want to change it? Use change birthday command instead')
        try:
            self.data[name].birthday = Birthday(birthday)

        except TypeError:
            raise TypeError(
                f'Format for birthday - dd.mm.YYYY, example 01.01.1970')

    def add_contact(self, name):
        """
        Creating new contact with given <name>
        """
        if name not in self.data:
            new_record = Record(name)
            self.data[new_record.name.value] = new_record

        else:
            raise ValueError(
                f'Contact with this name exist. Try other name or other command')

    def add_email(self, name, email):
        """
        Adding <email> to the contact <name>
        """
        if name not in self.data:
            raise ValueError(f'Contact {name} has not been found')
        if self.data[name].email:
            raise ValueError(
                f'Contact already have email. Did you want to change it? Use change email command instead')
        try:
            self.data[name].email = Email(email)
        except ValueError:
            raise ValueError("Mistake in email, example: my_email@python.com")

    def add_phone(self, name, phone):
        """
        Adding <phone> to the contact <name>
        """
        if name not in self.data:
            raise ValueError(f'Contact {name} has not been found')
        for ph in self.data[name].phones:
            if ph.value == phone:
                raise ValueError(
                    f'Contact already have that phone. Did you want to change it? Use change phone command instead')
        try:
            self.data[name].add_new_phone(phone)
        except ValueError:
            raise ValueError("Use only number for phone. Example: 32457")

    def change_address(self, name, address):
        """
        Changing <address> in the contact <name>
        """
        try:
            self.data[name].address = address
        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def change_birthday(self, name, birthday):
        """
        Changing <birthday> in the contact <name>
        """
        try:
            self.data[name].birthday = Birthday(birthday)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        except TypeError:
            raise TypeError(
                f'Format for birthday - dd.mm.YYYY, example 01.01.3333')

    def change_contact(self, old_name, new_name):
        """
        Changing <old name> to <new name> in the contact
        """
        try:
            record = self.data[old_name]
        except KeyError:
            raise ValueError(f'Contact {old_name} has not been found')

        record.name.value = new_name
        self.data.__delitem__(old_name)
        self.data.__setitem__(new_name, record)

    def change_email(self, name, email):
        """
        Changing <email> in the contact <name>
        """
        try:
            self.data[name].email = Email(email)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        except ValueError:
            raise ValueError(f'Mistake in email')

    def change_phone(self, name, old_phone, new_phone):
        """
        Changing <old phone> to <new phone> in the contact <name>
        """
        try:
            self.data[name].edit_phone(old_phone, new_phone)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')
        except ValueError:
            raise ValueError(f'Phone {old_phone} has not been found')

    def find_contact(self, key):
        """
        Find all contact with give <key>
        """
        key_all = False
        lists = []

        for name, data in self.data.items():
            key_is = False
            if key in name:
                key_is = True
            elif key in str(data.email):
                key_is = True
            elif key in data.address:
                key_is = True
            elif key in str(data.birthday):
                key_is = True
            else:
                for phone in data.phones:
                    if key in phone.value:
                        key_is = True
            key_all = key_all or key_is

            if key_is:
                lists.append(self.data[name])

        if not key_all:
            raise ValueError(f'Contacts for {key} not found')
        return lists

    def remove_address(self, name):
        """
        Deleting address from the contact
        """
        try:
            self.data[name].address = ''

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def remove_birthday(self, name):
        """
        Deleting birthday from the contact
        """
        try:
            self.data[name].birthday = ''

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def remove_contact(self, name):
        """
        Deleting contact
        """
        try:
            self.data.__delitem__(name)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def remove_email(self, name):
        """
        Deleting email from the contact
        """
        try:
            self.data[name].email = ''

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def remove_phone(self, name, phone):
        """
        Deleting <phone> from the contact
        """
        try:
            self.data[name].delete_phone(phone)

        except KeyError:
            raise ValueError(f'Contact {name} has not been found')

    def show_all_contact(self, number_on_page=None):
        """
        Printing all contacts
        """
        return self.data.values()

    def show_birthdays(self, days):
        """
        Printing all contacts who will have birthday in <days>
        """
        list_birthday = []
        for rec in self.data.values():

            if rec.birthday:
                days_to = rec.days_to_birthday()

                if days_to <= days:
                    list_birthday.append(rec)
        return list_birthday

    def show_contact(self, name):
        """
        Printing contact with given <name>
        """
        if name in self.data:
            return [self.data[name]]
        else:
            raise ValueError(
                f"Contact with the name '{name}' does not exist. Try a different name.")