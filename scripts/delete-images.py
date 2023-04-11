from pathlib import Path
from typing import List

def delete_images(file_paths: List[str], images_dir: Path) -> None:
    """
    Deletes problematic images given a list of file paths.

    Parameters:
    file_paths (List[str]): A list of file paths.
    images_dir (Path): The directory where the images are located.

    Returns:
    None
    """
    for file_path in file_paths:
        path = images_dir / Path(file_path)
        if path.is_file():
            print(f"Deleting {path}")
            path.unlink()
