from classes.addressbook.field import Field


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):

        if not value.isnumeric():
            raise ValueError('Please for input phone use only number')

        self.__value = value
