- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос журналов транзакций в кошельке деривативов (классический счет) и счете обратных деривативов (обновленном до UTA)

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

`/v5/account/contract-transaction-log`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/account/contract-transaction-log?limit=1&symbol=BTCUSD HTTP/1.1
  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1714035117255
  X-BAPI-RECV-WINDOW: 5000
  ```

- requests

  ```python
  import time
  import hmac
  import hashlib
  import requests

  from urllib.parse import urlencode

  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/account/contract-transaction-log"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  api_secret = "<api_secret от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "accountType": "UNIFIED",
      "coin": "BTC",
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

  response = requests.get(url=complete_request, headers=headers, json=data, timeout=10)

  print(response.json())
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

|Параметр  	                  |Обязательный	 |Тип  	  |Комментарии       |По умолчанию|
|-----------------------------|--------------|--------|------------------|------------|
|Параметр                     |нет  |string     |Комментарии       |По умолчанию|
|Параметр                     |нет  |string     |Комментарии       |По умолчанию|
|Параметр                     |нет  |string     |Комментарии       |По умолчанию|
|Параметр                     |нет  |integer     |Комментарии       |По умолчанию|
|Параметр                     |нет  |integer     |Комментарии       |По умолчанию|
|Параметр                     |нет  |integer     |Комментарии       |По умолчанию|
|Параметр                     |нет  |string     |Комментарии       |По умолчанию|

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "list": [
            {
                "id": "467153",
                "symbol": "BTCUSD",
                "category": "inverse",
                "side": "Sell",
                "transactionTime": "1714032000000",
                "type": "SETTLEMENT",
                "qty": "1000",
                "size": "-1000",
                "currency": "BTC",
                "tradePrice": "63974.88",
                "funding": "-0.00000156",
                "fee": "",
                "cashFlow": "0.00000000",
                "change": "0.00000156",
                "cashBalance": "1.1311",
                "feeRate": "-0.00010000",
                "bonusChange": "",
                "tradeId": "423a565c-f1b6-4c81-bc62-760cd7dd89e7",
                "orderId": "",
                "orderLinkId": ""
            }
        ],
        "nextPageCursor": "cursor_id%3D467153%26"
    },
    "retExtInfo": {},
    "time": 1714035117258
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр  |Тип       |Комментарии                                             |
|----------|----------|--------------------------------------------------------|
|Параметр   |Тип      |Комментарии                                             |
|Параметр   |Тип      |Комментарии                                             |
|Параметр   |Тип      |Комментарии                                             |
