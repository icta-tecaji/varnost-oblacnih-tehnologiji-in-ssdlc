import requests

url = "https://demo.com/api/v1/test"
API_KEY = "14xgf4j0886ee910bqkib69iky0l69ntj0v6gp54"

resp = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})
print(resp.json())
