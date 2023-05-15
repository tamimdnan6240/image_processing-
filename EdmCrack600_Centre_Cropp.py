#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torchvision.transforms as transforms
from torchvision.utils import save_image
import cv2 
from matplotlib import pyplot as plt
import numpy as np
from torchvision import transforms, models
import matplotlib.image as mpimg 
from PIL import Image
import numpy as np
from numpy import asarray
import glob
import os


# In[ ]:


# we define a python file for our convenicences to make some operations
from image_msk_Load_rotate_display__resize_CenterCrop_RadndoFlipping import Load_Image, centerCrop, display_images


# In[ ]:


cropped_images =  ("D:\\SPRING 2023\\MS_Thesis\\MASTER'S THESIS\\EdmCrack600\\dataset-EdmCrack600\\cropped_images")
cropped_masks =   ("D:\\SPRING 2023\\MS_Thesis\\MASTER'S THESIS\\EdmCrack600\\dataset-EdmCrack600\\cropped_masks")

##create save image directory
if not os.path.exists(cropped_images):
    os.mkdir(cropped_images)

## create mask directory
if not os.path.exists(cropped_masks):
    os.mkdir(cropped_masks)
    
## program for saving the images, 
def save_img(img, msk): 
    img = Image.fromarray(img)
    msk = Image.fromarray(msk)
    os.path.join(cropped_images, img)
    os.path.join(cropped_masks, msk)


# In[ ]:


## load_images 
images = glob.glob("D:\\SPRING 2023\\MS_Thesis\\MASTER'S THESIS\\EdmCrack600\\dataset-EdmCrack600\\images/*png")
images 


# In[ ]:


masks = glob.glob("D:\\SPRING 2023\\MS_Thesis\\MASTER'S THESIS\\EdmCrack600\\dataset-EdmCrack600\\annotations/*png")
masks


# In[ ]:


import os
from PIL import Image

# Define the paths for the directories
base_dir = "D:\\SPRING 2023\\MS_Thesis\\MASTER'S THESIS\\EdmCrack600\\dataset-EdmCrack600\\"
image_dir = os.path.join(base_dir, "images")
mask_dir = os.path.join(base_dir, "annotations")
cropped_images_dir = os.path.join(base_dir, "cropped_images")
cropped_masks_dir = os.path.join(base_dir, "cropped_masks")

# Create directories if they don't exist
os.makedirs(cropped_images_dir, exist_ok=True)
os.makedirs(cropped_masks_dir, exist_ok=True)

# Get a list of image and mask files
image_files = [file for file in os.listdir(image_dir) if file.endswith('.jpg') or file.endswith('.png')]
mask_files = [file for file in os.listdir(mask_dir) if file.endswith('.jpg') or file.endswith('.png')]

for image_file, mask_file in zip(image_files, mask_files):
    image_path = os.path.join(image_dir, image_file)
    mask_path = os.path.join(mask_dir, mask_file)
    
    # Open the image and mask
    image = Image.open(image_path)
    image = np.array(image)
    mask = Image.open(mask_path)
    mask = np.array(mask)

    # Perform the center crop
    cropped_image, cropped_mask = centerCrop(image, mask, (512, 512))
    cropped_image = Image.fromarray(cropped_image)
    cropped_mask = Image.fromarray(cropped_mask)
    
    # Save the cropped images and masks
    cropped_image_path = os.path.join(cropped_images_dir, image_file)
    cropped_mask_path = os.path.join(cropped_masks_dir, mask_file)
    cropped_image.save(cropped_image_path)
    cropped_mask.save(cropped_mask_path)
    
    # Display the images if needed
    print(display_images(cropped_image, cropped_mask))


# In[ ]:





# In[ ]:




