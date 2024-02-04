# Alzheimer's Image Classification

This project focuses on building a deep learning model for the classification of Alzheimer's disease using an image dataset with four classes. The code includes data preprocessing, augmentation, and a custom neural network architecture optimized using Keras Tuner.
Table of Contents

    Introduction
    Environment Setup
    Dataset Download and Organization
    Data Augmentation and SMOTE
    Keras Tuner for Hyperparameter Tuning
    Custom Model Architecture (CNN)
    Training and Evaluation
    Results
    How to Use
    Contributing
    License

## Introduction

This project aims to classify Alzheimer's disease using a dataset containing images from four classes: MildDemented, ModerateDemented, NonDemented, and VeryMildDemented. The code includes data preprocessing, augmentation, and the creation of a custom neural network architecture optimized using Keras Tuner.

## Environment Setup

    Install the required libraries using pip install -r requirements.txt.
    Upload your Kaggle API token (kaggle.json) for dataset download.

## Dataset Download and Organization

    Download the Alzheimer's dataset with 4 classes of images using the Kaggle API.
    Organize the dataset into training, testing, and combined directories.

## Data Augmentation and SMOTE

    Apply data augmentation using Keras ImageDataGenerator for training data.
    Address class imbalance using Synthetic Minority Over-sampling Technique (SMOTE) on the training data.

## Keras Tuner for Hyperparameter Tuning

    Use Keras Tuner to search for the best hyperparameters for the custom model architecture.

## Custom Model Architecture

    Define a custom neural network architecture using the obtained hyperparameters.
    Create a model checkpoint for saving the best model during training.

## Training and Evaluation

    Train the model on the preprocessed data.
    Evaluate the model on the validation and test datasets.
    Plot training and validation metrics.

## Results

    Display confusion matrices and classification reports for validation and test datasets.

# How to Use

    cd to the Alok folder
    run the notebook cells

# Contributing

    This notebook builds a CNN and trains it using Kaggle dataset. It is recommended to use the ADNI dataset.

# License

    MIT
