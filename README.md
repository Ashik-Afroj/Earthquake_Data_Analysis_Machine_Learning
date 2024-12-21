# Earthquake_Data_Analysis_Machine_Learning


Required module and packages:
Core Python Modules:
os
pickle
datetime

Data Manipulation:
pandas
numpy

Machine Learning & Neural Networks:
scikit-learn
tensorflow.keras
xgboost
lightgbm

Data Visualization:
matplotlib
seaborn

Geospatial Analysis:
geopandas
folium
folium.plugins.HeatMap

Others:
joblib


Run in Anaconda Prompt with correct directory:

At first you need to download the "earthquake_model.pkl" file and save it in the directory:
File link: https://drive.google.com/drive/folders/1DbIeE5a3gvqvUj0HX1QS5O-9eZdf258q?usp=sharing

For loading the dashboard:

Run: "python dashboard4.py"
Then Visit: http://127.0.0.1:8050/

For the prediction:
Run: "uvicorn app:app --reload"
Then visit: http://127.0.0.1:8000/docs#/