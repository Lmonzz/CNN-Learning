# Deep Learning Self-Learning Repository

This repository contains several Jupyter notebooks and pre-trained models related to various deep learning experiments and practices, especially in computer vision (CV) tasks.

## Directory Structure and File Explanation

### Notebooks:

- **01-Keras-CNN-MNIST.ipynb**  
  This notebook implements a Convolutional Neural Network (CNN) on the MNIST dataset, which contains grayscale images of handwritten digits (0-9). It demonstrates how to preprocess the dataset and train a CNN model for image classification.

- **02-Keras-CNN-CIFAR-10.ipynb**  
  This notebook uses a CNN to classify images from the CIFAR-10 dataset, which consists of color images with 3 color channels (RGB). It includes steps for model training, and evaluation on the CIFAR-10 dataset.

- **03-Deep-Learning-Custom-Images-Malaria.ipynb**  
  This notebook demonstrates how to train a CNN model on custom images (e.g., images related to Malaria detection, stored in JPG/JPEG formats). It walks through the process of data preprocessing, including resizing images, augmented images,and training the model on custom datasets.

- **04-DL-CV-Assessment.ipynb**  
  This is a personal project or self-assessment as part of a course. It involve applying deep learning techniques to solve a specific problem in computer vision.

- **05-DL-CV-Assessment-Solution.ipynb**  
  This notebook contains the solution provided by the course for the same assessment completed in **04-DL-CV-Assessment.ipynb**. It may include different approaches or improvements over your original approach.

- **CNN_model1.ipynb**  
  This notebook contains my custom CNN model that I trained for classicate trashes.

- **file_process.ipynb**  
  This notebook is used for preprocessing and organizing image files. It helps in categorizing images into directories based on their labels, which is useful when using functions like `flow_from_directory` for image data loading in Keras. 

- **inceptionv3.ipynb**  
  This notebook uses the pre-trained InceptionV3 model and fine-tunes it for your custom dataset. The InceptionV3 model is a well-known pre-trained model used for transfer learning in various computer vision tasks.

### Models:

- **cifar_10epochs.h5**  
  This is a trained model (in `.h5` format) that I obtained from the course for classifying images in the CIFAR-10 dataset. It is a model trained for 10 epochs.

- **cifar_10epochs.keras**  
  This is the same CIFAR-10 model, but saved in the `.keras` format (instead of `.h5`) due to compatibility issues with the latest versions of TensorFlow. This model can be loaded and used in my deep learning projects.

- **larger_CIFAR10_model.h5**  
  This is another version of the CIFAR-10 model trained in the course. It may be a model trained on a larger or more complex version of the CIFAR-10 dataset.

- **malaria_detector.h5**  
  This is a model trained specifically for malaria image detection, as part of a course or project. The model is stored in the `.h5` format.

- **myfirstmodel.h5**  
  This is my first model trained in the course, stored in `.h5` format. It might be a simple model or an early version that you used to understand deep learning workflows.

## Usage

- To run any of the Jupyter notebooks, open them using a Jupyter notebook environment or JupyterLab.
- Make sure all required dependencies (e.g., TensorFlow, Keras, etc.) are installed by running `pip install -r requirements.txt` (if you have a `requirements.txt` file).
- The models can be loaded into your Python code using Keras's `load_model` function for further evaluation or fine-tuning.

## Notes

- Ensure that you have the correct version of TensorFlow installed, as some older `.h5` files might not be compatible with the latest TensorFlow versions.
- You can use the pre-trained models for transfer learning or further experimentation on new datasets.
