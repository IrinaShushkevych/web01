from datetime import datetime
from power9bot.classes.name import Name
from power9bot.classes.phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = ''
        self.address = ''
        self.email = ''

    def __str__(self):
        str_name = f'| Name {self.name.value} |'
        str_phone = f'| Phone:{", ".join([phone.value for phone in self.phones])} |'
        str_birthday = f'| birthday: {str(self.birthday)} |'
        str_email = f'| E-mail: {str(self.email)}  |'
        str_address = f'| Address: {self.address} |'
        return f'{str_name}{str_phone}{str_birthday}{str_email}{str_address}'

    def add_new_phone(self, phone_new):

        self.phones.append(Phone(phone_new))

    def delete_phone(self, old_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        self.delete_phone(old_phone)
        self.phones.append(Phone(new_phone))

    def days_to_birthday(self):
        current_date = datetime.now()
        try:
            next_birthday = datetime(
                year=current_date.year, month=self.birthday.value.month, day=self.birthday.value.day)
        except ValueError:
            next_birthday = datetime(
                year=current_date.year, month=self.birthday.value.month, day=self.birthday.value.day-1)

        if next_birthday < current_date:
            try:
                next_birthday = datetime(
                    year=current_date.year+1, month=self.birthday.value.month, day=self.birthday.value.day)
            except ValueError:
                next_birthday = datetime(
                    year=current_date.year+1, month=self.birthday.value.month, day=self.birthday.value.day-1)

        return (next_birthday-current_date).days
