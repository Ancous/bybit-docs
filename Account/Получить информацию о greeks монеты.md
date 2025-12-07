- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос на получение информации о текущем счете [greeks](https://www.bybit-global.com/ru-RU/help-center/article/Option-Greeks)

<a id="конечная-точка"></a>

## Конечная точка

`/v5/asset/coin-greeks`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/asset/coin-greeks?baseCoin=BTC HTTP/1.1
  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1672287887610
  X-BAPI-RECV-WINDOW: 5000
  ```

- собственная реализация

  ```python
  import time
  import hmac
  import hashlib
  import requests

  from urllib.parse import urlencode

  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/asset/coin-greeks"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "baseCoin": "BTC",
  }

  param_str = time_stamp + api_key + recv_window + urlencode(data)
  
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

  response = requests.get(url=complete_request, headers=headers, params=data, timeout=10)

  print(response.json())
  ```

- pybit

  ```python
  from pybit.unified_trading import HTTP

  session = HTTP(
      testnet=True,
      api_key="<api_key от биржи bybit>",
      api_secret="<secret_key от биржи bybit>",
  )
  print(session.get_coin_greeks(
      baseCoin="BTC", 
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

|Параметр  	                  |Обязательный	 |Тип  	  |Комментарии       |По умолчанию|
|-----------------------------|--------------|--------|------------------|------------|
|baseCoin                     |нет  |string     |***Базовая монета***<br><br>Только заглавными буквами.<br>Если не передано, все поддерживаемые базовые монеты будут возвращены по умолчанию.       |-   |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "list": [
            {
                "baseCoin": "BTC",
                "totalDelta": "0.00004001",
                "totalGamma": "-0.00000009",
                "totalVega": "-0.00039689",
                "totalTheta": "0.01243824"
            }
        ]
    },
    "retExtInfo": {},
    "time": 1672287887942
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр  |Тип       |Комментарии                                             |
|----------|----------|--------------------------------------------------------|
|list       |array  	       	  |Массив объектов                               |
|baseCoin   |string      |Базовая монета                                             |
|totalDelta   |string      |Значение Delta                                             |
|totalGamma   |string      |Значение Gamma                                             |
|totalVega   |string      |Значение Vega                                             |
|totalTheta   |string      |Значение Theta                                             |
