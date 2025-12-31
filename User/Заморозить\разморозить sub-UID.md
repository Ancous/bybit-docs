- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос на замораживание или размораживание sub-UID

> Информация:
>
> Используется только API-ключ master-пользователя.
<!-- -->
> Важное замечание:
>
> API-ключ master-UID должен обладать одним из следующих разрешений для вызова этой конечной точки:
>
> - “Account Transfer”
> - “Subaccount Transfer”
> - “Withdrawal”

<a id="конечная-точка"></a>

## Конечная точка

`/v5/user/frozen-sub-member`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  POST /v5/user/frozen-sub-member HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1676430842094
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  
  {
      "subuid": 53888001,
      "frozen": 1
  }
  ```

- собственная реализация

  ```python
  import time
  import hmac
  import hashlib
  import json
  import requests
  
  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/user/frozen-sub-member"
  complete_request = base_url + end_point
  
  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"
  
  data = {
      "subuid": 53888001,
      "frozen": 1,
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
      api_secret="<secret_key от биржи bybit>",
  )
  print(session.freeze_sub_uid(
      subuid=53888001,
      frozen=1,
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

| Параметр   | Обязательный | Тип     | Комментарии                                                      | По умолчанию |
|------------|--------------|---------|------------------------------------------------------------------|--------------|
| subuid     | Да           | integer | ***Идентификатор sub-UID.***                                     | -            |
| frozen     | Да           | integer | ***Действие.***<br><br>-  `0`: разморозить<br>- `1`: заморозить  | -            |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "",
    "result": {},
    "retExtInfo": {},
    "time": 1676430697553
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

Отсутствуют
