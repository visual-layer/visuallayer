from ..clean_torchvision_food101 import CleanTorchvisionFood101
from ..dataset import Dataset
from dataclasses import dataclass
from torchvision.datasets import Food101

@dataclass(frozen=True)
class VLFood101(Dataset):
    name: str = "vl-food101"
    homepage_url: str = "https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/"
    license: str = "Unknown"
    description: str = "A challenging data set of 101 food categories is introduced, consisting of 101,000 images."
    num_images: int = 101000
    filelist_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/food101_images_issue_file_list.csv"
    issue_count_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/food101_images_issue_count.csv"
    exclude_csv: str = None

    # Hack: Download the dataset in the current dir
    def __post_init__(self):
        Food101(root="./", download=True)