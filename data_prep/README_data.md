# Dataset Preparation 

This directory contains the script responsible for converting image folders into NumPy arrays for efficient training.

## File
- **data.py**

## Functions
- Loads resized images and masks  
- Normalizes image intensities  
- Binarizes mask values  
- Saves the following arrays:
imgs_train.npy
imgs_mask_train.npy
imgs_val.npy
imgs_mask_val.npy
imgs_test.npy
imgs_mask_test.npy
