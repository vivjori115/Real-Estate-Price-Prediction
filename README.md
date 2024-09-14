🏡 Real Estate Price Prediction Web Application
This project is a web-based application designed to predict real estate prices based on user input. It uses a machine learning model trained on location-based data such as distance to MRT stations, number of convenience stores, and geographical coordinates (latitude and longitude). The application is built with Streamlit and leverages a Linear Regression model for making predictions.

🚀 Features
Predicts house price per unit area using Linear Regression.
User-friendly interface built with Streamlit.
Takes inputs such as distance to the nearest MRT station, number of convenience stores, latitude, and longitude.
Provides a quick estimate of real estate prices based on location.
📚 Technologies Used
Python
Streamlit (for the web interface)
Scikit-learn (for machine learning model)
Pandas (for data handling)
NumPy (for numerical operations)
🎯 Objective
The aim of this project is to provide a preliminary estimate of real estate prices based on key location-based factors. This app can serve as a quick reference for individuals looking to estimate property values in a particular area.

🔧 How It Works
The model is trained on a real estate dataset using Linear Regression to predict house prices per unit area based on the following features:

Distance to the nearest MRT station
Number of convenience stores nearby
Latitude
Longitude
The user inputs these values, and the app provides a predicted price based on the trained model.

⚙️ Usage
1. Clone the Repository
bash
Copy code
git clone <repository_url>
2. Install the Required Dependencies
bash
Copy code
pip install streamlit numpy pandas scikit-learn
3. Run the Streamlit App
bash
Copy code
streamlit run app.py
4. Access the App
Once the app is running, a URL will be provided in the terminal. Open your web browser and navigate to the given URL to interact with the app.

📝 Input Parameters
The app takes the following inputs from the user:

Distance to MRT Station (meters): Distance of the property from the nearest MRT station.
Number of Convenience Stores: Number of convenience stores located near the property.
Latitude: Latitude coordinate of the property.
Longitude: Longitude coordinate of the property.
🎯 Output
The app will provide a predicted house price per unit area based on the inputs provided by the user.

⚠️ Note
This model provides a basic price estimate and should be used as a preliminary reference. For more accurate real estate valuations, additional factors and professional consultation may be necessary.
