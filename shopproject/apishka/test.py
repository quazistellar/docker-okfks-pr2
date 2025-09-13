import requests

try:
        response = requests.get('http://127.0.0.1:8000/')
        print(f"Status code: {response.status_code}")
        print(f"Content: {response.text}")
except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
