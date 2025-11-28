# U-Net Segmentation Model

This folder contains the deep learning model and training/testing pipeline used for scalar-interface segmentation.

## File
- **case.py**

## Main Functions
- `load_data()`  
  Loads NumPy datasets prepared in data_prep/.

- `get_unet()`  
  Builds the U-Net architecture (encoder–decoder with skip connections).

- `train()`  
  Trains the model, saves weights at checkpoints.

- `test()`  
  Runs inference on test images.

- `save_image()`  
  Exports predicted masks as images.

- `plot()`  
  Visualizes the U-Net architecture.

## Model
The implemented U-Net:
- Accepts 256×256 (or configurable) images  
- Performs pixel-wise segmentation  
- Outputs binary interface predictions

## Output
Saved items include:
- Trained model weights  
- Prediction images  
- Evaluation visualizations

