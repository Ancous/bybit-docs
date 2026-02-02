- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос на удаление API-key sub-UID.  
Для вызова этой конечной точки используйте либо API-key sub-UID, который требуется удалить, либо API-key master-UID для
удаления соответствующего ключа sub-аккаунта.

> Важное замечание:
>
> API-key должен обладать одним из следующих разрешений для вызова этой конечной точки:
>
> - Для API-key sub-UID:
>   - "Account Transfer"
>   - "Sub Member Transfer"
>
> - Для API-key master-UID:
>   - "Account Transfer"
>   - "Sub Member Transfer"
>   - "Withdrawal"
<!-- -->
> ⚠️ ОПАСНОСТЬ!
>
> БУДЬТЕ ОСТОРОЖНЫ! API-key sub-UID будет немедленно удален после вызова этой конечной точки.

<a id="конечная-точка"></a>

## Конечная точка

`/v5/user/delete-sub-api`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  POST /v5/user/delete-sub-api HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1676431922953
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  
  {}
  ```

- собственная реализация

  ```python
  import time
  import hmac
  import hashlib
  import json
  import requests
  
  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/user/delete-sub-api"
  complete_request = base_url + end_point
  
  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"
  
  data = {}
  
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
  print(session.delete_sub_api_key())
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

| Параметр | Обязательный | Тип    | Комментарии                                                                                                                                                                                                                            | По умолчанию |
|----------|--------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| apikey   | нет          | string | ***Sub-UID API-key.***<br><br>- Обязательно передавайте, если вы используете master-UID для управления настройками sub-UID API-key<br>- Нельзя передавать, если вы вызываете эндпоинт с соответствующим sub-UID API-key (будет ошибка) | -            |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "",
    "result": {},
    "retExtInfo": {},
    "time": 1676431924719
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

Отсутствуют
