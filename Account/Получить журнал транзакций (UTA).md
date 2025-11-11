- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос журнала транзакций в вашей единой учётной записи. Поддерживаются данные за период до 2 лет.

>Зона применения:  
>
>`spot` - спот  
>`option` - опцион  
>`linear` - контракт (расчет в USDT, USDC, ...)
>
> - `Perpetual` - контракт без даты экспирации
> - `Futures` - контракт с датой экспирации
>

<a id="конечная-точка"></a>

## Конечная точка

`/v5/account/transaction-log`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/account/transaction-log?accountType=UNIFIED&category=linear&currency=USDT HTTP/1.1
  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1672132480085
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
  end_point = "/v5/account/transaction-log"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  api_secret = "<api_secret от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "accountType": "UNIFIED",
      "category": "linear",
      "currency": "USDT",
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

- pybit

  ```python
  from pybit.unified_trading import HTTP

  session = HTTP(
      testnet=True,
      api_key="<api_key от биржи bybit>",
      api_secret="<api_secret от биржи bybit>",
  )
  print(session.get_transaction_log(
      accountType="UNIFIED",
      category="linear",
      currency="USDT",
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

|Параметр  	                  |Обязательный	 |Тип  	  |Комментарии       |По умолчанию|
|-----------------------------|--------------|--------|------------------|------------|
|[accountType](<../19.Определения значений в запросах и ответах.md#accountType>)        |нет  |string    |***Тип аккаунта***<br><br>`UNIFIED`      |-   |
|[category](<../19.Определения значений в запросах и ответах.md#category>)	|да           |string    |***Тип продукта.***<br><br>- [UTA2.0](<../13.Различные режимы аккаунтов.md#единый-торговый-аккаунт-2.0>): `spot`, `option`, `linear`, `inverse`<br>- [UTA1.0](<../13.Различные режимы аккаунтов.md#единый-торговый-аккаунт-1.0>): `spot`, `option`, `linear`  |-   |
|currency                     |нет  |string     |***Валюта актива***<br><br>Только заглавными буквами        |-   |
|baseCoin                     |нет  |string     |***Базовая монета***<br><br>Только заглавными буквами         |По умолчанию|
|[type](<../19.Определения значений в запросах и ответах.md#type(uta-translog)>)                     |нет  |string     |***Типы журналов транзакций***       |-   |
|startTime                     |нет  |integer     |Комментарии       |По умолчанию|
|endTime                     |нет  |integer     |Комментарии       |По умолчанию|
|limit                     |нет  |string     |Комментарии        |По умолчанию|
|cursor                     |нет  |string     |Комментарии        |По умолчанию|

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "nextPageCursor": "21963%3A1%2C14954%3A1",
        "list": [
            {
                "transSubType": "",
                "id": "592324_XRPUSDT_161440249321",
                "symbol": "XRPUSDT",
                "side": "Buy",
                "funding": "-0.003676",
                "orderLinkId": "",
                "orderId": "1672128000-8-592324-1-2",
                "fee": "0.00000000",
                "change": "-0.003676",
                "cashFlow": "0",
                "transactionTime": "1672128000000",
                "type": "SETTLEMENT",
                "feeRate": "0.0001",
                "bonusChange": "",
                "size": "100",
                "qty": "100",
                "cashBalance": "5086.55825002",
                "currency": "USDT",
                "category": "linear",
                "tradePrice": "0.3676",
                "tradeId": "534c0003-4bf7-486f-aa02-78cee36825e4",
                "extraFees": ""
            },
            {
                "transSubType": "",
                "id": "592324_XRPUSDT_161440249321",
                "symbol": "XRPUSDT",
                "side": "Buy",
                "funding": "",
                "orderLinkId": "linear-order",
                "orderId": "592b7e41-78fd-42e2-9aa3-91e1835ef3e1",
                "fee": "0.01908720",
                "change": "-0.0190872",
                "cashFlow": "0",
                "transactionTime": "1672121182224",
                "type": "TRADE",
                "feeRate": "0.0006",
                "bonusChange": "-0.1430544",
                "size": "100",
                "qty": "88",
                "cashBalance": "5086.56192602",
                "currency": "USDT",
                "category": "linear",
                "tradePrice": "0.3615",
                "tradeId": "5184f079-88ec-54c7-8774-5173cafd2b4e",
                "extraFees": ""
            },
            {
                "transSubType": "",
                "id": "592324_XRPUSDT_161407743011",
                "symbol": "XRPUSDT",
                "side": "Buy",
                "funding": "",
                "orderLinkId": "linear-order",
                "orderId": "592b7e41-78fd-42e2-9aa3-91e1835ef3e1",
                "fee": "0.00260280",
                "change": "-0.0026028",
                "cashFlow": "0",
                "transactionTime": "1672121182224",
                "type": "TRADE",
                "feeRate": "0.0006",
                "bonusChange": "",
                "size": "12",
                "qty": "12",
                "cashBalance": "5086.58101322",
                "currency": "USDT",
                "category": "linear",
                "tradePrice": "0.3615",
                "tradeId": "8569c10f-5061-5891-81c4-a54929847eb3",
                "extraFees": ""
            }
        ]
    },
    "retExtInfo": {},
    "time": 1672132481405
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр  |Тип       |Комментарии                                             |
|----------|----------|--------------------------------------------------------|
|Параметр   |Тип      |Комментарии                                             |
|Параметр   |Тип      |Комментарии                                             |
|Параметр   |Тип      |Комментарии                                             |
