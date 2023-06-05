from .vl_oxford_iiit import VLOxfordIIITPet

def load(dataset_name):
    print("Loading dataset here")
    if dataset_name == 'Oxford IIIT Pets':
        return VLOxfordIIITPet()
    
def list_dataset():
    datasets = [VLOxfordIIITPet()]

    names = []
    for dataset in datasets:
        names.append(dataset.name)

    print("Listing all datasets in zoo.")
    print(names)
