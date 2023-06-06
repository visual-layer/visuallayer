from ..clean_torchvision_oxford_iiit_pet import CleanTorchvisionOxfordIIITPet
from ..dataset import Dataset
from dataclasses import dataclass
import pandas as pd

@dataclass
class VLOxfordIIITPet(Dataset):
    csv: str = "https://drive.google.com/uc?export=download&id=1OLa8k4NITnmCHjeByzvGaWt3W7k6R1QL"
    name: str = "vl-oxford-iiit-pets"
    description: str = "A modified version of the original Oxford IIIT Pets Dataset removing dataset issues."
    num_images: int = 7349
    
    @property
    def report(self):
        raise NotImplementedError
    
    @property
    def num_images_with_issues(self):
        df = pd.read_csv(self.csv)
        return len(df['filename'].unique())
    
    @property
    def info(self):
        print(
            f"Name:{self.name} \nDescription: {self.description} \nImages: {self.num_images} \nImages with Issues: {self.num_images_with_issues} ({self.num_images_with_issues/self.num_images*100:.2f}%)"
        )

    def export(self, output_format, root="./", split="train"):
        if output_format == "pytorch":
            print(f"Exporting dataset into {output_format}")
            return CleanTorchvisionOxfordIIITPet(root=root, split=split)
        else:
            print("Unknown output format.")
