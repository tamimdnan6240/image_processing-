import os
import shutil
import random
import time

# Set source directories
source_root = '/content/drive/MyDrive/Railroad-crossing-Vision-Language-Model/VLM-DATA-updated/Princeton-Indiana-Rail-cross'
day_folder = os.path.join(source_root, 'Day-time')
night_folder = os.path.join(source_root, 'Night')

# Set target directory
target_root = '/content/drive/MyDrive/Railroad-crossing-Vision-Language-Model/VLM-DATA-updated/sampled_dataset'
os.makedirs(target_root, exist_ok=True)

min_images = 3
max_images = 0

# Function to sample and copy images
def sample_images(src_base, dest_base, time_of_day):
    for category in os.listdir(src_base):
        category_path = os.path.join(src_base, category)
        if os.path.isdir(category_path):
            images = os.listdir(category_path)
            if len(images) < min_images:
                print(f"❌ Skipped '{time_of_day}/{category}' (only {len(images)} images)")
                continue

            sample_count = min(len(images), max_images)
            sampled_images = random.sample(images, sample_count)

            target_category_path = os.path.join(dest_base, time_of_day, category)
            os.makedirs(target_category_path, exist_ok=True)

            for img in sampled_images:
                try:
                    shutil.copy2(os.path.join(category_path, img), target_category_path)
                    time.sleep(0.1)
                except Exception as e:
                    print(f"⚠️ Failed to copy {img}: {e}")
            print(f"✅ Sampled {sample_count} images from '{time_of_day}/{category}'")

# Run sampling for both day and night
sample_images(day_folder, target_root, 'Day')
sample_images(night_folder, target_root, 'Night')

print("\n✅ Sampling complete.")
