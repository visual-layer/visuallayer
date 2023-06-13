import pandas as pd
from typing import Union, List, Tuple
from dataclasses import dataclass

@dataclass(frozen=True)
class Dataset:
    root: str
    name: str
    homepage_url: str 
    license: str 
    description: str 
    num_images: int 
    filelist_csv_url: str 
    issue_count_csv_url: str

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
    
    def explore(self) -> pd.DataFrame:
        import base64
        from itables import init_notebook_mode
        init_notebook_mode(all_interactive=True)

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

    def export_issues(self, filename: str) -> None:
        df = pd.read_csv(self.issue_count_csv_url)
        df.to_csv(filename, index=False)
    