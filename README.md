# 🔢 MNIST Digit Classifier

A handwritten digit classification project using **Perceptron, Artificial Neural Network (ANN), and Convolutional Neural Network (CNN)** trained on the MNIST dataset.

## 🚀 Live Demo

[Try the MNIST Digit Classifier](https://mnist-digit-classifier-4ko5nobnzot2gtgzy28xzw.streamlit.com)

## 📌 Project Overview

This project compares three different machine learning and deep learning approaches for handwritten digit classification.

The trained models are integrated into a **Streamlit web application**, where users can upload a handwritten digit image and get a prediction.

## 🤖 Models Used

* Perceptron
* Artificial Neural Network (ANN)
* Convolutional Neural Network (CNN)

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* TensorFlow / Keras
* Streamlit
* Matplotlib
* Jupyter Notebook

## 🔄 Project Workflow

```text
MNIST Dataset
      ↓
Data Preprocessing
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Save Trained Models
      ↓
Streamlit Application
      ↓
Upload Digit
      ↓
Prediction
```

## 📂 Project Structure

```text
mnist-digit-classifier/
│
├── app.py
├── mnist_project.ipynb
├── ANN.keras
├── CNN.keras
├── perceptron.pkl
├── requirements.txt
├── runtime.txt
├── .gitignore
└── README.md
```

## 📓 Notebook

`mnist_project.ipynb` contains the complete model development process, including:

* Dataset loading
* Data preprocessing
* Model building
* Model training
* Model evaluation
* Saving trained models

## 🌐 Streamlit App

The Streamlit application provides a simple interface to:

1. Upload a handwritten digit image
2. Select a model
3. Generate a digit prediction


## ⚠️ Note

The models were trained on the **MNIST dataset**, so predictions are most reliable for images that resemble the MNIST handwritten-digit format.

Different handwriting styles, image backgrounds, fonts, lighting, and image quality can affect predictions.

## 🎯 Future Improvements

* Multi-digit number recognition
* Automatic digit detection and cropping
* Improved image preprocessing
* Prediction confidence visualization
* Model accuracy comparison
* Improved Streamlit UI

## 👨‍💻 Author

**Ghanshyam Bansod**

AI & Data Science Student | Aspiring Data Scientist

GitHub: [@bansod-dev](https://github.com/bansod-dev)
