import requests

url = "http://nonexistingipaddress"

try:
    response = requests.get(url)
    response.raise_for_status()  # This will raise an error for non-2xx status codes
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
