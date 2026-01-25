- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Получить доступные типы кошельков для master-аккаунта или sub-аккаунта

> Важное замечание:
>
> - Для master API-ключа: можно получить доступные типы кошельков как для master-аккаунта, так и для указанного
>   sub-аккаунта. В одном запросе поддерживается до 200 sub-UID.
> - Для sub API-ключа: можно получить только свои собственные доступные типы кошельков.

<a id="конечная-точка"></a>

## Конечная точка

`v5/user/get-member-type`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/user/get-member-type HTTP/1.1
  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1686884973961
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/jsonb
  ```

- собственная реализация

  ```python
  import time
  import hmac
  import hashlib
  import requests
  
  from urllib.parse import urlencode
  
  base_url = "https://api-testnet.bybit.com"
  end_point = "v5/user/get-member-type"
  complete_request = base_url + end_point
  
  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"
  
  data = {}
  
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

|Параметр                     |Обязательный  |Тип     |Комментарии       |По умолчанию|
|-----------------------------|--------------|--------|------------------|------------|
|memberIds                    |нет           |string  |***Идентификаторы участников.***<br><br>- Если параметр не передан, запрос возвращает типы кошельков текущего аккаунта (того, чей API-ключ используется)<br>- При использовании master API-ключа для запроса sub-UID, данные master-UID всегда возвращаются первым элементом массива<br>- Поддерживается запрос нескольких sub-UID, перечисленных через запятую<br>- Этот параметр игнорируется, если используется API-ключ sub-аккаунта       | -   |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "",
    "result": {
        "accounts": [
            {
                "uid": "533285",
                "accountType": [
                    "UNIFIED",
                    "FUND"
                ]
            }
        ]
    },
    "retExtInfo": {},
    "time": 1686884974151
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр   |Тип       |Комментарии                                             |
|-----------|----------|--------------------------------------------------------|
|accounts   |array       |***Массив объектов.***                                             |
|uid   |string       |***Идентификатор пользователя.***<br><br>- Master-UID Sub-UID                                             |
|accountType   |array       |***Массив доступных типов кошельков.***<br><br>- `FUND`: Фондирующий<br>- `UNIFIED` Единый                                             |
