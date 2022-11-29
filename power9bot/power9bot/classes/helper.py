import os
import pickle

from classes.addressbook import AddressBook
from classes.notebook import NoteBook
from classes.output import OutputList, OutputMessage, OutputTable, OutputNote
# from classes.output import OutputTable
# from classes.output import OutputNote
from classes import FileSorting
from data.constants import COMMANDS_HELP, HEADER_ADDRESSBOOK


class Helper:
    def __init__(self):
        self.handler_command = {
            'hello': self.func_hello,
            'add contact': self.func_add_contact,
            'remove contact': self.func_remove_contact,
            'delete contact': self.func_remove_contact,
            'change contact': self.func_change_contact,
            'add address': self.func_add_address,
            'remove address': self.func_remove_address,
            'delete address': self.func_remove_address,
            'change address': self.func_change_address,
            'add email': self.func_add_email,
            'remove email': self.func_remove_email,
            'delete email': self.func_remove_email,
            'change email': self.func_change_email,
            'add birthday': self.func_add_birthday,
            'remove birthday': self.func_remove_birthday,
            'delete birthday': self.func_remove_birthday,
            'change birthday': self.func_change_birthday,
            'add phone': self.func_add_phone,
            'remove phone': self.func_remove_phone,
            'delete phone': self.func_remove_phone,
            'change phone': self.func_change_phone,
            'show all contacts': self.func_show_all_contacts,
            'show contact': self.func_show_contact,
            'show birthdays': self.func_show_birthdays,
            'find contact': self.func_find_contact,
            'add note': self.func_add_note,
            'remove note': self.func_remove_note,
            'delete note': self.func_remove_note,
            'change note': self.func_change_note,
            'add text': self.func_add_text,
            'remove text': self.func_remove_text,
            'delete text': self.func_remove_text,
            'change text': self.func_change_text,
            'add tag': self.func_add_tag,
            'remove tag': self.func_remove_tag,
            'delete tag': self.func_remove_tag,
            'change tag': self.func_change_tag,
            'show all notes': self.func_show_all_notes,
            'show note': self.func_show_note,
            'find note': self.func_find_note,
            'find tag': self.func_find_tag,
            'clear notes': self.func_clear_notes,
            'sort folder': self.func_sort_folder,
            'exit': self.func_exit,
            'close': self.func_exit,
            'goodbye': self.func_exit,
            'quit': self.func_exit,
            'help': self.func_help
        }
        self.max_length_cmd = 3
        self.sorter = None
        self.addressbook_path = os.path.join(os.path.dirname(__file__).replace('classes','data'), 'addressbook.bin')
        self.notebook_path = os.path.join(os.path.dirname(__file__).replace('classes','data'), 'notebook.bin')
        self.addressbook_load()
        self.notebook_load()

    def addressbook_load(self):
        if os.path.exists(self.addressbook_path) and os.path.isfile(self.addressbook_path) and os.stat(
                self.addressbook_path).st_size > 0:
            with open(self.addressbook_path, 'rb') as f:
                self.addressbook = pickle.load(f)
        else:
            self.addressbook = AddressBook()

    def notebook_load(self):
        if os.path.exists(self.notebook_path) and os.path.isfile(self.notebook_path) and os.stat(
                self.notebook_path).st_size > 0:
            with open(self.notebook_path, 'rb') as f:
                self.notebook = pickle.load(f)
        else:
            self.notebook = NoteBook()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        with open(self.addressbook_path, 'wb') as f:
            pickle.dump(self.addressbook, f)
        with open(self.notebook_path, 'wb') as f:
            pickle.dump(self.notebook, f)

    def check_args(self, count_args=None, more=None, text_err='Invalid number of arguments.', *args):
        args = [value for value in args if value]
        if (more == 0 and (len(args) != count_args)) or (more == 1 and (len(args) < count_args)):
            raise ValueError(text_err)

    def func_hello(self, *args):
        """
        Command: hello
        Greetings from the POWER9 bot to the USER
        """
        OutputMessage('How can I help you?').output()

    def func_exit(self):
        """
        Command: exit | close | goodbye
        Terminates the work of the POWER9 bot
        All data is saved
        """
        OutputMessage('Goodbye!').output()
        quit()

    def func_add_contact(self, name=None, *args):
        """
        Command: add contact <name>
        Creating new contact with given <name>
        <name> is a string without spaces
        """
        err = self.func_add_contact.__doc__
        self.check_args(1, 0, err, name, *args)
        self.addressbook.add_contact(name)
        OutputMessage(f'Contact {name} added to the book').output()

    def func_remove_contact(self, name=None, *args):
        """
        Command: remove | delete contact <name>
        Deleting contact with given <name>
        <name> is a string without spaces
        """
        err = self.func_remove_contact.__doc__
        self.check_args(1, 0, err, name, *args)
        self.addressbook.remove_contact(name)
        OutputMessage(f'Contact {name} removed from the book').output()

    def func_change_contact(self, name_old=None, name_new=None, *args):
        """
        Command: change contact <old name> <new name>
        Changing the name of the contact from <old name> to <new name>
        <old name> and <new name> both are strings without spaces
        """
        err = self.func_change_contact.__doc__
        self.check_args(2, 0, err, name_old, name_new, *args)
        self.addressbook.change_contact(name_old, name_new)
        OutputMessage(f"{name_old}'s contact name has been changed").output()

    def func_add_address(self, name=None, *args):
        """
        Command: add address <name> <address>
        Adding <address> to the contact with given <name>
        <name> is a string without spaces
        <address> is a string of any length
        """
        err = self.func_add_address.__doc__
        self.check_args(2, 1, err, name, *args)
        address = ' '.join(args)
        self.addressbook.add_address(name, address)
        OutputMessage(f"Address '{address}' added to {name}'s contact").output()

    def func_remove_address(self, name=None, *args):
        """
        Command: remove | delete address <name>
        Deleting address from the contact with given <name>
        <name> is a string without spaces
        """
        err = self.func_remove_address.__doc__
        self.check_args(1, 0, err, name, *args)
        self.addressbook.remove_address(name)
        OutputMessage(f"Address removed from {name}'s contact").output()

    def func_change_address(self, name=None, *args):
        """
        Command: change address <name> <address>
        Changing address in the contact with given <name>
        <name> is a string without spaces
        <address> is a string of any length
        """
        err = self.func_change_address.__doc__
        self.check_args(2, 1, err, name, *args)
        address = ' '.join(args)
        self.addressbook.change_address(name, address)
        OutputMessage(f"{name}'s contact address has been changed to '{address}'").output()

    def func_add_email(self, name=None, email=None, *args):
        """
        Command: add email <name> <email>
        Adding <email> to the contact with given <name>
        <name> and <email> both are strings without spaces
        """
        err = self.func_add_email.__doc__
        self.check_args(2, 0, err, name, email, *args)
        self.addressbook.add_email(name, email)
        OutputMessage(f"E-mail '{email}' added to {name}'s contact").output()

    def func_remove_email(self, name=None, *args):
        """
        Command: remove | delete email <name>
        Deleting email from the contact with given <name>
        <name> is a string without spaces
        """
        err = self.func_remove_email.__doc__
        self.check_args(1, 0, err, name, *args)
        self.addressbook.remove_email(name)
        OutputMessage(f"E-mail removed from {name}'s contact").output()

    def func_change_email(self, name=None, email=None, *args):
        """
        Command: change email <name> <email>
        Changing <email> in the contact with given <name>
        <name> and <email> both are strings without spaces
        """
        err = self.func_change_email.__doc__
        self.check_args(2, 0, err, name, email, *args)
        self.addressbook.change_email(name, email)
        OutputMessage(f"{name}'s contact e-mail has been changed to '{email}'").output()

    def func_add_birthday(self, name=None, birthday=None, *args):
        """
        Command: add birthday <name> <birthday>
        Adding <birthday> to the contact with given <name>
        <name> is string without spaces
        <birthday> format: dd.mm.yyyy
        """
        err = self.func_add_birthday.__doc__
        self.check_args(2, 0, err, name, birthday, *args)
        self.addressbook.add_birthday(name, birthday)
        OutputMessage(f"Date of birthday '{birthday}' added to {name}'s contact").output()

    def func_remove_birthday(self, name=None, *args):
        """
        Command: remove | delete birthday <name>
        Deleting birthday from the contact with given <name>
        <name> is string without spaces
        """
        err = self.func_remove_birthday.__doc__
        self.check_args(1, 0, err, name, *args)
        self.addressbook.remove_birthday(name)
        OutputMessage(f"Date of birthday removed from {name}'s contact").output()

    def func_change_birthday(self, name=None, birthday=None, *args):
        """
        Command: change birthday <name> <birthday>
        Changing <birthday> in the contact with given <name>
        <name> is string without spaces
        <birthday> format: dd.mm.yyyy
        """
        err = self.func_change_birthday.__doc__
        self.check_args(2, 0, err, name, birthday, *args)
        self.addressbook.change_birthday(name, birthday)
        OutputMessage(f"{name}'s contact birthday has been changed to '{birthday}'").output()

    def func_add_phone(self, name=None, phone=None, *args):
        """
        Command: add phone <name> <phone>
        Adding <phone> to the phones list of the contact with given <name>
        <name> is string without spaces
        <phone> is string without spaces, only digits as characters
        """
        err = self.func_add_phone.__doc__
        self.check_args(2, 0, err, name, phone, *args)
        self.addressbook.add_phone(name, phone)
        OutputMessage(f"Phone '{phone}' added to {name}'s contact").output()

    def func_remove_phone(self, name=None, phone=None, *args):
        """
        Command: remove | delete phone <name> <phone>
        Deleting <phone> from the phones list of the contact with given <name>
        <name> is string without spaces
        <phone> is string without spaces, only digits as characters
        """
        err = self.func_remove_phone.__doc__
        self.check_args(2, 0, err, name, phone, *args)
        self.addressbook.remove_phone(name, phone)
        OutputMessage(f"Phone '{phone}' removed from {name}'s contact").output()

    def func_change_phone(self, name=None, phone_old=None, phone_new=None, *args):
        """
        Command: changing phone <name> <old phone> <new phone>
        Changing <old phone> to <new phone> in the phones list of the contact
        with given <name>
        <name> is string without spaces
        <old phone> and <new phone> both are strings without spaces, only digits as characters
        """
        err = self.func_change_phone.__doc__
        self.check_args(3, 0, err, name, phone_old, phone_new, *args)
        self.addressbook.change_phone(name, phone_old, phone_new)
        OutputMessage(f"Contact {name}'s phone number '{phone_old}' has been changed to '{phone_new}'").output()

    def func_show_all_contacts(self):
        """
        Command: show all contact
        Printing all contacts stored by POWER9 bot
        """
        result = self.addressbook.show_all_contact()
        OutputTable(result, HEADER_ADDRESSBOOK).output()

    def func_show_contact(self, name=None, *args):
        """
        Command: show contact <name>
        Printing contact with given <name>
        <name> is string without spaces
        """
        err = self.func_show_contact.__doc__
        self.check_args(1, 0, err, name, *args)
        result = self.addressbook.show_contact(name)
        OutputTable(result, HEADER_ADDRESSBOOK).output()

    def func_find_contact(self, key='', *args):
        """
        Command: show contact <key>
        Printing contact
        <key> is string without spaces
        """
        if args:
            raise ValueError(self.func_find_contact.__doc__)
        result = self.addressbook.find_contact(key)
        OutputTable(result, HEADER_ADDRESSBOOK).output()

    def func_show_birthdays(self, days, *args):
        """
        Command: show birthdays <days>
        Printing contacts who will celebrate birthday in span <days>
        <days> is integer
        """
        if args:
            raise ValueError(self.func_show_birthdays.__doc__)
        try:
            days = int(days)
        except Exception:
            raise ValueError('Day to birthday must be number.')
        result = self.addressbook.show_birthdays(days)
        OutputTable(result, HEADER_ADDRESSBOOK).output()

    def func_add_note(self, title=None, *args):
        """
        Command: add note <title>
        Creating new note with given <title>
        <title> is a string without spaces
        """
        err = self.func_add_note.__doc__
        self.check_args(1, 0, err, title, *args)
        self.notebook.add_note(title)
        OutputMessage(f"Added note with title '{title}'").output()

    def func_remove_note(self, title=None, *args):
        """
        Command: remove | delete note <title>
        Deleting note with given <title>
        <title> is a string without spaces
        """
        err = self.func_remove_note.__doc__
        self.check_args(1, 0, err, title, *args)
        self.notebook.delete_note(title)
        OutputMessage(f"The note with the title '{title}' has been deleted").output()

    def func_change_note(self, title_old=None, title_new=None, *args):
        """
        Command: change note <old title> <new title>
        Changing <old title> to the <new title> in the note
        <old title> and <new title> both are strings without spaces
        """
        err = self.func_change_note.__doc__
        self.check_args(2, 0, err, title_old, title_new, *args)
        self.notebook.change_note(title_old, title_new)
        OutputMessage(f"'{title_old}' note has its title changed to '{title_new}'").output()

    def func_add_text(self, title=None, *args):
        """
        Command: add text <title> <text>
        Adding <text> to the note with given <title>
        <title> is string without spaces
        <text> is a string of any length
        """
        err = self.func_add_text.__doc__
        self.check_args(2, 1, err, title, *args)
        text = ' '.join(args)
        self.notebook.add_text(title, text)
        OutputMessage(f"Added text to the note titled '{title}'").output()

    def func_remove_text(self, title=None, *args):
        """
        Command: remove | delete text <title>
        Deleting <text> from the note with given <title>
        <title> is string without spaces
        """
        err = self.func_remove_text.__doc__
        self.check_args(1, 0, err, title, *args)
        self.notebook.edit_text(title, '')
        OutputMessage(f"Text removed from the note with title '{title}'").output()

    def func_change_text(self, title=None, *args):
        """
        Command: change text <title> <text>
        Changing <text> in the note with given <title>
        <title> is string without spaces
        <text> is a string of any length
        """
        err = self.func_change_text.__doc__
        self.check_args(2, 1, err, title, *args)
        text = ' '.join(args)
        self.notebook.edit_text(title, text)
        OutputMessage(f"Text changed in the note titled '{title}'").output()

    def func_add_tag(self, title=None, tag=None, *args):
        """
        Command: add tag <title> <tag>
        Adding <tag> to the note with given <title>
        <title> and <tag> both are strings without spaces
        """
        err = self.func_add_tag.__doc__
        self.check_args(2, 0, err, title, tag, *args)
        self.notebook.add_tag(title, tag)
        OutputMessage(f"Added '{tag}' to the note titled '{title}'").output()

    def func_remove_tag(self, title=None, tag=None, *args):
        """
        Command: remove | delete tag <title> <tag>
        Deleting <tag> from the note with given <title>
        <title> and <tag> both are strings without spaces
        """
        err = self.func_remove_tag.__doc__
        self.check_args(2, 0, err, title, tag, *args)
        self.notebook.remove_tag(title, tag)
        OutputMessage(f"Tag '{tag}' removed from the note with title '{title}'").output()

    def func_change_tag(self, title=None, old_tag=None, new_tag=None, *args):
        """
        Command: change tag <title> <old tag> <new tag>
        Changing <old tag> to the <new tag> in the note
        <title>, <old tag> and <new tag> are strings without spaces
        """
        err = self.func_change_tag.__doc__
        self.check_args(3, 0, err, title, old_tag, new_tag, *args)
        self.notebook.change_tag(title, old_tag, new_tag)
        OutputMessage(f"The tag '{old_tag}' has been changed to '{new_tag}' in the note titled '{title}'").output()

    def func_show_all_notes(self, flag=None, *args):
        """
        Command: show all notes {-r}
        Printing all notes stored by POWER9 bot
        {-r} is optional flag for reverse sorting
        """
        if (flag and flag != '-r') or args:
            raise ValueError(self.func_show_all_notes.__doc__)
        result = self.notebook.show_all_notes(flag)
        OutputNote(result).output()

    def func_show_note(self, title=None, *args):
        """
        Command: show note <title>
        Printing note with give <title>
        <title> is string without spaces
        """
        err = self.func_show_note.__doc__
        self.check_args(1, 0, err, title, *args)
        result = self.notebook.show_note(title)
        OutputNote(result).output()

    def func_find_note(self, key=None, flag=None, *args):
        """
        Command: find note <key> {-r}
        Printing the sorted list of notes by the given <key>
        <key> is string without spaces
        {-r} is optional flag for reverse sorting
        """
        if (flag and flag != '-r') or args:
            raise ValueError(self.func_find_note.__doc__)
        result = self.notebook.find_note_by_word(key, flag)
        OutputNote(result).output()

    def func_find_tag(self, tag=None, flag=None, *args):
        """
        Command: find note <tag> {-r}
        Printing the sorted list of notes by the given <tag>
        <tag> is string without spaces
        {-r} is optional flag for reverse sorting
        """
        if (flag and flag != '-r') or args:
            raise ValueError(self.func_find_tag.__doc__)
        result = self.notebook.find_note_by_tag(tag, flag)
        OutputNote(result).output()

    def func_clear_notes(self, *args):
        """
        Command: clear notes
        Clear all notes.
        """
        if args:
            raise ValueError(self.func_clear_notes.__doc__)
        while True:
            is_remove = input('Do you realy want remove all notes? (y / n):')
            if is_remove == 'y':
                self.notebook.clear_notes()
                break
            if is_remove == 'n':
                break
            
    def func_sort_folder(self, folder=None, *args):
        """
        Command: sort folder <path>
        Sorting folders, sub-folders and files in given <path> if path exists
        Files organised by type and moved the specific folder assign to the file type
        Empty folders will be deleted
        """
        err = self.func_sort_folder.__doc__
        self.check_args(1, 0, err, folder, *args)
        sorter = FileSorting(folder)
        sorter.sorting()

    def func_help(self, *args):
        """
        Command: help
        Print the list of commands
        """
        OutputList(COMMANDS_HELP).output()

    def handler(self, cmd):
        command = cmd.strip().split(' ')
        # same commands
        for i in range(self.max_length_cmd, 0, -1):
            if (' '.join(command[0:i]).lower()) in self.handler_command:
                return self.handler_command[' '.join(command[0:i]).lower()](*command[i:])
        # similar command
        list_cmd = set()
        # -- Levenshtein
        for el in self.handler_command:
            count = len(el.split(' '))
            for i in range(count, 0, -1):
                c = ' '.join(command[0:i]).lower()
                result = self.levenshtein(el, c) * 100 / len(el)
                if result < 40:
                    list_cmd.add(el)
        # -- rearranged words
        for element_handler in self.handler_command:
            cmd_range = element_handler.split(' ')
            founded = True
            for element_cmd in command:
                if element_cmd not in cmd_range:
                    founded = False
            if founded:
                list_cmd.add(element_handler)
        # -- same words
        for i in range(self.max_length_cmd - 1, 0, -1):
            for element in self.handler_command:
                check_cmd = ' '.join(command[0:i]).lower()
                cnt = len(element.split(' ')[0])
                if element.startswith(check_cmd[0:cnt]) or element.split(' ')[0] in check_cmd:
                    list_cmd.add(element)
                result = self.levenshtein(element.split(
                    ' ')[0], check_cmd[0:cnt]) * 100 / len(element.split(' ')[0])
                if result < 40:
                    list_cmd.add(element)
            if list_cmd:
                break
        # -- similar word
        if not list_cmd:
            pass
        if list_cmd:
            OutputMessage('Maybe you wanted to use one of this commands:').output()
            OutputList(list_cmd).output()
        else:
            raise IndexError('Command is wrong')

    def running(self):
        while True:
            cmd = input('Enter command (help - show all commands): ').lower()
            try:
                self.handler(cmd)
            except Exception as e:
                OutputMessage(e).output()

    def levenshtein(self, str_1, str_2):
        n, m = len(str_1), len(str_2)
        if n > m:
            str_1, str_2 = str_2, str_1
            n, m = m, n
        current_row = range(n + 1)
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [i] + [0] * n
            for j in range(1, n + 1):
                add, delete, change = previous_row[j] + \
                                      1, current_row[j - 1] + 1, previous_row[j - 1]
                if str_1[j - 1] != str_2[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)
        return current_row[n]
