"""pass"""

import requests

base_url = "https://api-testnet.bybit.com"
end_point = "/v5/market/premium-index-price-kline"

complete_request = base_url + end_point
parameters = {
    "category": "linear",
    "symbol": "BTCUSDT",
    "interval": "D",
    "start": 1652112000000,
    "end": 1652544000000
}

response = requests.get(url=complete_request, params=parameters, timeout=10)

print(response.json())
