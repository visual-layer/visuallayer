import pandas as pd
from typing import Union, List, Tuple
from dataclasses import dataclass
from functools import lru_cache


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

    @staticmethod
    @lru_cache(maxsize=None)
    def _get_csv(url: str) -> pd.DataFrame:
        """
        Downloads a CSV file from a given URL and returns it as a pandas DataFrame. The results are cached, so 
        calling the method multiple times with the same URL will not cause additional network requests.

        Args:
            url (str): The URL of the CSV file.

        Returns:
            pd.DataFrame: The data from the CSV file as a pandas DataFrame.
        """
        return pd.read_csv(url)

    @property
    def num_images_with_issues(self) -> int:
        """
        Computes the number of images with issues in the dataset. The number is calculated as the number of unique 
        entries in the "filename" column of the DataFrame obtained from the `filelist_csv_url`.

        Returns:
            int: The number of images with issues.
        """
        df = self._get_csv(self.filelist_csv_url)
        return len(df["filename"].unique())

    @property
    def info(self) -> None:
        """
        Prints the metadata information for the dataset.

        The following information is printed:
        - Name
        - Description
        - License
        - Homepage URL
        - Number of Images
        - Number of Images with Issues
        """

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
        """
        Creates a summary report for the dataset. The report is a DataFrame that contains the reason, count, and 
        percentage of issues for each type of issue in the dataset.

        Returns:
            pd.DataFrame: The report DataFrame.
        """

        print("Showing a table of issues found in the original dataset.")
        df = self._get_csv(self.issue_count_csv_url)
        df = df.loc[df["split"] == "all"].drop("split", axis=1).reset_index(drop=True)
        
        # Calculate the total sum per column
        total_count = df['count'].sum()
        total_pct = df['pct'].sum()

        # Create a DataFrame for the new row and concatenate it with the old DataFrame
        new_row = pd.DataFrame({'reason': ['Total'], 'count': [total_count], 'pct': [total_pct]})
        df = pd.concat([df, new_row], ignore_index=True)

        return df
    
    def explore(self, num_images:int = 50, issue: str ="all") -> pd.DataFrame:
        """
        Creates a DataFrame that can be used to visually explore the dataset. This DataFrame contains several columns 
        related to the images and their issues, including previews of the images.

        Returns:
            pd.DataFrame: The exploration DataFrame.
        """

        # Suppress pandas warning
        import pandas as pd
        pd.options.mode.chained_assignment = None # default='warn'

        print("For a more extensive visual exploration of the dataset visit https://app.visual-layer.com/")

        # Interactive table in jupyter notebook
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


        df = self._get_csv(self.filelist_csv_url)
        df = df[:num_images]

        # filter df with issues
        if issue != "all":
            df = df[df['reason'] == issue]


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
        """
        Exports the issue count data to a CSV file.

        Args:
            filename (str): The path where the CSV file will be saved.
        """
        df = self._get_csv(self.issue_count_csv_url)
        df.to_csv(filename, index=False)
    