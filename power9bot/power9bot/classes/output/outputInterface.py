from abc import ABC, abstractmethod

class OutputInterface(ABC):
    def __init__(self, output_list):
        self.output_list = output_list

    @abstractmethod
    def output(self):
        pass