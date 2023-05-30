# Code adapted from https://github.com/pytorch/vision/blob/main/torchvision/datasets/

from torchvision.datasets import ImageNet
from typing import Callable, Optional, Union, Sequence, Any, Tuple
import pandas as pd

class VLImageNet(ImageNet):
    def __init__(self, root: str, 
                 split: str = "train", 
                 exclude_csv: Optional[str] = None, 
                 **kwargs: Any) -> None:
        

        super().__init__(root=root, split=split **kwargs)
        
        self.exclude_df, self.exclude_set = parse_exclude_csv(exclude_csv)

        # Filter file lists based on VL CSV files
        # TODO: use more efficient method. This takes too long. Sets subtraction maybe?
        image_keep_list = [i for i, (filename, class_num) in enumerate(self.samples) if not filename.endswith(tuple(self.exclude_set))]

        self.samples = [self.samples[i] for i in image_keep_list]
        self.targets = [self.targets[i] for i in image_keep_list]
        

def parse_exclude_csv(exclude_csv_arg: str) -> Tuple[pd.DataFrame, set]:
    
    if exclude_csv_arg:
        print(f"Using provided CSV file: {exclude_csv_arg}")
        exclude_df = pd.read_csv(exclude_csv_arg, header=0)
        # Strip additional dir name and only use filenames.
        exclude_df['filename'] = exclude_df['filename'].str.replace('imagenet1k/', '')
        exclude_df['prototype'] = exclude_df['prototype'].str.replace('imagenet1k/', '')
        exclude_set = set(exclude_df["filename"].tolist())

    else:
        print("CSV not provided, using original version of ImageNet")
        exclude_df = pd.DataFrame()
        exclude_set = set()

    return exclude_df, exclude_set