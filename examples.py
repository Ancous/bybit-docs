"""pass"""

import requests

base_url = "https://api-testnet.bybit.com"
end_point = "/v5/market/account-ratio"

complete_request = base_url + end_point
parameters = {
    "category": "linear",
    "symbol": "BTCUSDT",
    "period": "1h",
    "limit": 2,
    "startTime": "1696089600000",
    "endTime": "1696262400000"
}

response = requests.get(url=complete_request, params=parameters, timeout=10)

print(response.json())
