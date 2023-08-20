import joblib
from flask import Flask, request, jsonify
from xgboost import XGBRegressor

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
        data = request.get_json()
        # Gelen veriyi modele uygun hale getirin
        # Örnek: text = data['text']
        # dtest = xgb.DMatrix([[text]])
        
        # Tahmin
        prediction = model_service.predict(dtest)

        response = {
            'predicted_label': prediction
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
