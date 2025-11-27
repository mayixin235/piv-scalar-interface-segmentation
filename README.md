# PIV Scalar Interface Segmentation (U-Net)

This project performs scalar interface segmentation on synthetic PIV (Particle Image Velocimetry) images using a U-Net model.  
It was developed as part of my MSc research work.

---

## 🔍 Overview
- Synthetic PIV images + ground-truth interface masks  
- Preprocessing scripts for resizing images and masks  
- U-Net segmentation implemented with Keras  
- Training / testing pipeline with result saving

---

## 📂 Project Structure
src/
├── data.py # Load + preprocess data, create .npy datasets
├── case.py # U-Net model, training and testing
scripts/
├── image_size.py # Resize PIV images
├── mask_size.py # Resize and binarize masks


