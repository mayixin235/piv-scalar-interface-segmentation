# Image Resizing and Preprocessing

This folder contains Python scripts used to resize and clean the MATLAB-generated images before creating NumPy datasets.

## Files
- **image_size.py**  
  Resizes raw synthetic particle images to a fixed resolution suitable for the U-Net model.

- **mask_size.py**  
  Performs identical resizing operations on mask images to ensure pixel alignment.

## Purpose
MATLAB output images often vary slightly in size.  
This step ensures:
- Consistent input dimensions  
- Aligned image–mask pairs  
- Clean dataset structure for training  

## Output
Resized images saved into:
- `train/`  
- `val/`  
- `test/`

