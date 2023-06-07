from ..clean_torchvision_oxford_iiit_pet import CleanTorchvisionOxfordIIITPet
from ..dataset import Dataset
from dataclasses import dataclass
import pandas as pd
from torchvision.datasets import OxfordIIITPet
from typing import Union, List, Tuple
from itables import init_notebook_mode

init_notebook_mode(all_interactive=True)


@dataclass(frozen=True)
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

    # Hack: Download the dataset in the current dir
    def __post_init__(self):
        OxfordIIITPet(root="./", download=True)

    @property
    def num_images_with_issues(self) -> int:
        df = pd.read_csv(self.filelist_csv_url)
        return len(df["filename"].unique())

    @property
    def info(self) -> None:
        # Get all attributes and methods of the class
        dataset_metadata: List[Tuple[str, Union[str, int]]] = [
            ("Name", self.name),
            ("Description", self.description),
            ("License", self.license),
            ("Homepage URL", self.homepage_url),
            ("Number of Images", self.num_images),
            ("Number of Images with Issues", self.num_images_with_issues),
        ]

        print("Metadata:")
        for metadata in dataset_metadata:
            print(f"--> {metadata[0]} - {metadata[1]}")

    @property
    def report(self) -> pd.DataFrame:
        df = pd.read_csv(self.issue_count_csv_url)
        df = df.loc[df["split"] == "all"].drop("split", axis=1).reset_index(drop=True)
        
        # Calculate the total sum per column
        total_count = df['count'].sum()
        total_pct = df['pct'].sum()

        # Create a DataFrame for the new row and concatenate it with the old DataFrame
        new_row = pd.DataFrame({'reason': ['Total'], 'count': [total_count], 'pct': [total_pct]})
        df = pd.concat([df, new_row], ignore_index=True)

        return df


        # print(f"Visual Layer Profiler issues in this dataset:\n")

        # print issues to user
        # for _, row in all_issues_df.iterrows():
        #     reason: str = row["reason"]
        #     count: int = row["count"]
        #     pct: float = row["pct"]

        #     output: str = f"--> {count:,} {reason.upper()}(S) ({pct:.2f}%)"
        #     print(output)

        # print(
        #     "\nThese images are removed in the `vl` variant of the dataset. To load the original version of the dataset, use variant=`original`. Explore the full data and the issues head to http://visual-layer.com/datasets/dataset/1234-5678-abcd"
        # )

    def export(
        self,
        output_format: str,
        variant: str = "vl",
        root: str = "./",
        split: str = "train",
    ):
        if output_format == "pytorch":
            if variant == "vl":
                print(
                    f"Exporting {variant.upper()} dataset into {output_format} dataset."
                )
                return CleanTorchvisionOxfordIIITPet(root=root, split=split)
            elif variant == "original":
                print(
                    f"Exporting {variant.upper()} dataset into {output_format} dataset."
                )
                return OxfordIIITPet(root=root, split=split, download=True)
        
        elif output_format == "csv":
            if variant == "vl":
                print(
                    f"Exporting {variant.upper()} dataset into {output_format} dataset."
                )
                dataset = CleanTorchvisionOxfordIIITPet(root=root, split=split)
                samples = {"Image": dataset._images, "Label": dataset._labels}
                df = pd.DataFrame(samples)
                return df
            elif variant == "original":
                print(
                    f"Exporting {variant.upper()} dataset into {output_format} dataset."
                )
                dataset = OxfordIIITPet(root=root, split=split, download=True)
                samples = {"Image": dataset._images, "Label": dataset._labels}
                df = pd.DataFrame(samples)
                return df

        else:
            raise ValueError(
                f"Unknown output format: {output_format} or variant {variant}."
            )

    def export_issues(self, filename: str) -> None:
        df = pd.read_csv(self.issue_count_csv_url)
        df.to_csv(filename, index=False)

    def explore(self) -> pd.DataFrame:
        import base64

        def to_img_tag(path):
            if isinstance(path, str):
                with open(path, 'rb') as f:
                    image_data = f.read()
                    base64_image = base64.b64encode(image_data).decode('utf-8')
                return '<img src="data:image/png;base64,' + base64_image + '" width="150" >'
            else:
                return path  # Return the original value if it's not a string


        df = pd.read_csv(self.filelist_csv_url)
        df["filename_preview"] = df["filename"]
        df["prototype_preview"] = df["prototype"]
        df = df.loc[
            :,
            [
                "filename",
                "filename_preview",
                "reason",
                "value",
                "prototype",
                "prototype_preview",
            ],
        ]
        df["filename_preview"] = df["filename"].apply(to_img_tag)
        df["prototype_preview"] = df["prototype"].apply(to_img_tag)

        return df


@dataclass(frozen=True)
class VLOriginalOxfordIIITPet(VLOxfordIIITPet):
    name: str = "oxford-iiit-pets"
    description: str = "The original pets dataset by Oxford IIIT."
