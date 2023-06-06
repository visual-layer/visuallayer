from abc import ABC, abstractmethod

class Dataset(ABC):

    @property
    @abstractmethod
    def csv(self):
        pass

    @property
    @abstractmethod
    def num_images(self):
        pass

    @property
    @abstractmethod
    def num_images_with_issues(self):
        pass

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

    