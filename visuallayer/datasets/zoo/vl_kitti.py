import pandas as pd
from ..dataset import Dataset
from dataclasses import dataclass
from torchvision.datasets import Kitti

@dataclass(frozen=True)
class VLKitti(Dataset):
    root: str = './'
    name: str = "vl-kitti"
    homepage_url: str = "https://www.cvlibs.net/datasets/kitti/"
    license: str = "Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0)"
    description: str = "A modified version of the original KITTI Dataset removing dataset issues."
    num_images: int = 12919
    filelist_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/Kitti_images_issue_file_list.csv"
    issue_count_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/Kitti_images_issue_count.csv"


    # Hack: Download the dataset in root dir
    def __post_init__(self):
        Kitti(root=self.root, download=True)

    def export(self,
               output_format: str,
               variation: str = "vl",
               split: str = "train",):
        raise NotImplementedError



@dataclass(frozen=True)
class VLOriginalKitti(VLKitti):
    name: str = "kitti"
    description: str = "The original KITTI dataset."
