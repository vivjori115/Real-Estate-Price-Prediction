import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the dataset
real_estate_data = pd.read_csv("Real_Estate (1).csv")

# Selecting features and target variable
features = ['Distance to the nearest MRT station', 'Number of convenience stores', 'Latitude', 'Longitude']
target = 'House price of unit area'

X = real_estate_data[features]
y = real_estate_data[target]

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model initialization and training
model = LinearRegression()
model.fit(X_train, y_train)

# Streamlit App
st.title("Real Estate Price Prediction")

# Input fields
distance_to_mrt = st.number_input("Distance to MRT Station (meters)", min_value=0)
num_convenience_stores = st.number_input("Number of Convenience Stores", min_value=0)
latitude = st.number_input("Latitude")
longitude = st.number_input("Longitude")

# Prediction button
if st.button('Predict Price'):
    if all(v is not None for v in [distance_to_mrt, num_convenience_stores, latitude, longitude]):
        # Prepare the feature vector
        features = pd.DataFrame([[distance_to_mrt, num_convenience_stores, latitude, longitude]], 
                                columns=['Distance to the nearest MRT station', 'Number of convenience stores', 'Latitude', 'Longitude'])
        # Predict
        prediction = model.predict(features)[0]
        st.write(f'Predicted House Price of Unit Area: {prediction:.2f}')
    else:
        st.write('Please provide all inputs to make a prediction.')
# Add your name to the bottom-right corner
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        right: 0;
        width: 100%;
        text-align: right;
        font-size: 12px;
        color: gray;
    }
    </style>
    <div class="footer">
    Developed by Vivek Rajaram Jori
    </div>
    """,
    unsafe_allow_html=True
)
