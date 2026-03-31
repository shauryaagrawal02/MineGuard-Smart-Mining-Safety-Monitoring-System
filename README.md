# MineGuard: AI-Based Mining Safety Monitoring System

## Overview

MineGuard is a machine learning-based safety monitoring system designed to assess risk levels in mining environments. It analyzes environmental parameters such as methane gas level, temperature, humidity, and mine depth to classify conditions into LOW, MEDIUM, or HIGH risk.

The system combines a rule-based approach with a Decision Tree model to provide intelligent and explainable predictions. It also includes critical safety conditions where extreme values immediately result in HIGH risk.

---

## Features

* Machine learning-based risk prediction using Decision Tree
* Rule-based system for comparison
* Automatic HIGH risk detection for extreme conditions
* Model evaluation using accuracy and confusion matrix
* Feature importance analysis
* Synthetic dataset generation for training

---

## How It Works

1. A synthetic dataset is generated using realistic mining conditions
2. A Decision Tree model is trained on this dataset
3. The model learns patterns between environmental parameters and risk levels
4. The user inputs real-time values
5. The system predicts risk using:

   * Machine learning model
   * Rule-based logic
6. Extreme conditions (e.g., very high temperature or gas levels) directly result in HIGH risk

---

## Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn

---

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mineguard.git
cd mineguard
```

### 2. Install dependencies

```bash
pip3 install numpy pandas scikit-learn
```

### 3. Run the project

```bash
python3 mineguard.py
```

---

## Usage

1. Run the program

2. Enter the following values:

   * Methane Gas Level (ppm)
   * Temperature (°C)
   * Humidity (%)
   * Mine Depth (meters)

3. The system will display:

   * ML Prediction
   * Rule-Based Prediction
   * Whether both predictions match
---

## Model Evaluation

* Accuracy Score is used to measure performance
* Confusion Matrix shows correct and incorrect classifications
* Feature Importance indicates which parameters influence risk the most

## Note

This project is developed not only for academic purposes but also to emphasize the importance of safety in mining environments. Hazardous conditions can lead to serious risks, and this system aims to promote awareness and preventive measures.
