from collections import UserDict
from shutil import get_terminal_size


def check_title(func):
    def inner(self, *args):
        flag = self.data.get(args[0], None)
        if flag:
            return func(self, *args)
        raise IndexError('Wrong title, try something else!')
    return inner


class NoteBook(UserDict):
    def add_note(self, title):
        flag = self.data.get(title, None)
        if not flag:
            self.data[title] = Note(title)
        else:
            raise IndexError('This title is already exist')

    def clear_notes(self):
        self.data.clear()

    def show_note(self, title):
        self.print_notes([self.data.get(title, 'This note doesnt exist')])

    def show_all_notes(self, flag=None):
        flag = True if flag == '-r' else False
        count = 0
        constant_number = 5
        data_new = sorted(list(self.data.values()),
                          key=lambda x: x.title.lower(), reverse=flag)
        while count < len(data_new):
            self.print_notes(data_new[count:count + constant_number])
            if len(data_new[count + constant_number + 1:]) == 0:
                break
            user_input = input('Press any button or ''exit''')
            if user_input.lower() == 'exit':
                break
            else:
                count += constant_number

    def find_note_by_word(self, word, flag=None):
        flag = True if flag == '-r' else False
        result = [note for title, note in self.data.items()
                  if word.lower() in title.lower() or word.lower() in note.text.lower()]
        self.print_notes(sorted(result, key=lambda x: x.title.lower(), reverse=flag))

    def find_note_by_tag(self, tag, flag=None):
        flag = True if flag == '-r' else False
        result = [note for note in self.data.values() if tag.lower() in [
            x.lower() for x in note.tags]]
        # print(sorted(result, key=lambda x: x.title.lower(), reverse=flag))
        self.print_notes(sorted(result, key=lambda x: x.title.lower(), reverse=flag))

    @check_title
    def delete_note(self, title):
        self.data.pop(title)

    @check_title
    def edit_text(self, title, new_text):
        self.data[title].text = new_text

    @check_title
    def add_text(self, title, new_words):
        if self.data[title].text:
            self.data[title].text += ' ' + new_words
        else:
            self.data[title].text = new_words

    @check_title
    def add_tag(self, title, new_tag):
        existing_tags = [x.lower() for x in self.data[title].tags]
        if new_tag.lower() not in existing_tags:
            self.data[title].tags.append(new_tag)
        else:
            raise ValueError('This tag is exist')

    @check_title
    def remove_tag(self, title, target_tag):
        result = ''.join(list(filter(lambda x: target_tag.lower()
                                     == x.lower(), self.data[title].tags)))
        if result:
            self.data[title].tags.remove(result)
        else:
            raise ValueError('This tag doesnt exist!')

    @check_title
    def change_tag(self, title, old_tag, new_tag):
        result = ''.join(list(filter(lambda x: old_tag.lower()
                                     == x.lower(), self.data[title].tags)))
        if result:
            self.data[title].tags.remove(result)
            self.data[title].tags.append(new_tag)
        else:
            raise ValueError('This tag doesnt exist!')

    @check_title
    def change_note(self, old_title, new_title):
        self.data[new_title] = self.data.pop(old_title)
        self.data[new_title].title = new_title

    def delimiter_text(self, text, length):
        idx_begin = 0
        idx_end = length
        lists = []
        while idx_begin <= len(text):
            lists.append(text[idx_begin: idx_end])
            idx_begin = idx_end
            idx_end += length
        return lists

    def print_notes(self, notes=[]):
        table_width = get_terminal_size().columns - 2
        string = ''
        if not notes or type(notes[0]) == str:
            print('-' * table_width)
            string = "|{:^" + str(table_width - 2) + "}|"
            print(string.format('No notes'))
            print('-' * table_width)
            return True
        for note in notes:
            if type(note) == tuple:
                titles = note[1].title.capitalize()
                tags = note[1].tags
                texts = note[1].text
            else:
                titles = note.title.capitalize()
                tags = note.tags
                texts = note.text
            print('-' * table_width)
            string = "|{:^" + str(table_width - 2) + "}|"
            print(string.format(titles))
            print('-' * table_width)
            string = "|{:^" + str(table_width - 2) + "}|"
            print(string.format(', '.join(tags)))
            print('-' * table_width)
            texts = self.delimiter_text(texts, table_width - 4)
            for text in texts:
                string = "| {:<" + str(table_width - 4) + "} |"
                print(string.format(text))
            print('-' * table_width, '\n\n')


class Note:
    def __init__(self, title):
        self.title = title
        self.text = ''
        self.tags = []

    def __repr__(self):
        return f'| Title: {self.title} : Text: {self.text} : Tags: {self.tags} |'
