from torchvision.datasets import OxfordIIITPet
import pathlib
from typing import Callable, Optional, Union, Sequence
from .utils import verify_str_arg
from torchvision.datasets.vision import StandardTransform
import pandas as pd
import requests
import torchvision.transforms as transforms


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


class CleanOxfordIIITPet(OxfordIIITPet):
    def __init__(
        self,
        root: str,
        split: str = "trainval",
        target_types: Union[Sequence[str], str] = "category",
        transforms: Optional[Callable] = None,
        transform: Optional[Callable] = None,
        target_transform: Optional[Callable] = None,
        exclude_csv: Optional[str] = None,
        download: bool = False,
    ):
        self._split = verify_str_arg(split, "split", ("trainval", "test"))
        if isinstance(target_types, str):
            target_types = [target_types]
        self._target_types = [
            verify_str_arg(target_type, "target_types", self._VALID_TARGET_TYPES)
            for target_type in target_types
        ]

        super().__init__(
            root,
            transforms=transforms,
            transform=transform,
            target_transform=target_transform,
        )

        self._base_folder = pathlib.Path(self.root) / "oxford-iiit-pet"
        self._images_folder = self._base_folder / "images"
        self._anns_folder = self._base_folder / "annotations"
        self._segs_folder = self._anns_folder / "trimaps"

        if download:
            self._download()

        if not self._check_exists():
            raise RuntimeError(
                "Dataset not found. You can use download=True to download it"
            )

        # # Default tranform
        if transform is None:
            if split == "trainval":
                print("Apply default transform")
                self.transform = train_transform

            elif split == "test":
                self.transform = valid_transform

            self.transforms = StandardTransform(self.transform, self.target_transform)

        if exclude_csv:
            print(f"Using provided CSV file: {exclude_csv}")
            self.exclude_df = pd.read_csv(exclude_csv, header=0)
            self.exclude_set = set(self.exclude_df["filename"].tolist())

        elif exclude_csv is None:
            print("Downloading CSV file")
            url = "https://drive.google.com/uc?export=download&id=1OLa8k4NITnmCHjeByzvGaWt3W7k6R1QL"
            filename = "oxford-pets.csv"

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

        image_ids = []
        self._labels = []

        # A copy of self.exclude_set but without file extension
        exclude_set_filenames = {
            filename.split(".")[0] for filename in self.exclude_set
        }

        with open(self._anns_folder / f"{self._split}.txt") as file:
            for line in file:
                image_id, label, *_ = line.strip().split()

                # if filename found in exclude set continue
                if image_id in exclude_set_filenames:
                    print(f"Excluded {image_id} from the {split} set")
                    continue

                image_ids.append(image_id)
                self._labels.append(int(label) - 1)

        self.classes = [
            " ".join(part.title() for part in raw_cls.split("_"))
            for raw_cls, _ in sorted(
                {
                    (image_id.rsplit("_", 1)[0], label)
                    for image_id, label in zip(image_ids, self._labels)
                },
                key=lambda image_id_and_label: image_id_and_label[1],
            )
        ]
        self.class_to_idx = dict(zip(self.classes, range(len(self.classes))))

        self._images = [
            self._images_folder / f"{image_id}.jpg" for image_id in image_ids
        ]
        self._segs = [self._segs_folder / f"{image_id}.png" for image_id in image_ids]
