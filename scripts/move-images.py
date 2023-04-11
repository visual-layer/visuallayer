import argparse
import csv
import shutil
from pathlib import Path

def move_images_to_folder(file_paths_csv: Path, images_dir: Path, dest_folder_name: str = "problem_images") -> None:
    """
    Moves problematic images to a destination folder for further analysis.

    Parameters:
    file_paths_csv (Path): A Path object representing the CSV file containing the list of file paths.
    images_dir (Path): A Path object representing the directory where the images are located.
    dest_folder_name (str): The name of the destination folder. Default is "problem_images".

    Returns:
    None
    """
    corrupted_images_dir = Path(dest_folder_name)
    corrupted_images_dir.mkdir(exist_ok=True)  # create the directory if it doesn't exist

    with open(file_paths_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            file_path = row[0]
            path = images_dir / Path(file_path)
            if path.is_file():
                new_path = corrupted_images_dir / Path(file_path)
                new_path.parent.mkdir(parents=True, exist_ok=True)  # create the parent directory if it doesn't exist
                print(f"Moving {path} to {new_path}")
                shutil.move(str(path), str(new_path))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Move problematic images to a destination folder for further analysis.')
    parser.add_argument('--file_paths_csv', type=str, help='The CSV file containing the list of file paths.')
    parser.add_argument('--images_dir', type=str, help='The directory where the images are located.')
    parser.add_argument('--dest_folder_name', type=str, default='problem_images', help='The name of the destination folder. Default is "problem_images".')
    args = parser.parse_args()

    file_paths_csv = Path(args.file_paths_csv)
    images_dir = Path(args.images_dir)
    dest_folder_name = args.dest_folder_name

    move_images_to_folder(file_paths_csv, images_dir, dest_folder_name)
