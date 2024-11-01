# Genetic Pedigree YOLO Dataset Generation

## Overview

This repository is dedicated to generating synthetic datasets of genetic pedigree charts for use with YOLO (You Only Look Once) object detection models. The dataset aims to simulate common symbols found in genealogical trees to help researchers and developers create models capable of detecting specific familial and medical markers on real-world genetic charts.

## Problem Statement

In genetics and medical research, pedigree charts (also known as family trees) are essential for visualizing hereditary patterns and medical history across generations. Pedigree charts often use distinct symbols to represent individuals and their relationships, as well as specific medical conditions and statuses, which are crucial for genetic counseling and research into hereditary diseases. However, manually annotated datasets of these symbols for machine learning purposes are scarce.

To address this issue, this project generates a synthetic dataset of symbols commonly found in genetic pedigree charts, represented in a YOLO-compatible format. Our dataset includes various classes of individuals with different attributes, such as gender, health status, and death, to facilitate the training of object detection models for recognizing these patterns.

## Classes and Symbols

In this dataset, we define the following classes, each represented by a unique symbol:

![Pedigree Nomenclature](Nomenclature_arbre_genealogique.png)

### Symbol Descriptions

1. **Male**: Represented as a black-bordered square.
2. **Female**: Represented as a black-bordered circle.
3. **Deceased Male**: A black-bordered square with a diagonal cross.
4. **Deceased Female**: A black-bordered circle with a diagonal cross.
5. **Affected Male (deceased)**: A red-filled square with a diagonal cross.
6. **Affected Female (deceased)**: A blue-filled circle with a diagonal cross.
7. **Index**: Indicated with an arrow, pointing to a specific individual in the pedigree.
8. **Affected Male**: A green-filled square.
9. **Affected Female**: A green-filled circle.

The symbols in the image above illustrate the different classes used in this dataset. Each class represents a specific familial or health-related attribute, aiding in the identification of hereditary patterns.

## Dataset Characteristics

The dataset contains the following features to make it suitable for robust training:

- **Random Rotations**: Each symbol is rotated randomly to introduce variety in orientation.
- **Connection Lines**: Random lines connect symbols to simulate real genealogical trees, adding contextual complexity to the dataset.
- **Synthetic Noise**: Random noise is applied to each image to simulate varying levels of image quality and help improve model robustness.
- **YOLO Format**: Each symbol is labeled with bounding boxes in YOLO format, making it compatible with YOLOv5 and YOLOv8 models.

## Project Structure

```plaintext
.
├── images/
│   ├── train/
│   ├── val/
│   └── test/
└── labels/
    ├── train/
    ├── val/
    └── test/