import re
from classes.addressbook.field import Field


class Email(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):

        pattern = r"[^@]+@[^@]+\.[^@]+"

        if not re.match(pattern, value):
            raise ValueError('You tried to enter incorrect e-mail. Please try again')

        self.__value = value
