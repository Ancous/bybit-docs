- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос на удаление API-key master-UID.  
Для вызова этой конечной точки используйте API-key, который требуется удалить.  
Используется только API-key master-UID.

> Важное замечание:
>
> API-key master-UID должен обладать одним из следующих разрешений для вызова этой конечной точки:
>
> - “Account Transfer”
> - “Subaccount Transfer”
> - “Withdrawal”
<!-- -->
> ⚠️ ОПАСНОСТЬ!
>
> БУДЬТЕ ОСТОРОЖНЫ!!! API-key, использованный для вызова этой конечной точки, будет немедленно удален.

<a id="конечная-точка"></a>

## Конечная точка

`/v5/user/delete-api`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  POST /v5/user/delete-api HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1676431576621
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
  end_point = "/v5/user/delete-api"
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
  print(session.delete_master_api_key())
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
    "time": 1676431577675
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

Отсутствуют
