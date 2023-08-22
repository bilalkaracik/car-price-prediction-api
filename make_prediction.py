import requests

file_path = r"C:*************\flask/sample.csv"
url = "http://127.0.0.1:5000/predict"

files = {'file': open(file_path, 'rb')}
response = requests.post(url, files=files)

print(response.json())
