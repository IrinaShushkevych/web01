from collections import UserDict
from power9bot.classes.birthday import Birthday
from power9bot.classes.email import Email
from power9bot.classes.record import Record
from shutil import get_terminal_size


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
        self.print_contacts_head()
        key_all = False

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
                self.print_contacts([self.data[name]])

        if not key_all:
            raise ValueError(f'Contacts for {key} not found')

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
        if not number_on_page:
            number_on_page = 3

        stock = self.iterator()
        page = 1
        self.print_contacts_head()
        while True:
            try:
                for _ in range(number_on_page):
                    self.print_contacts([next(stock)])

                page += 1
            except StopIteration:
                break

    def show_birthdays(self, days):
        """
        Printing all contacts who will have birthday in <days>
        """
        list_birthday = []
        self.print_contacts_head()
        for rec in self.data.values():

            if rec.birthday:
                days_to = rec.days_to_birthday()

                if days_to <= days:
                    list_birthday.append(rec)
        self.print_contacts(list_birthday)

    def show_contact(self, name):
        """
        Printing contact with given <name>
        """
        self.print_contacts_head()
        if name in self.data:
            self.print_contacts([self.data[name]])
        else:
            raise ValueError(
                f"Contact with the name '{name}' does not exist. Try a different name.")

    def delimiter_text(self, text, length):
        idx_begin = 0
        idx_end = length
        lists = []
        while idx_begin <= len(text):
            lists.append(text[idx_begin: idx_end])
            idx_begin = idx_end
            idx_end += length
        return lists

    def print_contacts_head(self):
        columns = ['Name', 'Address', 'Email', 'Birthday', 'Phones']
        table_width = get_terminal_size().columns - 3
        column_width = (get_terminal_size().columns - 2) // 5 - 1
        print('-' * table_width)
        print_string = '|'
        for _ in columns:
            print_string += ' {:^' + str(column_width - 2) + '} |'
        print(print_string.format(*columns))
        print('-' * table_width)

    def print_contacts(self, contacts=[]):
        columns = ['Name', 'Address', 'Email', 'Birthday', 'Phones']
        table_width = get_terminal_size().columns - 3
        column_width = (get_terminal_size().columns - 2) // 5 - 1
        print_string = '|'
        for _ in columns:
            print_string += ' {:^' + str(column_width - 2) + '} |'
        for contact in contacts:
            cnt_rows = 0
            name = self.delimiter_text(str(contact.name).capitalize(), column_width - 2)
            if len(name) > cnt_rows:
                cnt_rows = len(name)
            address = self.delimiter_text(contact.address, column_width - 2)
            if len(address) > cnt_rows:
                cnt_rows = len(address)
            email = self.delimiter_text(str(contact.email), column_width - 2)
            if len(email) > cnt_rows:
                cnt_rows = len(email)
            birthday = self.delimiter_text(str(contact.birthday), column_width - 2)
            if len(birthday) > cnt_rows:
                cnt_rows = len(birthday)
            phones = []
            for phone in contact.phones:
                if phone:
                    phones.append(phone.value)
            phones = phones if phones else ['']
            for i in range(cnt_rows):
                name_print = name[i] if i < len(name) else ''
                address_print = address[i] if i < len(address) else ''
                email_print = email[i] if i < len(email) else ''
                birthday_print = birthday[i] if i < len(birthday) else ''
                phones_print = phones[i] if i < len(phones) else ''
                print(print_string.format(
                    name_print,
                    address_print,
                    email_print,
                    birthday_print,
                    phones_print
                ))
            print('-' * table_width)
