"""
A torchvision dataset object for Kitti dataset
Used for filtering original dataset using the VL-Datasets analysis CSV
"""
import torch.utils.data
import torchvision
import pandas as pd
from typing import Any, Callable, List, Optional, Tuple

from vl_datasets.sentry import v1_sentry_handler
from vl_parse_exclude_csv import parse_exclude_csv

COCO_CSV_URL = "https://drive.google.com/u/0/uc?id=1D8Or_bOLQEPAxrTwHrrKTzYO3GaHeH7H&export=download"
COCO_CSV_FILENAME = "Coco_objects_issue_file_list.csv"


class VLCocoDetection(torchvision.datasets.CocoDetection):
    @v1_sentry_handler
    def __init__(
            self,
            root: str,
            annFile: str,
            transform: Optional[Callable] = None,
            target_transform: Optional[Callable] = None,
            transforms: Optional[Callable] = None,
            exclude_csv: Optional[str] = None,
    ):
        super().__init__(
            root,
            annFile=annFile,
            transform=transform,
            target_transform=target_transform,
            transforms=transforms,
        )

        original_image_count = len(self.coco.dataset['images'])
        original_annotation_count = len(self.coco.dataset['annotations'])

        self.exclude_df, self.exclude_set = parse_exclude_csv(exclude_csv, COCO_CSV_URL, COCO_CSV_FILENAME)

        # Removing redundant images:
        # 1. Get image ids to remove
        exclude_filename_set = set(o.split('/')[-1] for o in self.exclude_set)
        img_ids_to_remove = [img['id'] for img in self.coco.dataset['images']
                             if img['file_name'] in exclude_filename_set]

        # 2. Remove image ids
        self.coco.imgs = {k: v for k, v in self.coco.imgs.items() if k not in img_ids_to_remove}
        self.coco.dataset['images'] = [img for img in self.coco.dataset['images']
                                       if img['id'] not in img_ids_to_remove]

        # 3. Remove annotatios for bad image ids
        self.coco.dataset['annotations'] = [ann for ann in self.coco.dataset['annotations']
                                            if ann['image_id'] not in img_ids_to_remove]

        current_image_count = len(self.coco.dataset['images'])
        print(f"Removed {len(self.exclude_set)} out of {original_image_count} images.\n"
              f"{current_image_count} images, ({100 * current_image_count / original_image_count:.2f}%) remain.")

        current_annotations_count = len(self.coco.dataset['annotations'])
        print(f"Removed {original_annotation_count - current_annotations_count} out of {original_annotation_count} annotations.\n"
              f"{current_annotations_count} annotations, ({100 * current_annotations_count / original_annotation_count:.2f}%) remain.")
