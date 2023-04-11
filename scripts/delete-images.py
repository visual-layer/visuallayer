import argparse
from pathlib import Path
from typing import List

def delete_images(file_paths_csv: Path, images_dir: Path) -> None:
    """
    Deletes problematic images based on a list of file paths.

    Parameters:
    file_paths_csv (Path): A Path object representing the CSV file containing the list of file paths.
    images_dir (Path): A Path object representing the directory where the images are located.

    Returns:
    None
    """
    with open(file_paths_csv, newline='') as csvfile:
        for row in csvfile:
            file_path = row.strip()
            path = images_dir / Path(file_path)
            if path.is_file():
                print(f"Deleting {path}")
                path.unlink()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Deletes problematic images based on a list of file paths.')
    parser.add_argument('--file_paths_csv', type=str, help='The CSV file containing the list of file paths.')
    parser.add_argument('--images_dir', type=str, help='The directory where the images are located.')
    args = parser.parse_args()

    file_paths_csv = Path(args.file_paths_csv)
    images_dir = Path(args.images_dir)

    delete_images(file_paths_csv, images_dir)
