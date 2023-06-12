from .vl_oxford_iiit import VLOxfordIIITPet, VLOriginalOxfordIIITPet
from .vl_food101 import VLFood101, VLOriginalFood101

dataset = {
    ("vl-oxford-iiit-pets", "vl"): VLOxfordIIITPet,
    ("vl-oxford-iiit-pets", "original"): VLOriginalOxfordIIITPet,
    ("vl-food101", "vl"): VLFood101,
    ("vl-food101", "original"): VLOriginalFood101,
}


def load(dataset_name: str, variation: str = "vl"):
    loaded_dataset = dataset.get((dataset_name, variation), CombinationError)
    return loaded_dataset()


def list_datasets():
    names = _get_dataset_names()
    print("Listing all datasets in zoo.")
    return list(names)

def _get_dataset_names():
    dataset_names = [key[0] for key in dataset.keys()]
    return set(dataset_names)


class CombinationError:
    def __init__(self):
        raise NotImplementedError(
            "This dataset and variation combination is not implemented."
        )
