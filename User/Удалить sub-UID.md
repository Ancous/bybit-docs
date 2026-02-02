- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос на удаление sub-UID. Перед удалением sub-UID убедитесь, что на нём нет активов. Используется только
API-key master-UID.

> Важное замечание:
>
> API-key master-UID должен обладать одним из следующих разрешений для вызова этой конечной точки:
>
> - "Account Transfer"
> - "Subaccount Transfer"
> - "Withdrawal"

<a id="конечная-точка"></a>

## Конечная точка

`/v5/user/del-submember`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  POST /v5/user/del-submember HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1698907012755
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  Content-Length: 34
  
  {
      "subMemberId": "112725187"
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
  end_point = "/v5/user/del-submember"
  complete_request = base_url + end_point
  
  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"
  
  data = {
      "subMemberId": "112725187"
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

| Параметр     | Обязательный  | Тип      | Комментарии       | По умолчанию |
|--------------|---------------|----------|-------------------|--------------|
| subMemberId  | да            | string   | ***Sub-UID.***    | -            |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {},
    "retExtInfo": {},
    "time": 1698907012962
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

Отсутствуют
