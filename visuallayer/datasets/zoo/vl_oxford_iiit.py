from ..clean_torchvision_oxford_iiit_pet import CleanTorchvisionOxfordIIITPet
from ..dataset import Dataset
from dataclasses import dataclass

@dataclass
class VLOxfordIIITPet(Dataset):
    name: str = "vl-pets"
    description: str = "A modified version of the original Oxford IIIT Pets Dataset removing dataset issues."

    @property
    def report(self):
        print("Listing all issues from csv")

    @property
    def info(self):
        return {"name": self.name, "description": self.description}
    
    def export(self, output_format, root='./', split='train'):
        if output_format == "pytorch":
            print(f"Exporting dataset into {output_format}")
            return CleanTorchvisionOxfordIIITPet(root=root, split=split)