from abc import ABC, abstractmethod

class Dataset(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @property
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def report(self):
        pass

    @abstractmethod
    def export(self, output_format):
        pass

    