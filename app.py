import joblib
import pandas as pd
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

class ModelService:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)
    
    def predict(self, data):
        return self.model.predict(data)

model_service = ModelService("xgboost_tuned_model.pkl")

@app.route('/')
def root():
    return "Araç Tahmini Modeli"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_json = request.json  # JSON verisini al
        
        input_data = pd.DataFrame(input_json)  # JSON verisini DataFrame'e dönüştür
        input_np = input_data.to_numpy()
        
        prediction = model_service.predict(input_np)  # Tahmin işlemi
        
        response = {
            'predicted_price': prediction.tolist()
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=False)
