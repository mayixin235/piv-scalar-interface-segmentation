# PIV Scalar Interface Segmentation with U-Net

This repository contains my work on using a U-Net based deep learning model to segment scalar interfaces from synthetic particle image velocimetry (PIV) images.

The goal is to detect the scalar interface (mixing boundary) from PIV particle images, which is useful for analysing turbulence–scalar diffusion.

---

## 🔍 Project Overview

- Synthetic PIV dataset with pixel-wise ground truth interface masks
- U-Net segmentation model implemented in Python
- Training / validation / test pipeline
- Quantitative evaluation of:
  - training iterations
  - particle concentration
  - interface shape complexity

This repo is currently being cleaned up and migrated from my original MSc project.

---

## 📂 Planned Repository Structure

```bash
piv-scalar-interface-segmentation/
├── README.md
├── requirements.txt              # Python dependencies (to be added)
├── dataset/
│   ├── generate_dataset.m        # MATLAB script to create synthetic PIV images
│   └── examples/
│       ├── images/               # sample PIV images
│       └── masks/                # corresponding interface masks
├── src/
│   ├── models/
│   │   └── unet.py               # U-Net implementation
│   ├── train.py                  # training script
│   ├── evaluate.py               # evaluation script
│   └── inference.py              # run prediction on new images
└── figures/
    ├── sample_predictions.png    # qualitative examples
    └── training_curves.png       # loss/metric curves
