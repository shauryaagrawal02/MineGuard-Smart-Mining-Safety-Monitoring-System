# MineGuard: An AI-Based Mining Safety Monitoring System

## Overview

MineGuard is a machine learning-based safety monitoring system, which can effectively assess risk levels in a mining environment. The system takes various environmental parameters, such as methane gas level, temperature, humidity, and depth of the mine, and classifies them as LOW, MEDIUM, or HIGH risk levels.

The system incorporates a rule-based system along with a Decision Tree model, which helps in intelligent decision-making.

---

## Features

* Machine learning-based risk prediction using a Decision Tree model
* Rule-based system for comparison
* Automatic HIGH risk level detection for extreme conditions
* Model evaluation using accuracy and confusion matrix
* Feature importance analysis
* Synthetic dataset generation for training

---

## How It Works

1. Synthetic dataset generation using realistic conditions in a mine
2. Decision Tree model training on a synthetic dataset
3. Model learning from a dataset, where risk levels are associated with various environmental parameters
4. User input of real-time data
5. Predict risk levels using:

   * Machine learning model
   * Rule-based system
* Rule-based logic
6. Extreme conditions such as very high temperature or gas levels will directly cause HIGH risk

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
python3 MineGuard:Mining Safety Monitoring System.py
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

This project is developed not only for academic purposes but also to highlight the need for safety in the mining environment. The risk of hazardous conditions can cause serious risks, and this system is intended to raise awareness of preventive measures.
