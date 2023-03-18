#!/usr/bin/env python
# coding: utf-8

# In[3]:


import torch
import torchvision.transforms as transforms
from torchvision.utils import save_image
import cv2 
from matplotlib import pyplot as plt
import numpy as np
from torchvision import transforms, models


# In[4]:


## Load the images
# This function will read the image using its path with opencv
def Load_Image(Path):
    img = cv2.imread(Path)[:,:,::-1] # opencv read the images in BGR format 
                                    # so we use [:,:,::-1] to convert from BGR to RGB
    return img


# In[5]:


## display the image and corresponding masks/annotations/labelings

def display_images(image, mask): 
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title("Image")
    plt.subplot(1, 2, 2)
    plt.imshow(mask)
    plt.title("Mask")
    plt.show()


# In[6]:


## Rotate the image and corresponding masks/annotations/labelings

def rotate(image, mask, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle * (-1) , 1.0) ## 1 is the scaling factor to remain the size same 
    image = cv2.warpAffine(image, M, (w, h))
    mask = cv2.warpAffine(mask, M, (w, h))
    return image, mask


# In[7]:


## Flip the image and corresponding mask to left_right and up_down. This function is taken from https://github.com/qinnzou/DeepCrack/blob/master/codes/data/augmentation.py

def t_random(min=0, max=1):
    return min + (max - min) * np.random.rand()

def t_randint(min, max):
    return np.random.randint(low=min, high=max)

def RandomFlip(img, mask, FLIP_LEFT_RIGHT=True, FLIP_TOP_BOTTOM=True):

    if FLIP_LEFT_RIGHT and t_random() < 0.5:
        img = cv2.flip(img, 1)
        mask = cv2.flip(mask, 1)

    if FLIP_TOP_BOTTOM and t_random() < 0.5:
        img = cv2.flip(img, 0)
        mask = cv2.flip(mask, 0)
    return img, mask


# In[8]:


## CenterCrop
import numpy as np
import torchvision.transforms as transforms

def centerCrop(img, msk, size):
    # Convert to PIL images
    img = transforms.ToPILImage()(img)
    msk = transforms.ToPILImage()(msk)

    # Center crop images
    img_cropped = transforms.CenterCrop(size)(img)
    msk_cropped = transforms.CenterCrop(size)(msk)

    # Convert back to numpy arrays
    img_cropped = np.array(img_cropped)
    msk_cropped = np.array(msk_cropped)

    return img_cropped, msk_cropped


# In[9]:


### we dont need resize because center crop is resizing the region of interest
def resize(img, msk, size): 
    img = np.array(img)
    msk = np.array(msk)
    img = transforms.Resize(img, size)
    msk = transforms.Resize(msk, size)
    return img, msk


# In[ ]:





# In[ ]:




