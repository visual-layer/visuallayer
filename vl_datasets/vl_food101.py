# Code adapted from https://github.com/pytorch/vision/blob/main/torchvision/datasets/utils.py

from torchvision.datasets import Food101
from typing import Any, Callable, Optional, TypeVar, Iterable
from pathlib import Path
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
        exclude_csv: Optional[str] = None
    ) -> None:
        vl_capture_log_debug_state(locals())
        super().__init__(root, transform=transform, target_transform=target_transform, download=download)
        self._split = verify_str_arg(split, "split", ("train", "test"))
        self._base_folder = Path(self.root) / "food-101"
        self._meta_folder = self._base_folder / "meta"
        self._images_folder = self._base_folder / "images"

        if not self._check_exists():
            raise RuntimeError("Dataset not found. You can use download=True to download it")

        self._labels = []
        self._image_files = []
        with open(self._meta_folder / f"{split}.json") as f:
            metadata = json.loads(f.read())

        self.classes = sorted(metadata.keys())
        self.class_to_idx = dict(zip(self.classes, range(len(self.classes))))

        # Default tranform
        if transform is None:
            if split == 'train':
                self.transform = train_transform

            elif split == 'test':
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
            filename.split("/")[-2] + "/" + filename.split("/")[-1].split(".")[0] for filename in self.exclude_set
        }

        self.excluded_files = []
        for class_label, im_rel_paths in metadata.items():
            for im_rel_path in im_rel_paths:
                if f"{im_rel_path}" in exclude_set_filenames:
                    print(f"Excluding {im_rel_path}.jpg")
                    self.excluded_files.append(f"{im_rel_path}.jpg")
                    continue
                self._labels += [self.class_to_idx[class_label]]
                self._image_files += [self._images_folder.joinpath(*f"{im_rel_path}.jpg".split("/"))]

        print(f"Excluded {len(self.excluded_files)} from the {split} set")


T = TypeVar("T", str, bytes)

def iterable_to_str(iterable: Iterable) -> str:
    return "'" + "', '".join([str(item) for item in iterable]) + "'"

def verify_str_arg(
    value: T,
    arg: Optional[str] = None,
    valid_values: Optional[Iterable[T]] = None,
    custom_msg: Optional[str] = None,
) -> T:
    if not isinstance(value, str):
        if arg is None:
            msg = "Expected type str, but got type {type}."
        else:
            msg = "Expected type str for argument {arg}, but got type {type}."
        msg = msg.format(type=type(value), arg=arg)
        raise ValueError(msg)

    if valid_values is None:
        return value

    if value not in valid_values:
        if custom_msg is not None:
            msg = custom_msg
        else:
            msg = "Unknown value '{value}' for argument {arg}. Valid values are {{{valid_values}}}."
            msg = msg.format(value=value, arg=arg, valid_values=iterable_to_str(valid_values))
        raise ValueError(msg)

    return 
