import torch
from torch.utils.data import Dataset
import os
from PIL import Image

class UIDataset(Dataset):
    def __init__(self, root_dir, processor=None):
        self.root_dir = root_dir
        self.processor = processor
        self.image_paths = []

        for label in os.listdir(self.root_dir):
            subdir_path = os.path.join(self.root_dir, label)
            if os.path.isdir(subdir_path):
                for filename in os.listdir(subdir_path):
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')):
                        file_path = os.path.join(subdir_path, filename)
                        self.image_paths.append((file_path, label))  

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, index):
        file_path, label = self.image_paths[index]

        image = Image.open(file_path).convert("RGB")  

        if self.processor:
            inputs = self.processor(images=image, return_tensors="pt")
            image_tensor = inputs["pixel_values"].squeeze(0)  
            
        
        return image_tensor, label
