- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос конфигурации DCP для учётной записи.  
Перед вызовом интерфейса убедитесь, что вы подали заявку на настройку DCP для учётной записи UTA у своего менеджера
по работе с клиентами.

- Запросить информацию из этого API может только настроенный основной/дополнительный счёт. Вызов этого API из счёта
  всегда возвращает пустой результат.
- Если вы запрашиваете только активацию спотовой торговли для DCP, данные о контрактах и ​​опционах не будут возвращены.

>Зона применения:
>
>***UTA2.0:***
>
>`spot` - спот  
>`option` - опцион  
>`linear` - контракт (расчет в USDT, USDC, ...)
>
> - `Perpetual` - контракт без даты экспирации
> - `Futures` - контракт с датой экспирации
>
>`inverse` - контракт (расчет в BTC, ETH, ...)
>
> - `Perpetual` - контракт без даты экспирации
> - `Futures` - контракт с датой экспирации
>
>***UTA1.0:***
>
>`spot` - спот  
>`option` - опцион  
>`linear` - контракт (расчет в USDT, USDC, ...)
>
> - `Perpetual` - контракт без даты экспирации
> - `Futures` - контракт с датой экспирации
>

<a id="конечная-точка"></a>

## Конечная точка

`/v5/account/query-dcp-info`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/account/query-dcp-info HTTP/1.1
  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1717065530867
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
  end_point = "/v5/account/query-dcp-info"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  api_secret = "<api_secret от биржи bybit>"
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

  response = requests.get(url=complete_request, headers=headers, json=data, timeout=10)

  print(response.json())
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

Отсутствуют

<a id="пример-ответа"></a>

## Пример ответа

```json
// it means my account enables Spot and Deriviatvies on the backend
// Options is not enabled with DCP
{
    "retCode": 0,
    "retMsg": "success",
    "result": {
        "dcpInfos": [
            {
                "product": "SPOT",
                "dcpStatus": "ON",
                "timeWindow": "10"
            },
            {
                "product": "DERIVATIVES",
                "dcpStatus": "ON",
                "timeWindow": "10"
            }
        ]
    },
    "retExtInfo": {},
    "time": 1717065531697
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр  |Тип       |Комментарии                                             |
|----------|----------|--------------------------------------------------------|
|dcpInfos   |array      |Конфигурация DCP для каждого продукта                                             |
|product   |string      |`SPOT`, `DERIVATIVES`, `OPTIONS`                                             |
|dcpStatus   |string      |[Установить DCP](<../Trade/Установить DCP.md>) статус: `ON`.                                             |
|timeWindow   |string      |Временной интервал срабатывания DCP, который задаётся пользователем. Диапазон [`3`, `300`] секунд, по умолчанию: `10` секунд.       |
