import joblib
from flask import Flask, request, jsonify
from xgboost import XGBRegressor

app = Flask(__name__)

# XGBoost modelinizi yükleme
model = joblib.load("xgboost_tuned_model.pkl")

@app.route('/')
def root():
    return "Araç Tahmini Modeli"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # Gelen veriyi modele uygun hale getirin, örneğin:
        # text = data['text']
        # dtest = xgb.DMatrix([[text]])
        
        # Tahmin
        prediction = model.predict(dtest)[0]

        response = {
            'text': text,
            'predicted_label': prediction
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
