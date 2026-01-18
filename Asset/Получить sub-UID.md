- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос sub-UID, принадлежащие master-UID. Возвращает до 2000 sub-UID. Если вам нужно больше, пожалуйста,
обратитесь к этой [конечной точке USER](#).

<a id="конечная-точка"></a>

## Конечная точка

`/v5/asset/transfer/query-sub-member-list`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/asset/transfer/query-sub-member-list HTTP/1.1
  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1672147239931
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
  end_point = "/v5/asset/transfer/query-sub-member-list"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
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
  print(session.get_sub_uid())
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

Отсутствуют

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "success",
    "result": {
        "subMemberIds": [
            "554117",
            "592324",
            "592334",
            "1055262",
            "1072055",
            "1119352"
        ],
        "transferableSubMemberIds": [
            "554117",
            "592324"
        ]
    },
    "retExtInfo": {},
    "time": 1672147241320
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

| Параметр                 | Тип   | Комментарии                                                    |
|--------------------------|-------|----------------------------------------------------------------|
| subMemberIds             | array | ***Все sub-UID master-UID.***                                  |
| transferableSubMemberIds | array | ***Все sub-UID, для которых разрешен универсальный перевод.*** |
