"""
A torchvision dataset object for Kitti dataset
Used for filtering original dataset using the VL-Datasets analysis CSV
"""

from typing import Any, Callable, List, Optional, Tuple
import torchvision
import pandas as pd
from visuallayer.sentry import v1_sentry_handler


KITTI_CSV_PATH = "https://drive.google.com/u/0/uc?id=1P6YWOLwGQQ2777v6KA3qvhicznFXsaoQ&export=download"
KITTI_CSV_FILENAME = "Kitti_objects_issue_file_list.csv"


class CleanTorchvisionKitti(torchvision.datasets.Kitti):
    """
    A class inheriting the torchvision Kitti dataset and applying the findings of
    a VL Cleanup.
    V0 - Images containing objects affected with issues are removed
    TBD: Ignore flags and corrections for affected objects.

    Additional parameters:
    :param exclude_csv: Optional. A CSV file listing dataset issues, used for selecting images for removal.
    """
    @v1_sentry_handler
    def __init__(
        self,
        root: str,
        train: bool = True,
        transform: Optional[Callable] = None,
        target_transform: Optional[Callable] = None,
        transforms: Optional[Callable] = None,
        download: bool = False,
        exclude_csv: Optional[str] = None,
    ):
        super().__init__(
            root,
            train=train,
            transform=transform,
            target_transform=target_transform,
            transforms=transforms,
            download=download,
        )
        original_len = len(self)
        # Parse exclude CSV
        # If user specifies a csv file use it
        self.exclude_df, self.exclude_set = parse_exclude_csv(exclude_csv)

        # Filter file lists based on VL CSV files
        image_keep_list = [i for i, o in enumerate(self.images) if not o.endswith(tuple(self.exclude_set))]
        self.images = [self.images[i] for i in image_keep_list]
        self.targets = [self.targets[i] for i in image_keep_list]

        # Print stats
        print(f"Removed {len(self.exclude_set)} out of {original_len} images.\n"
              f"{len(self.images)} images, ({100 * len(self.images) / original_len:.2f}%) remain")


def parse_exclude_csv(exclude_csv_arg: str,
                      url: str = KITTI_CSV_PATH,
                      filename: str = KITTI_CSV_FILENAME) -> Tuple[pd.DataFrame, set]:
    if exclude_csv_arg:
        print(f"Using provided CSV file: {exclude_csv_arg}")
        exclude_df = pd.read_csv(exclude_csv_arg, header=0)
        exclude_set = set(exclude_df["filename"].tolist())

        # Otherwise, download the csv file
    elif exclude_csv_arg is None:
        import requests
        print("Downloading CSV file")
        try:
            response = requests.get(url, stream=True)
            with open(filename, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)

            exclude_df = pd.read_csv(filename, header=0)
            exclude_set = set(exclude_df["filename"].tolist())

        except Exception as e:
            print(f"Error parsing CSV file; {repr(e)}")
            exclude_df = pd.DataFrame()
            exclude_set = set()
    else:
        exclude_df = pd.DataFrame()
        exclude_set = set()

    return exclude_df, exclude_set


if __name__ == '__main__':
    dataset = CleanTorchvisionKitti('/home/ubuntu/data/vl_data/kitti/', train=True, download=True)  #, exclude_csv=KITTI_CSV_FILENAME)
    a = dataset[3]
    pass