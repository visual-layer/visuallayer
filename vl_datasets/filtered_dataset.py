from torchvision.datasets import ImageFolder
import pandas as pd
from pathlib import Path

class FilteredDataset(ImageFolder):
    """
    A modified version of torchvision.datasets.ImageFolder that filters out samples whose filenames
    are listed in a given CSV file.

    See: https://pytorch.org/vision/main/generated/torchvision.datasets.ImageFolder.html

    Args:
        root_dir (string): Root directory path of the dataset.
        csv_path (string, optional): Path to a CSV file containing a list of excluded filenames.
                                     Default: None.
        transform (callable, optional): A function/transform that takes in a PIL image and returns a
                                         transformed version. E.g, ``transforms.RandomCrop``
                                         Default: None.
        target_transform (callable, optional): A function/transform that takes in the target and
                                                transforms it. Default: None.

    Example usage:

        # Load the dataset and exclude certain samples
        dataset = FilteredDataset("dataset/images", "files-to-exclude.csv", transform=transforms.ToTensor())

        # Create a dataloader
        dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
    """

    def __init__(self, root_dir, csv_path=None, transform=None, target_transform=None):
        root_dir = Path(root_dir)
        super().__init__(root_dir, transform=transform, target_transform=target_transform)

        if csv_path:
            self.excluded_files = pd.read_csv(csv_path, header=0)
            self.excluded_files['filename'] = self.excluded_files['filename'].apply(lambda x: str(root_dir) + "/" + x )
            self.excluded_filenames = set(self.excluded_files['filename'])
 
            print(f"Original Samples: {len(self.samples)} in {root_dir}")
            print(f"Excluded: {len(self.excluded_filenames)} in {root_dir}")
            excluded_indices = [i for i, (path, _) in enumerate(self.samples) if path in self.excluded_filenames]
            self.samples = [sample for i, sample in enumerate(self.samples) if i not in excluded_indices]
            self.targets = [target for i, target in enumerate(self.targets) if i not in excluded_indices]
            print(f"Cleaned Samples: {len(self.samples)} in {root_dir}")