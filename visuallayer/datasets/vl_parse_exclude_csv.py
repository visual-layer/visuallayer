from typing import Tuple
import pandas as pd


def parse_exclude_csv(exclude_csv_arg: str,
                      url: str,
                      filename: str) -> Tuple[pd.DataFrame, set]:
    if exclude_csv_arg:
        print(f"Using provided CSV file: {exclude_csv_arg}")
        exclude_df = pd.read_csv(exclude_csv_arg, header=0)
        exclude_set = set(exclude_df["filename"].tolist())

        # Otherwise, download the csv file
    elif exclude_csv_arg is None:
        import requests
        print("Downloading CSV file")
        try:
            response = requests.get(url, stream=True)
            with open(filename, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)

            exclude_df = pd.read_csv(filename, header=0)
            exclude_set = set(exclude_df["filename"].tolist())

        except Exception as e:
            print(f"Error parsing CSV file; {repr(e)}")
            exclude_df = pd.DataFrame()
            exclude_set = set()
    else:
        exclude_df = pd.DataFrame()
        exclude_set = set()

    return exclude_df, exclude_set
