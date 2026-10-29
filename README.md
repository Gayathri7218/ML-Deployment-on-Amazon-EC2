# ML Deployment on Amazon EC2

## Overview
A machine learning web application that predicts Iris flower
species using scikit-learn and Flask.

## Technologies
- Python
- Flask
- scikit-learn
- Joblib
- Ubuntu Linux
- Amazon EC2

## Project Files
- app.py: Flask web application
- train_model.py: Trains the ML model
- requirements.txt: Python dependencies

## Run Locally or on Ubuntu

1. Install Python and pip.
2. Create and activate a virtual environment.
3. Install dependencies:
   pip install -r requirements.txt
4. Train and save the model:
   python train_model.py
5. Start the application:
   python app.py
6. Open http://127.0.0.1:5000

## Dataset
The application uses the Iris dataset provided by scikit-learn.

## Cloud Deployment
The application was deployed on an Ubuntu EC2 instance
using Flask and a security group rule for port 5000.
