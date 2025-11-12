- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос на изменения режима хеджирования для сотовой торговли

>Зона применения:  
>
>`spot` - спот  

<a id="конечная-точка"></a>

## Конечная точка

`/v5/account/set-hedging-mode`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  POST /v5/account/set-hedging-mode HTTP/1.1
  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1700117968580
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  Content-Length: 31
  
  {
      "setHedgingMode": "OFF"
  }
  ```

- requests

  ```python
  import time
  import hmac
  import hashlib
  import json
  import requests

  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/account/set-hedging-mode"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  api_secret = "<api_secret от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "setHedgingMode": "OFF"
  }

  param_str = time_stamp + api_key + recv_window + json.dumps(data)
  
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

<a id="параметры-запроса"></a>

## Параметры запроса

|Параметр  	                  |Обязательный	 |Тип  	  |Комментарии       |По умолчанию|
|-----------------------------|--------------|--------|------------------|------------|
|setHedgingMode                     |да  |string       |`ON`, `OFF`       |-   |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "SUCCESS"
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр  |Тип       |Комментарии                                             |
|----------|----------|--------------------------------------------------------|
|retCode   |integer      |Код результата                                          |
|retMsg   |string      |Сообщение результата                                     |
