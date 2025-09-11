- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Примеры ответа](#примеры-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="конечная-точка"></a>

#### Конечная точка<p id="id71"></p>

`/v5/market/time`

<a id="примеры-запроса"></a>

#### Примеры запроса<p id="id72"></p>

- HTTP

  ```bash
  GET /v5/market/time HTTP/1.1
  Host: api.bybit.com
  ```

- Python

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

#### Параметры запроса<p id="id73"></p>

none

<a id="примеры-ответа"></a>

#### Пример ответа<p id="id74"></p>

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

#### Параметры ответа<p id="id75"></p>

|Параметр	   |Тип       |Комментарии                        |
|--------------|----------|-----------------------------------|
|timeSecond    |string    |Время сервера Bybit (секунды)      |
|timeNano      |string    |Время сервера Bybit (наносекунды)  |
