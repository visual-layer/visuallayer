from .vl_oxford_iiit import VLOxfordIIITPet, VLOriginalOxfordIIITPet
from .vl_food101 import VLFood101, VLOriginalFood101
from .vl_imagenet import VLImageNet1k, VLOriginalImageNet1k, VLImageNet21k, VLOriginalImageNet21k

dataset = {
    "vl-oxford-iiit-pets": VLOxfordIIITPet,
    "oxford-iiit-pets": VLOriginalOxfordIIITPet,
    "vl-food101": VLFood101,
    "food101": VLOriginalFood101,
    "vl-imagenet-1k": VLImageNet1k,
    "imagenet-1k": VLOriginalImageNet1k,
    "vl-imagenet-21k": VLImageNet21k,
    "imagenet-21k": VLOriginalImageNet21k
}


def load(dataset_name: str):
    loaded_dataset = dataset.get(dataset_name, CombinationError)
    return loaded_dataset()

def list_datasets():
    names = _get_dataset_names()
    print("Listing all datasets in the zoo.")
    sorted_names = list(sorted(names))
    reversed_list = sorted_names[::-1]
    return reversed_list 

def _get_dataset_names():
    dataset_names = [key for key in dataset.keys()]
    return set(dataset_names)


class CombinationError:
    def __init__(self):
        raise NotImplementedError("This dataset and variation combination is not implemented.")
