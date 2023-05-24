# Code adapted from https://github.com/pytorch/vision/blob/main/torchvision/datasets/

from torchvision.datasets import Food101
from typing import Callable, Optional
import json
import pandas as pd
import requests
import torchvision.transforms as transforms
from vl_datasets.sentry import v1_sentry_handler, vl_capture_log_debug_state


train_transform = transforms.Compose(
    [
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)

valid_transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


class VLFood101(Food101):
    @v1_sentry_handler
    def __init__(
        self,
        root: str,
        split: str = "train",
        transform: Optional[Callable] = None,
        target_transform: Optional[Callable] = None,
        download: bool = True,
        exclude_csv: Optional[str] = None,
    ) -> None:
        vl_capture_log_debug_state(locals())

        super().__init__(
            root,
            split=split,
            transform=transform,
            target_transform=target_transform,
            download=download,
        )

        with open(self._meta_folder / f"{split}.json") as f:
            metadata = json.loads(f.read())

        self.classes = sorted(metadata.keys())
        self.class_to_idx = dict(zip(self.classes, range(len(self.classes))))

        # Default tranform
        if transform is None:
            if split == "train":
                self.transform = train_transform

            elif split == "test":
                self.transform = valid_transform

        # If user specifies a csv file use it
        if exclude_csv:
            print(f"Using provided CSV file: {exclude_csv}")
            self.exclude_df = pd.read_csv(exclude_csv, header=0)
            self.exclude_set = set(self.exclude_df["filename"].tolist())

        # Otherwise, download the csv file
        elif exclude_csv is None:
            print("Downloading CSV file")
            url = "https://drive.google.com/uc?export=download&id=1QaaNJif3qWC_AsOEugnnBASySZO0cLjW"
            filename = "food-101.csv"

            try:
                response = requests.get(url, stream=True)
                with open(filename, "wb") as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        f.write(chunk)

                self.exclude_df = pd.read_csv(filename, header=0)
                self.exclude_set = set(self.exclude_df["filename"].tolist())

            except Exception as e:
                print("Error parsing CSV file")
                print(e)

        # A copy of self.exclude_set but without file extension
        exclude_set_filenames = {
            filename.split("/")[-2] + "/" + filename.split("/")[-1].split(".")[0]
            for filename in self.exclude_set
        }

        self._labels = []
        self._image_files = []
        self.excluded_files = []
        for class_label, im_rel_paths in metadata.items():
            for im_rel_path in im_rel_paths:
                if f"{im_rel_path}" in exclude_set_filenames:
                    print(f"Excluding {im_rel_path}.jpg from the {split} set")
                    self.excluded_files.append(f"{im_rel_path}.jpg")
                    continue
                self._labels += [self.class_to_idx[class_label]]
                self._image_files += [
                    self._images_folder.joinpath(*f"{im_rel_path}.jpg".split("/"))
                ]
