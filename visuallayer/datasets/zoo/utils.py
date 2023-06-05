from .vl_oxford_iiit import VLOxfordIIITPet

def load(dataset_name):
    print("Loading dataset here")
    if dataset_name == 'Oxford IIIT Pets':
        return VLOxfordIIITPet()
    
def list_datasets():
    datasets = [VLOxfordIIITPet()]
    names = [dataset.name for dataset in datasets]
    print("Listing all datasets in zoo.")
    return names
