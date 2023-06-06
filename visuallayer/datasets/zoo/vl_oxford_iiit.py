from ..clean_torchvision_oxford_iiit_pet import CleanTorchvisionOxfordIIITPet
from ..dataset import Dataset
from dataclasses import dataclass
import pandas as pd
from torchvision.datasets import OxfordIIITPet


@dataclass
class VLOxfordIIITPet(Dataset):
    filelist_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/oxford-iiit-pet_images_issue_file_list.csv"
    issue_count_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/oxford-iiit-pet_images_issue_count.csv"
    name: str = "vl-oxford-iiit-pets"
    homepage_url: str = "https://www.robots.ox.ac.uk/~vgg/data/pets/"
    license: str = (
        "Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)"
    )
    description: str = "A modified version of the original Oxford IIIT Pets Dataset removing dataset issues."
    num_images: int = 7349
    variant: str = "vl"

    # If the class is instantiated with the original flag, change the name property.
    # def __post_init__(self):
    #     if self.variant == "original":
    #         self.name = "oxford-iiit-pets"

    @property
    def report(self):
        df = pd.read_csv(self.issue_count_csv_url)
        all_issues_df = df.loc[df["split"] == "all"]
        all_issues_df = (
            all_issues_df.loc[df["split"] == "all"]
            .drop("split", axis=1)
            .reset_index(drop=True)
        )

        print(f"Visual Layer Profiler issues in this dataset:\n")

        # print issues to user
        for _, row in all_issues_df.iterrows():
            reason = row["reason"]
            count = row["count"]
            pct = row["pct"]

            output = f"--> {count:,} {reason.upper()}(S) ({pct:.2f}%)"
            print(output)

        print(
            "\nThese images are removed in the `vl` variant of the dataset. To load the original version of the dataset, use variant=`original`. Explore the full data and the issues head to http://visual-layer.com/datasets/dataset/1234-5678-abcd"
        )

    @property
    def num_images_with_issues(self):
        df = pd.read_csv(self.filelist_csv_url)
        return len(df["filename"].unique())

    @property
    def info(self):
        # Get all attributes and methods of the class
        dataset_metadata = [
            ("Name", self.name),
            ("Description", self.description),
            ("License", self.license),
            ("Homepage URL", self.homepage_url),
            ("Number of Images", self.num_images),
            ("Number of Images with Issues", self.num_images_with_issues),
        ]

        if self.variant == "original":
            dataset_metadata = [
                ("Name", "oxford-iiit-pets"),
                ("Description", "The original pets dataset by Oxford IIIT."),
                ("License", self.license),
                ("Homepage URL", self.homepage_url),
                ("Number of Images", self.num_images),
            ]

        print("Metadata:")
        for metadata in dataset_metadata:
            print(f"--> {metadata[0]} - {metadata[1]}")

    def export(self, output_format, variant="vl", root="./", split="train"):
        if output_format == "pytorch" and variant == "vl":
            print(f"Exporting {variant.upper()} dataset into {output_format} dataset.")
            return CleanTorchvisionOxfordIIITPet(root=root, split=split)
        elif variant == "original":
            print(f"Exporting {variant.upper()} dataset into {output_format} dataset.")
            return OxfordIIITPet(root=root, split=split, download=True)
        else:
            raise ValueError(
                f"Unknown output format: {output_format} or variant {variant}"
            )

    def export_issues(self, filename):
        df = pd.read_csv(self.issue_count_csv_url)
        df.to_csv(filename, index=False)
