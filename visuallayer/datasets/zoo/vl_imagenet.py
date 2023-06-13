from dataclasses import dataclass
from ..dataset import Dataset
from ..clean_torchvision_imagenet import CleanTorchvisionImageNet
from torchvision.datasets import ImageNet
import pandas as pd

@dataclass(frozen=True)
class VLImageNet1k(Dataset):
    root: str = "./"
    name: str = "vl-imagenet-1k"
    homepage_url: str = "https://www.image-net.org/"
    license: str = "Unknown"
    description: str = "A modified version of the original ImageNet-1k dataset removing dataset issues."
    num_images: int = 1431167
    filelist_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/ImageNet-1K_images_issue_file_list.csv"
    issue_count_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/ImageNet-1K_images_issue_count.csv"

    def export(
        self,
        output_format: str,
        variation: str = "vl",
        split: str = "train",
    ):
        if output_format == "pytorch":
            if variation == "vl":
                print(
                    f"Exporting {variation.upper()} dataset into {output_format} dataset."
                )
                return CleanTorchvisionImageNet(root=self.root, split=split, exclude_csv=self.filelist_csv_url)
            elif variation == "original":
                print(
                    f"Exporting {variation.upper()} dataset into {output_format} dataset."
                )
                return ImageNet(root=self.root, split=split)
        
        elif output_format == "csv":
            if variation == "vl":
                print(
                    f"Exporting {variation.upper()} dataset into {output_format} dataset."
                )
                dataset = CleanTorchvisionImageNet(root=self.root, split=split, exclude_csv=self.filelist_csv_url)
                samples = {"Image": dataset._images, "Label": dataset._labels}
                df = pd.DataFrame(samples)
                return df
            elif variation == "original":
                print(
                    f"Exporting {variation.upper()} dataset into {output_format} dataset."
                )
                dataset = ImageNet(root=self.root, split=split)
                samples = {"Image": dataset._images, "Label": dataset._labels}
                df = pd.DataFrame(samples)
                return df

        else:
            raise ValueError(
                f"Unknown output format: {output_format} or variation {variation}."
            )

    # TODO - fix me. Does not work because directory from csv file is different from what is expected locally in ImageFolder form. Also check self.root
    def explore(self):
        raise NotImplementedError


@dataclass(frozen=True)
class VLOriginalImageNet1k(VLImageNet1k):
    name: str = "imagenet-1k"
    description: str = "The original imagenet-1k dataset."


@dataclass(frozen=True)
class VLImageNet21k(VLImageNet1k):
    root: str = "./"
    name: str = "vl-imagenet-21k"
    homepage_url: str = "https://github.com/Alibaba-MIIL/ImageNet21K"
    license: str = "Unknown"
    description: str = "A modified version of the original ImageNet-21k dataset removing dataset issues."
    num_images: int = 13153500
    filelist_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/ImageNet-21K_images_issue_file_list.csv"
    issue_count_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/ImageNet-21K_images_issue_count.csv"

@dataclass(frozen=True)
class VLOriginalImageNet21k(VLImageNet21k):
    name: str = "imagenet-21k"
    description: str = "The original imagenet-21k dataset."