from .vl_oxford_iiit import VLOxfordIIITPet, VLOriginalOxfordIIITPet


def load(dataset_name, variant="vl"):
    if dataset_name == "vl-oxford-iiit-pets":
        if variant == "original":
            return VLOriginalOxfordIIITPet()
        else:
            return VLOxfordIIITPet()
    else:
        raise ValueError(f"Could not find dataset. Did you mean {get_dataset_names()}?")


def list_datasets():
    names = get_dataset_names()
    print("Listing all datasets in zoo.")
    return names


def get_dataset_names():
    datasets = [VLOxfordIIITPet]
    datasets_names = [dataset.name for dataset in datasets]
    return datasets_names
