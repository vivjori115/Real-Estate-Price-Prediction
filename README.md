# 🏡 Real Estate Price Prediction Web Application

## Table of Contents
1. [Introduction](#introduction)  
2. [Project Objective](#project-objective)  
3. [Dataset Overview](#dataset-overview)  
4. [Analysis Highlights](#analysis-highlights)  
5. [Technologies Used](#technologies-used)  
6. [How to Use](#how-to-use)     
7. [Contributors](#contributors)  
8. [Input Parameters](#inputParameters)  
---

## Introduction
This project is a web-based application designed to predict real estate prices based on user input. It uses a machine learning model trained on location-based data such as distance to MRT stations, number of convenience stores, and geographical coordinates (latitude and longitude). The application is built with Streamlit and leverages a Linear Regression model for making predictions.

---

## Project Objective
The primary objectives of this project are:
- To provide an estimate of real estate prices based on key location-based factors.
- To offer a quick, user-friendly tool for property price estimation.
- To use a machine learning model to predict prices per unit area based on user inputs.

---

## Dataset Overview
The dataset used for this analysis includes the following features:
- **Distance to the nearest MRT station** (in meters)
- **Number of convenience stores** nearby
- **Latitude** (geographical coordinate)
- **Longitude** (geographical coordinate)

The model is trained using this data to predict house prices per unit area.

---

## Analysis Highlights
- **Price Prediction**: Predicts house prices based on user inputs.
- **User Input Interface**: A simple and interactive interface built with Streamlit.
- **Machine Learning**: Uses Linear Regression to provide price predictions.
- **Geographical Analysis**: Factors in location-based data such as distance to MRT stations and the number of nearby convenience stores.

---

## Technologies Used
- **Python**: Programming language for building the application.
- **Streamlit**: Framework for building the web interface.
- **Scikit-learn**: Machine learning library for building the Linear Regression model.
- **Pandas**: For data handling and manipulation.
- **NumPy**: For numerical operations.

---

## How It Works
The model is trained on a real estate dataset using Linear Regression to predict house prices per unit area based on the following features:
- **Distance to the nearest MRT station** (in meters)
- **Number of convenience stores** nearby
- **Latitude** (geographical coordinate)
- **Longitude** (geographical coordinate)

The user inputs these values, and the app provides a predicted price based on the trained model.

---


## Contributors
- **Data Scientist, Data Analyst and sql Web Developer.**

---


## Input Parameters
The app takes the following inputs from the user:
- **Distance to MRT Station (meters)**: Distance of the property from the nearest MRT station.
- **Number of Convenience Stores**: Number of convenience stores located near the property.
- **Latitude**: Latitude coordinate of the property.
- **Longitude**: Longitude coordinate of the property.

---

## Output
The app will provide a predicted house price per unit area based on the inputs provided by the user.

---

## ⚠ Note
This model provides a basic price estimate and should be used as a preliminary reference. For more accurate real estate valuations, additional factors and professional consultation may be necessary.

---

##  How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/vivjori115/Real-Estate-Price-Prediction.git

2. Install required dependencies:
    ```bash
   pip install -r requirements.txt
3. Run the Streamlit application:
    ```bash
   streamlit run app.py

    
   


