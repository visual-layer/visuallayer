from ..clean_torchvision_oxford_iiit_pet import CleanTorchvisionOxfordIIITPet
from ..dataset import Dataset
from dataclasses import dataclass
import pandas as pd
from torchvision.datasets import OxfordIIITPet
from typing import Union, List, Tuple

@dataclass(frozen=True)
class VLOxfordIIITPet(Dataset):
    name: str = "vl-oxford-iiit-pets"
    homepage_url: str = "https://www.robots.ox.ac.uk/~vgg/data/pets/"
    license: str = "Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)"
    description: str = "A modified version of the original Oxford IIIT Pets Dataset removing dataset issues."
    num_images: int = 7349
    filelist_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/oxford-iiit-pet_images_issue_file_list.csv"
    issue_count_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/oxford-iiit-pet_images_issue_count.csv"
    exclude_csv: str = None

    # Hack: Download the dataset in the current dir
    def __post_init__(self):
        OxfordIIITPet(root="./", download=True)

    def export(
        self,
        output_format: str,
        variation: str = "vl",
        root: str = "./",
        split: str = "train",
    ):
        if output_format == "pytorch":
            if variation == "vl":
                print(
                    f"Exporting {variation.upper()} dataset into {output_format} dataset."
                )
                return CleanTorchvisionOxfordIIITPet(root=root, split=split, exclude_csv=self.exclude_csv)
            elif variation == "original":
                print(
                    f"Exporting {variation.upper()} dataset into {output_format} dataset."
                )
                return OxfordIIITPet(root=root, split=split, download=True)
        
        elif output_format == "csv":
            if variation == "vl":
                print(
                    f"Exporting {variation.upper()} dataset into {output_format} dataset."
                )
                dataset = CleanTorchvisionOxfordIIITPet(root=root, split=split, exclude_csv=self.exclude_csv)
                samples = {"Image": dataset._images, "Label": dataset._labels}
                df = pd.DataFrame(samples)
                return df
            elif variation == "original":
                print(
                    f"Exporting {variation.upper()} dataset into {output_format} dataset."
                )
                dataset = OxfordIIITPet(root=root, split=split, download=True)
                samples = {"Image": dataset._images, "Label": dataset._labels}
                df = pd.DataFrame(samples)
                return df

        else:
            raise ValueError(
                f"Unknown output format: {output_format} or variation {variation}."
            )

@dataclass(frozen=True)
class VLOriginalOxfordIIITPet(VLOxfordIIITPet):
    name: str = "oxford-iiit-pets"
    description: str = "The original pets dataset by Oxford IIIT."
