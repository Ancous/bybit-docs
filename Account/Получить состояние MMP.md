- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос на получения состояния MMP

<a id="конечная-точка"></a>

## Конечная точка

`/v5/account/mmp-state`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  POST /v5/account/mmp-reset HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1675842997277
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  
  {
      "baseCoin": "ETH"
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
  end_point = "/v5/account/mmp-state"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  api_secret = "<api_secret от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "baseCoin": "ETH"
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

- pybit

  ```python
  from pybit.unified_trading import HTTP

  session = HTTP(
      testnet=True,
      api_key="<api_key от биржи bybit>",
      api_secret="<api_secret от биржи bybit>",
  )
  print(session.get_mmp_state(
      baseCoin="ETH",
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

|Параметр  	                  |Обязательный	 |Тип  	  |Комментарии       |По умолчанию|
|-----------------------------|--------------|--------|------------------|------------|
|baseCoin	                  |да            |string  |***Базовая монета***<br><br>Только заглавными буквами	|-  |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "result": [
            {
                "baseCoin": "BTC",
                "mmpEnabled": true,
                "window": "5000",
                "frozenPeriod": "100000",
                "qtyLimit": "0.01",
                "deltaLimit": "0.01",
                "mmpFrozenUntil": "1675760625519",
                "mmpFrozen": false
            }
        ]
    },
    "retExtInfo": {},
    "time": 1675843188984
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр  |Тип       |Комментарии                                             |
|----------|----------|--------------------------------------------------------|
|result   |array      |Массив объектов                                             |
|baseCoin   |string      |Базовая монета                                             |
|mmpEnabled   |boolean      |Включена ли учетная запись mmp                                             |
|window   |string      |Временное окно (миллисекунды)                                             |
|frozenPeriod   |string      |Период заморозки (миллисекунды)                                             |
|qtyLimit   |string      |Лимит количества                                             |
|deltaLimit   |string      |Лимит дельты                                             |
|mmpFrozenUntil   |string      |Временная метка разморозки (миллисекунды)                                            |
|mmpFrozen   |boolean      |Срабатывает ли mmp.<br>`true`: значение `mmpFrozenUntil` имеет смысл.<br>`false`: значение `mmpFrozenUntil` следует игнорировать.                                             |
