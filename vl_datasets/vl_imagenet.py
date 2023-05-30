# Code adapted from https://github.com/pytorch/vision/blob/main/torchvision/datasets/

from torchvision.datasets import ImageNet
from typing import Callable, Optional, Union, Sequence, Any
import pandas as pd

class VLImageNet(ImageNet):
    def __init__(self, root: str, 
                 split: str = "train", 
                 exclude_csv: Optional[str] = None, 
                 **kwargs: Any) -> None:
        

        super().__init__(root=root, split=split, **kwargs)

        if exclude_csv:
            print(f"Using provided CSV file: {exclude_csv}")
            self.exclude_df = pd.read_csv(exclude_csv, header=0)
            self.exclude_set = set(self.exclude_df["filename"].tolist())