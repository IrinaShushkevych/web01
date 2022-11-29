from datetime import datetime
from classes.addressbook.field import Field


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):

        date_format = '%d.%m.%Y'

        try:
            date_birthday = datetime.strptime(value, date_format)
            self.__value = date_birthday

        except TypeError:

            raise TypeError(
                "Incorrect data format for birthday, should be DD.MM.YYYY")

    def __str__(self):
        return datetime.strftime(self.__value, '%d.%m.%Y')
