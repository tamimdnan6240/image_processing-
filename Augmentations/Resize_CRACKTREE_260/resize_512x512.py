import os
from PIL import Image

# set the input directory containing the images
input_folder = "C:\\Users\\tamim\\OneDrive - University of North Carolina at Charlotte\\DeepCrack_(tamim)\\DeepCrack_Master\\codes\\data\\CRACKTREE260\\image"

# set the output directory for the resized images
output_folder = 'C:\\Users\\tamim\\OneDrive - University of North Carolina at Charlotte\\DeepCrack_(tamim)\\DeepCrack_Master\\codes\\data\\CRACKTREE260\\resized_image'

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
    
 ## again for masks
import os
from PIL import Image

# set the input directory containing the images
input_folder = 'C:\\Users\\tamim\\OneDrive - University of North Carolina at Charlotte\\DeepCrack_(tamim)\\DeepCrack_Master\\codes\\data\\CRACKTREE260\\gt'

# set the output directory for the resized images
output_folder = 'C:\\Users\\tamim\\OneDrive - University of North Carolina at Charlotte\\DeepCrack_(tamim)\\DeepCrack_Master\\codes\\data\\CRACKTREE260\\resized_mask'

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
