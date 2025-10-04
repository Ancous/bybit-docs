- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос серверного времени

<a id="конечная-точка"></a>

## Конечная точка

`/v5/market/time`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/market/time HTTP/1.1
  Host: api.bybit.com
  ```

- requests

  ```python
  import requests

  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/market/time"

  complete_request = base_url + end_point

  response = requests.get(url=complete_request, timeout=10)

  print(response.json())
  ```

- pybit

  ```python
  from pybit.unified_trading import HTTP
  
  session = HTTP(testnet=True)
  print(session.get_server_time())
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

Отсутствуют

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "timeSecond": "1757404648",
        "timeNano": "1757404648942446966"
    },
    "retExtInfo": {},
    "time": 1757404648942
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр	     |Тип       |Комментарии                        |
|--------------|----------|-----------------------------------|
|timeSecond    |string    |Время сервера Bybit (секунды)      |
|timeNano      |string    |Время сервера Bybit (наносекунды)  |
