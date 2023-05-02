from torchvision.datasets import Places365
from typing import Any, Callable, Optional, Tuple, TypeVar, Iterable, List
from pathlib import Path
from os import path
import os
import json
import pandas as pd

class CleanPlaces365(Places365):
    def __init__(self, 
                 root: str, 
                 split: str = "train-standard", 
                 small: bool = False, 
                 download: bool = True, 
                 exclude_csv: Optional[str] = None,
                 transform: Callable[..., Any] | None = None, 
                 target_transform: Callable[..., Any] | None = None, 
                 loader: Callable[[str], Any] = ...) -> None:
        super().__init__(root, split, small, download, transform, target_transform, loader)

        self.exclude_csv = exclude_csv
        self.exclude_set = set()

        self.split = self._verify_split(split)
        self.small = small
        self.loader = loader

        self.classes, self.class_to_idx = self.load_categories(download)
        self.imgs, self.targets = self.load_files(download)
        
    def load_files(self, download: bool = True):
        if self.exclude_csv:
            self.exclude_df = pd.read_csv(self.exclude_csv, header=0)
            self.exclude_set = set(self.exclude_df["filename"].tolist())

        def process(line: str, sep="/") -> Tuple[str, int]:
            image, idx = line.split()
            return path.join(self.images_dir, image.lstrip(sep).replace(sep, os.sep)), int(idx)
        
        file, md5 = self._FILE_LIST_META[self.split]
        file = path.join(self.root, file)
        if not self._check_integrity(file, md5, download):
            self.download_devkit()

        images = []
        with open(file) as fh:
            for line in fh:
                image_data = process(line)
                if image_data[0] in self.exclude_set:
                    print(f"Excluded image {image_data}")
                    continue
                images.append(image_data)


        _, targets = zip(*images)
        return images, list(targets)
        
