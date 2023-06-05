from abc import ABC, abstractmethod

class Dataset(ABC):
    @abstractmethod
    def load(self, dataset_name):
        pass
    
    @abstractmethod
    def export(self, output_format):
        pass
    
    @abstractmethod
    def clean(self):
        pass