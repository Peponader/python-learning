from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("MY_API_KEY")

url = "https://httpbin.org/headers"

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(
    url,
    headers=headers,
    timeout=30
)

print(response.json())