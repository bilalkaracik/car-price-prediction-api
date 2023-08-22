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
        csv_data = request.files['file']  # CSV dosyasını al
        input_data = pd.read_csv(csv_data)  # CSV verisini DataFrame'e dönüştür
        
        # # Gerekli dönüşümleri ve One-Hot Encoding işlemlerini yapma
        # input_data["doornumber"] = input_data["doornumber"].replace({"two": 2, "four": 4})
        # input_data['cylindernumber'] = input_data['cylindernumber'].replace({'four': 4, 'six': 6, 'five': 5,
        #                                                                      'three': 3, 'twelve': 12, 'two': 2,
        #                                                                      'eight': 8})
        # dums = pd.get_dummies(input_data[["CarName", "fueltype", "aspiration", "carbody",
        #                                   "drivewheel", "enginelocation", "enginetype",
        #                                   "fuelsystem"]])
        # X_ = input_data.drop(["price" ,"CarName", "fueltype", "aspiration", "carbody", "drivewheel",
        #                       "enginelocation", "enginetype", "fuelsystem"], axis=1)
        # X = pd.concat([X_, dums], axis=1)
        input_np = input_data.to_numpy()
        
        # Tahmin işlemi
        prediction = model_service.predict(input_np)
        
        response = {
            'predicted_price': prediction.tolist()
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=False)
