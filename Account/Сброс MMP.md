- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос на сброс MMP

> Информация:
>
> - После срабатывания MMP вы можете разморозить счёт с помощью этой конечной точки, после чего значения `qtyLimit` и
>   `deltaLimit` будут сброшены до `0`.
> - Если счёт не заморожен, сброс также может удалить предыдущие накопления, т.е. значения `qtyLimit` и `deltaLimit`
>   будут сброшены до `0`.

## Конечная точка

`/v5/account/mmp-reset`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  POST /v5/account/mmp-reset HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1675842997277
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  
  {
      "baseCoin": "ETH"
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
  end_point = "/v5/account/mmp-reset"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "baseCoin": "ETH"
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
  print(session.reset_mmp(
      baseCoin="ETH",
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

| Параметр     | Обязательный  | Тип    | Комментарии                                                | По умолчанию |
|--------------|---------------|--------|------------------------------------------------------------|--------------|
| baseCoin     | да            | string | ***Базовая монета.***<br><br>- Только заглавными буквами   | -            |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "success"
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

Отсутствуют
