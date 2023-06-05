from .vl_oxford_iiit import VLOxfordIIITPet

def load(dataset_name):
    print("Loading dataset here")
    if dataset_name == 'pets':
        return VLOxfordIIITPet()