import requests
import pandas as pd

# CSV dosyasının yolunu belirtin
file_path = r"*******\sample.csv"
url = "http://127.0.0.1:5000/predict"

# CSV dosyasını DataFrame olarak okuyun
csv_data = pd.read_csv(file_path)

# DataFrame'i JSON formatına dönüştürün
json_data = csv_data.to_dict(orient='list')

response = requests.post(url, json=json_data)

print(response.json())
