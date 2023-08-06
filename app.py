from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Araç tahmini için modelin yüklenmmesi
model = joblib.load("")

@app.route('/')
def root():
    return "Araç Tahmini Modeli"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data['text']

        # Tahmin
        prediction = model.predict([text])[0]

        response = {
            'text': text,
            'predicted_label': prediction
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
