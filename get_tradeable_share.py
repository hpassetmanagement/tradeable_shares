import requests
import pandas as pd

# Define URL and payload
url = "https://www.idx.co.id/primary/TradingSummary/GetStockSummary"
payload = {
    "length": 9999,
    "start": 0
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
}

# Send the request with headers
response = requests.get(url, params=payload, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()["data"]  # Extract the 'data' key from the response

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv("stock_summary.csv", index=False)
    print("Data berhasil disimpan ke 'stock_summary.csv'")
else:
    print("Failed to retrieve data. Status code:", response.status_code)
