# Brain Tumor Detection using Convolutional Neural Networks

This repository contains code to train a Convolutional Neural Network (CNN) for detecting brain tumors using the Keras library with TensorFlow backend.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Results](#results)
- [License](#license)

## Introduction

This project aims to build a brain tumor detection model using deep learning techniques. The model is built using the Keras library with a TensorFlow backend. The code provided here includes data preprocessing, model definition, training, and evaluation.

## Dataset

The dataset used in this project is the "Brain Tumor Data Set." It contains MRI images of brains with and without tumors. The dataset is divided into training and validation subsets. It's available [here](/path/to/your/dataset).

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/brain-tumor-detection.git
   cd brain-tumor-detection
   ```

2. Install the required dependencies:

   ```bash
   pip install tensorflow pandas keras
   ```

## Usage

1. Ensure you have downloaded the dataset and placed it in the appropriate location.
2. Open the `brain_tumor_detection.py` script.
3. Update the `train_dir` and `val_dir` paths to point to your dataset directories.
4. Run the script:

   ```bash
   python brain_tumor_detection.py
   ```

## Model Architecture

The CNN model used for brain tumor detection consists of several layers, including convolutional layers, max-pooling layers, fully connected layers, batch normalization, and dropout layers.

## Training

The model is trained using the `ImageDataGenerator` class, which preprocesses and augments the training data. The training process involves optimizing the Binary Crossentropy loss using the Adam optimizer. Early stopping is employed to prevent overfitting.

## Results

The training history and validation accuracy of the model can be visualized and analyzed by referring to the `history` object obtained after training. Example code for visualization can be found in the `brain_tumor_detection.py` script.

## License

This project is licensed under the [MIT License](LICENSE).

---

The Dataset was provided by PREET VIRADIYA and is available on Kaggle.
