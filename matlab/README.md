# MATLAB Synthetic PIV Image Generation

This folder contains MATLAB scripts used to generate synthetic PIV (Particle Image Velocimetry) particle images and the corresponding scalar-interface masks.

## Files
- **Layer_Generator.m**  
  Generates multi-layer turbulence structures with adjustable parameters (density ratio, wavelength limits, number of layers).

- **mat_new.m**  
  Controls the dataset size, saving paths, and calls the generator to produce full training, validation, and test sets.

## Output
The scripts produce:
- Raw synthetic particle images  
- Binary ground-truth masks  
- Configurable number of samples  

## Parameters
Key adjustable settings include:
- Density ratio  
- Lower wavelength limit (Lwk)  
- Number of turbulence layers  
- Number of images per dataset  

This dataset serves as the training ground for the U-Net segmentation model.
