- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос

>Зона применения:  
>
>`spot` - спот  
>`option` - опцион  
>`linear` - контракт (расчет в USDT, USDC, ...)
>
> - `Perpetual` - контракт без даты экспирации
> - `Futures` - контракт с датой экспирации
>
>`inverse` - контракт (расчет в BTC, ETH, ...)
>
> - `Perpetual` - контракт без даты экспирации
> - `Futures` - контракт с датой экспирации

<a id="конечная-точка"></a>

## Конечная точка

`xxxxx`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  
  ```

- requests

  ```python
  import time
  import hmac
  import hashlib
  import json
  import requests

  base_url = "https://api-testnet.bybit.com"
  end_point = "xxxxx"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  secret_key = "<api_secret от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "category": "spot",
      "symbol": "BTCUSDT",
      "side": "Buy",
      "orderType": "Limit",
      "qty": "0.1",
      "price": "15600",
      "timeInForce": "PostOnly",
      "orderLinkId": "spot-test-postonly",
      "isLeverage": 0,
      "orderFilter": "Order"
  }

  param_str = time_stamp + api_key + recv_window + json.dumps(data, separators=(',', ':'))
  
  signature = hmac.new(
      key=secret_key.encode("utf-8"),
      msg=param_str.encode("utf-8"),
      digestmod=hashlib.sha256
  ).hexdigest()
  
  headers = {
    "X-BAPI-API-KEY": api_key,
    "X-BAPI-SIGN": signature,
    "X-BAPI-TIMESTAMP": time_stamp,
    "X-BAPI-RECV-WINDOW": recv_window,
  }

  response = requests.post(url=complete_request, headers=headers, json=data, timeout=10)

  print(response.json())
  ```

- pybit

  ```python
  
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

|Параметр  	                  |Обязательный	 |Тип  	  |Комментарии       |По умолчанию|
|-----------------------------|--------------|--------|------------------|------------|
|Параметр                     |Обязательный  |Тип     |Комментарии       |По умолчанию|
|Параметр                     |Обязательный  |Тип     |Комментарии       |По умолчанию|
|Параметр                     |Обязательный  |Тип     |Комментарии       |По умолчанию|

<a id="пример-ответа"></a>

## Пример ответа

```json

```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр  |Тип       |Комментарии                                             |
|----------|----------|--------------------------------------------------------|
|Параметр   |Тип      |Комментарии                                             |
|Параметр   |Тип      |Комментарии                                             |
|Параметр   |Тип      |Комментарии                                             |

x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x<br>
