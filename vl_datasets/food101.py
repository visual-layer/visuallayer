# Code adapted from https://github.com/pytorch/vision/blob/main/torchvision/datasets/utils.py

from torchvision.datasets import Food101
from typing import Any, Callable, Optional, Tuple, TypeVar, Iterable
from pathlib import Path
import json
import pandas as pd

class CleanFood101(Food101):
    def __init__(
        self,
        root: str,
        split: str = "train",
        transform: Optional[Callable] = None,
        target_transform: Optional[Callable] = None,
        download: bool = True,
        exclude_csv: Optional[str] = None
    ) -> None:
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

        if exclude_csv:
            self.exclude_df = pd.read_csv(exclude_csv, header=0)
            self.exclude_set = set(self.exclude_df["filename"].tolist())

        self.excluded_files = []
        for class_label, im_rel_paths in metadata.items():
            for im_rel_path in im_rel_paths:
                if exclude_csv is not None and f"{im_rel_path}.jpg" in self.exclude_set:
                    # print(f"Excluding {im_rel_path}.jpg")
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
