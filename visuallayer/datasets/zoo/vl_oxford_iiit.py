from ..clean_torchvision_oxford_iiit_pet import CleanTorchvisionOxfordIIITPet
from ..dataset import Dataset
from dataclasses import dataclass
import pandas as pd


@dataclass
class VLOxfordIIITPet(Dataset):
    filelist_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/oxford-iiit-pet_images_issue_file_list.csv"
    issue_count_csv_url: str = "https://sharedvisuallayer.s3.us-east-2.amazonaws.com/visual-layer-sdk/oxford-iiit-pet_images_issue_count.csv"
    name: str = "vl-oxford-iiit-pets"
    description: str = "A modified version of the original Oxford IIIT Pets Dataset removing dataset issues."
    num_images: int = 7349

    @property
    def report(self):
        df = pd.read_csv(self.issue_count_csv_url)
        all_issues_df = df.loc[df["split"] == "all"]
        all_issues_df = (
            all_issues_df.loc[df["split"] == "all"]
            .drop("split", axis=1)
            .reset_index(drop=True)
        )

        print(
            f"Visual Layer Profiler found and removed the following issues from the original dataset and removed them in {self.name}\n"
        )

        # print issues to user
        for _, row in all_issues_df.iterrows():
            reason = row["reason"]
            count = row["count"]
            pct = row["pct"]

            output = f"{count:,} {reason} ({pct:.1f}%)"
            print(output)

        print(
            "\nTo explore the full data and the issues head to http://visual-layer.com/datasets/dataset/1234-5678-abcd"
        )

    @property
    def num_images_with_issues(self):
        df = pd.read_csv(self.filelist_csv_url)
        return len(df["filename"].unique())

    @property
    def info(self):
        print(
            f"Name:{self.name} \nDescription: {self.description} \nImages: {self.num_images} \nImages with Issues: {self.num_images_with_issues} ({self.num_images_with_issues/self.num_images*100:.2f}%)"
        )

    def export(self, output_format, root="./", split="train"):
        if output_format == "pytorch":
            print(f"Exporting dataset into {output_format}")
            return CleanTorchvisionOxfordIIITPet(root=root, split=split)
        else:
            print("Unknown output format.")

    def export_issues(self, filename):
        df = pd.read_csv(self.filelist_csv_url)
        df.to_csv(filename)