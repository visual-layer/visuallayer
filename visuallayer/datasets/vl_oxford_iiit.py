from .clean_torchvision_oxford_iiit_pet import CleanTorchvisionOxfordIIITPet
from .dataset import Dataset

class VLOxfordIIITPet(Dataset):
    @property
    def info(self):
        return {"name": "Oxford IIIT Pets",
                "description": "The Oxford-IIIT pet dataset comprises 37 categories of pet images, with approximately 200 images per class. The dataset exhibits significant variations in scale, pose, and lighting. Each image is accompanied by a ground truth annotation indicating the breed."} 
    
    def export(self, output_format, root='./', split='train'):
        if output_format == "pytorch":
            print(f"Exporting dataset into {output_format}")
            return CleanTorchvisionOxfordIIITPet(root=root, split=split)