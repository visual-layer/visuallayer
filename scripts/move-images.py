import shutil
from pathlib import Path
from typing import List

def move_images_to_folder(file_paths: List[str], images_dir: Path, dest_folder_name: str = "problematic_images") -> None:
    """
    Moves problematic images to a destination folder for further analysis.

    Parameters:
    file_paths (List[str]): A list of file paths.
    images_dir (Path): The directory where the images are located.
    dest_folder_name (str): The name of the destination folder. Default is "problematic_images".

    Returns:
    None
    """
    corrupted_images_dir = Path(dest_folder_name)
    corrupted_images_dir.mkdir(exist_ok=True)  # create the directory if it doesn't exist

    for file_path in file_paths:
        path = images_dir / Path(file_path)
        if path.is_file():
            new_path = corrupted_images_dir / Path(file_path)
            new_path.parent.mkdir(parents=True, exist_ok=True)  # create the parent directory if it doesn't exist
            print(f"Moving {path} to {new_path}")
            shutil.move(str(path), str(new_path))
