from abc import ABC, abstractmethod

class Dataset(ABC):
    @property
    @abstractmethod
    def info():
        pass

    @abstractmethod
    def export(self, output_format):
        pass

    