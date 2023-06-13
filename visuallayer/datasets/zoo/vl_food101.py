from ..clean_torchvision_food101 import CleanTorchvisionFood101
from ..dataset import Dataset
from dataclasses import dataclass
import pandas as pd
from torchvision.datasets import Food101
from typing import Union, List, Tuple

@dataclass(frozen=True)
class VLFood101(Dataset):
    root: str = './'
    name: str = "vl-food101"
    homepage_url: str = "https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/"
    license: str = "Unknown"
    description: str = "A modified version of the original Food101 Dataset removing dataset issues."
    num_images: int = 101000
    filelist_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/food101_images_issue_file_list.csv"
    issue_count_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/food101_images_issue_count.csv"
    exclude_csv: str = None

    # Hack: Download the dataset in root dir
    def __post_init__(self):
        Food101(root=self.root, download=True)
    
    def export(
        self,
        output_format: str,
        variation: str = "vl",
        split: str = "train",
    ):
        if output_format == "pytorch":
            if variation == "vl":
                print(
                    f"Exporting {variation.upper()} dataset into {output_format} dataset."
                )
                return CleanTorchvisionFood101(root=self.root, split=split, exclude_csv=self.exclude_csv)
            elif variation == "original":
                print(
                    f"Exporting {variation.upper()} dataset into {output_format} dataset."
                )
                return Food101(root=self.root, split=split, download=True)
        
        elif output_format == "csv":
            if variation == "vl":
                print(
                    f"Exporting {variation.upper()} dataset into {output_format} dataset."
                )
                dataset = CleanTorchvisionFood101(root=self.root, split=split, exclude_csv=self.exclude_csv)
                samples = {"Image": dataset._images, "Label": dataset._labels}
                df = pd.DataFrame(samples)
                return df
            elif variation == "original":
                print(
                    f"Exporting {variation.upper()} dataset into {output_format} dataset."
                )
                dataset = Food101(root=self.root, split=split, download=True)
                samples = {"Image": dataset._images, "Label": dataset._labels}
                df = pd.DataFrame(samples)
                return df

        else:
            raise ValueError(
                f"Unknown output format: {output_format} or variation {variation}."
            )

@dataclass(frozen=True)
class VLOriginalFood101(VLFood101):
    name: str = "food101"
    description: str = "The original food101 dataset."