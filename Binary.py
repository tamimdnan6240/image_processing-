import os
from PIL import Image

input_dir = "C:\\Users\\tamim\\crackseg\\CRACKTREE260\\masks"
output_dir = "C:\\Users\\tamim\\crackseg\\CRACKTREE260\\binary_images"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Open image and convert to grayscale
        img = Image.open(os.path.join(input_dir, filename)).convert('L')
        
        # Convert to binary
        threshold = 50
        binary = img.point(lambda x: 0 if x < threshold else 255, '1')
        
        # Save binary image with same filename
        binary.save(os.path.join(output_dir, filename))
