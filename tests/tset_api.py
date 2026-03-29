import requests
import json

# URL of our local endpoint
url = "http://127.0.0.1:8000/predict"

# Data for the forecast (e.g., trying to predict July 2026)
payload = {
  "month": 7,
  "quarter": 3,
  "year": 2026,
  "lag_1M": 4500000,           # Passenger traffic in June 2026
  "lag_3M": 4100000,           # Passenger traffic in April 2026
  "lag_12M": 4450000,          # Passenger traffic a year ago (July 2025)
  "rolling_mean_3M": 4300000,  # Average for spring-summer (last 3 months)
  "rolling_mean_6M": 4000000,  # Average for the last 6 months
  "pct_change_1M": 0.05       # 5% growth compared to the previous month
}

headers = {
  'Content-Type': 'application/json'
}

print("Sending request to Lufthansa Forecasting API...")
print("Input data:", json.dumps(payload, indent=2))

# Making a POST request
response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    result = response.json()
    print("\nSUCCESS! Response from server:")
    print(f"Passenger traffic forecast: {result['predicted_passengers']:,} people")
else:
    print(f"\nServer error: {response.status_code}")
    print(response.text)