from classes.output.outputInterface import OutputInterface

class OutputList(OutputInterface):

    def output(self):
        for command in self.output_list:
            print(command)