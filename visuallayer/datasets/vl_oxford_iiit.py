from .clean_torchvision_oxford_iiit_pet import CleanTorchvisionOxfordIIITPet
from .dataset import Dataset

class VLOxfordIIITPet(Dataset):
    def load(self, dataset_name):
        print(f"Loading {dataset_name}")
    
    def export(self, output_format, root='./'):
        if output_format == "pytorch":
            print(f"Exporting dataset into {output_format}")
            return CleanTorchvisionOxfordIIITPet(root=root)
    def clean(self):
        print(f"Getting clean version of the dataset")