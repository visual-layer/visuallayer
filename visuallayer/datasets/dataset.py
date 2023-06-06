from abc import ABC, abstractmethod

class Dataset(ABC):

    @property
    @abstractmethod
    def filelist_csv_url(self):
        pass

    @property
    @abstractmethod
    def issue_count_csv_url(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def homepage_url(self):
        pass

    @property
    @abstractmethod
    def license(self):
        pass

    @property
    @abstractmethod
    def description(self):
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
    def info(self):
        pass

    @abstractmethod
    def report(self):
        pass

    @abstractmethod
    def export(self, output_format):
        pass

    @abstractmethod
    def export_issues(self, filename):
        pass
    