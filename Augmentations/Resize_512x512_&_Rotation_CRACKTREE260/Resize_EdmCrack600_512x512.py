#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torchvision
import torch
device = torch.device("cpu")
device

## do this first otherwise Kerner will die


# In[2]:


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


# In[3]:


import os
from PIL import Image

# set the input directory containing the images
input_folder = "D:\\SPRING 2023\\MS_Thesis\\MASTER'S THESIS\\EdmCrack600\\dataset-EdmCrack600\\images"

# set the output directory for the resized images
output_folder = "D:\\SPRING 2023\\MS_Thesis\\MASTER'S THESIS\\EdmCrack600\\dataset-EdmCrack600\\resized_image"

# set the desired output size
output_size = (512, 512)

# create the output directory if it does not exist
os.makedirs(output_folder, exist_ok=True)

# loop through each image in the input directory
for image_name in os.listdir(input_folder):
    # read the image
    image_path = os.path.join(input_folder, image_name)
    image = Image.open(image_path)
    
    # resize the image to the desired output size
    image_resized = image.resize(output_size)
    
    # save the resized image to the output directory with a new filename
    output_name = f"resized_{image_name}"
    output_path = os.path.join(output_folder, output_name)
    image_resized.save(output_path)


# In[4]:


import os
from PIL import Image

# set the input directory containing the images
input_folder = "D:\\SPRING 2023\\MS_Thesis\\MASTER'S THESIS\\EdmCrack600\\dataset-EdmCrack600\\annotations"

# set the output directory for the resized images
output_folder = "D:\\SPRING 2023\\MS_Thesis\\MASTER'S THESIS\\EdmCrack600\\dataset-EdmCrack600\\resized_masks"

# set the desired output size
output_size = (512, 512)

# create the output directory if it does not exist
os.makedirs(output_folder, exist_ok=True)

# loop through each image in the input directory
for image_name in os.listdir(input_folder):
    # read the image
    image_path = os.path.join(input_folder, image_name)
    image = Image.open(image_path)
    
    # resize the image to the desired output size
    image_resized = image.resize(output_size)
    
    # save the resized image to the output directory with a new filename
    output_name = f"resized_{image_name}"
    output_path = os.path.join(output_folder, output_name)
    image_resized.save(output_path)


# In[ ]:




