from fastapi import FastAPI
from fastapi.responses import Response
import pandas as pd
import joblib

# Load pre-trained model
model = joblib.load('earthquake_model.pkl')

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Earthquake Prediction API"}

# Serve a placeholder favicon
@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    # Return a small transparent PNG as a favicon
    favicon_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\nIDATx\xdac\xf8\x0f\x04\x00\x09\xf2\x02\xfa\xa7M\x0eE\x00\x00\x00\x00IEND\xaeB`\x82'
    return Response(content=favicon_bytes, media_type="image/png")

@app.post("/predict/")
def predict(latitude: float, longitude: float, depth: float, year: int, month: int, day: int):
    # Create input feature vector
    input_features = pd.DataFrame([{
        'latitude': latitude,
        'longitude': longitude,
        'depth': depth,
        'year': year,
        'month': month,
        'day': day
    }])
    # Make prediction
    prediction = model.predict(input_features)[0]
    return {"predicted_magnitude": prediction}
