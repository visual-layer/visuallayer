# Code adapted from https://github.com/pytorch/vision/blob/main/torchvision/datasets/

from torchvision.datasets import ImageNet
from typing import Optional, Any, Tuple
import pandas as pd

class VLImageNet(ImageNet):
    def __init__(self, root: str, 
                 split: str = "train", 
                 exclude_csv: Optional[str] = None, 
                 **kwargs: Any) -> None:
        

        super().__init__(root=root, split=split, **kwargs)
        
        self.exclude_df, self.exclude_set = parse_exclude_csv(exclude_csv)

        # Filter file lists based on VL CSV files
        # Extract filenames from samples
        filenames = {sample[0].split("/")[-1] for sample in self.samples}

        # Remove filenames found in exclude_set
        filtered_filenames = filenames - self.exclude_set

        # Create the filtered_list by filtering tuples_list based on the filtered_filenames
        filtered_samples = [(filename, label) for filename, label in self.samples if filename.split("/")[-1] in filtered_filenames]
        filtered_targets = [s[1] for s in filtered_samples]

        self.samples = filtered_samples
        self.targets = filtered_targets
        

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