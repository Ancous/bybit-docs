- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

> Информация:
>
> - master-UID может запрашивать лимит для себя и своих sub-UID.
> - sub-UID может запрашивать лимит только для себя.

<a id="конечная-точка"></a>

## Конечная точка

`/v5/apilimit/query`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/apilimit/query?uids=290118 HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1728460942776
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  Content-Length: 2
  ```

- собственная реализация

  ```python
  import time
  import hmac
  import hashlib
  import requests
  
  from urllib.parse import urlencode
  
  
  base_url = "https://api.bybit.com"
  end_point = "/v5/apilimit/query"
  complete_request = base_url + end_point
  
  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"
  
  data = {
    "uids": "290118"
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

<a id="параметры-запроса"></a>

## Параметры запроса

| Параметр | Обязательный | Тип    | Комментарии                               | По умолчанию |
|----------|--------------|--------|-------------------------------------------|--------------|
| uids     | да           | string | ***Несколько UID, разделённых запятыми*** | -            |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "success",
    "result": {
        "list": [
            {
                "uids": "290118",
                "bizType": "SPOT",
                "rate": 600
            },
            {
                "uids": "290118",
                "bizType": "DERIVATIVES",
                "rate": 400
            }
        ]
    },
    "retExtInfo": {},
    "time": 1754894341984
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

| Параметр                                                              | Тип     | Комментарии                                 |
|-----------------------------------------------------------------------|---------|---------------------------------------------|
| list                                                                  | array   | ***Массив объектов.***                      |
| uids                                                                  | string  | ***Несколько UID, разделённых запятыми.***  |
| [bizType](</19.Определения значений в запросах и ответах.md#bizType>) | string  | ***Тип бизнеса.***                          |
| rate                                                                  | integer | ***Лимит в секунду.***                      |
