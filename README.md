# PIV Scalar Interface Segmentation using U-Net

This repository contains a full pipeline for generating, preprocessing, and segmenting synthetic PIV (Particle Image Velocimetry) particle images using a U-Net model. The project is based on MATLAB image generation, Python data processing, and deep learning training.

## Pipeline Overview

1. **MATLAB Synthetic Image Generation**
   - Generate multi-layer turbulence structures
   - Adjustable density ratio and wavelength limits
   - Outputs raw images and binary masks

2. **Python Image Resizing**
   - Resize all images to consistent dimensions
   - Maintains mask–image alignment

3. **Data Preparation**
   - Convert image folders into NumPy arrays
   - Normalization and mask binarization
   - Generates all `.npy` datasets

4. **U-Net Training**
   - Build U-Net architecture
   - Train, test, and visualize predictions
   - Save segmentation results

## Repository Structure
'''text
piv-scalar-segmentation/
│
├── matlab/
│     ├── Layer_Generator.m
│     ├── mat_new.m
│     └── README_matlab.md
│
├── resize/
│     ├── image_size.py
│     ├── mask_size.py
│     └── README_resize.md
│
├── data_prep/
│     ├── data.py
│     └── README_data.md
│
├── unet/
│     ├── case.py
│     ├── weights/ (empty or .gitignore)
│     └── README_unet.md
│
├── sample_outputs/
│     ├── synthetic_image.png
│     ├── synthetic_mask.png
│     ├── unet_prediction.png
│
├── figures/
│     └── pipeline_diagram.png (optional)
│
└── README.md
'''

## Example Results
<img width="840" height="630" alt="11" src="https://github.com/user-attachments/assets/69c0702d-ba88-42da-b865-67d60a4bd6f2" />

## Requirements
Python 3.x, NumPy, TensorFlow/Keras, OpenCV, MATLAB

## About
Project developed for research on turbulence–scalar interface detection.
