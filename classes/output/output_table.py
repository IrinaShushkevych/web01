from classes.output.outputInterface import OutputInterface
from shutil import get_terminal_size

class OutputTable(OutputInterface):
    def __init__(self, output_list, header_list):
        super().__init__(output_list)
        self.header_list = header_list

    def delimiter_text(self, text, length):
        idx_begin = 0
        idx_end = length
        lists = []
        while idx_begin <= len(text):
            lists.append(text[idx_begin: idx_end])
            idx_begin = idx_end
            idx_end += length
        return lists

    def print_table_head(self):
        table_width = get_terminal_size().columns - 3
        column_width = (get_terminal_size().columns - 2) // len(self.header_list) - 1
        print('_' * table_width)
        print_string = '|'
        for _ in self.header_list:
            print_string += ' {:^' + str(column_width - 2) + '} |'
        print(print_string.format(*self.header_list.values()))
        print('_' * table_width)

    def print_table(self):
        table_width = get_terminal_size().columns - 3
        column_width = (get_terminal_size().columns - 2) // len(self.header_list) - 1
        print_string = '|'
        for _ in self.header_list:
            print_string += ' {:^' + str(column_width - 2) + '} |'
        for contact in self.output_list:
            cnt_rows = 0
            print_list = []
            for col_name in self.header_list.keys():
                if not isinstance(contact[col_name.lower()], list):
                    value = self.delimiter_text(str(contact[col_name.lower()]).capitalize(), column_width - 2) 
                else:
                    value = []
                    for el in contact[col_name.lower()]:
                        if el:
                            value.append(el.value)
                    value = value if value else ['']
                print_list.append(value)
                if len(value) > cnt_rows:
                    cnt_rows = len(value)
            for i in range(cnt_rows):
                list_row = []
                for j in range(len(print_list)):
                    list_row.append(print_list[j][i] if i < len(print_list[j]) else '')
                print(print_string.format(*list_row))
            print('_' * table_width)
            
    def output(self):
        self.print_table_head()
        self.print_table()