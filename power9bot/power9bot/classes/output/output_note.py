from classes.output.outputInterface import OutputInterface
from shutil import get_terminal_size

class OutputNote(OutputInterface):

    def delimiter_text(self, text, length):
        idx_begin = 0
        idx_end = length
        lists = []
        while idx_begin <= len(text):
            lists.append(text[idx_begin: idx_end])
            idx_begin = idx_end
            idx_end += length
        return lists

    def output(self):
        table_width = get_terminal_size().columns - 2
        string = ''
        if not self.output_list or type(self.output_list[0]) == str:
            print('_' * table_width)
            string = "|{:^" + str(table_width - 2) + "}|"
            print(string.format('No notes'))
            print('_' * table_width)
            return True
        for note in self.output_list:
            if type(note) == tuple:
                titles = note[1].title.capitalize()
                tags = note[1].tags
                texts = note[1].text
            else:
                titles = note.title.capitalize()
                tags = note.tags
                texts = note.text
            
            print('_' * table_width)
            string = "|{:^" + str(table_width - 2) + "}|"
            print(string.format(titles))
            print('_' * table_width)
            string = "|{:^" + str(table_width - 2) + "}|"
            print(string.format(', '.join(tags)))
            print('_' * table_width)
            texts = self.delimiter_text(texts, table_width - 4)
            for text in texts:
                string = "| {:<" + str(table_width - 4) + "} |"
                print(string.format(text))
            print('_' * table_width, '\n\n')
