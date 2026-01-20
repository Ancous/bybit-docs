- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос на подтверждения нового risk limit

>Зона применения:  
>
>`linear` - контракт (расчет в USDT, USDC, ...)
>
> - `Perpetual` - контракт без даты экспирации
> - `Futures` - контракт с датой экспирации
>
>`inverse` - контракт (расчет в BTC, ETH, ...)
>
> - `Perpetual` - контракт без даты экспирации
> - `Futures` - контракт с датой экспирации
<!-- -->
>Информация:
>
>Применимо только в том случае, если пользователь отмечен `isReduceOnly`=`True` в ответе на запрос
>[Получить информацию о позиции](<Получить информацию о позиции.md>). После того, как пользователь активно корректирует
>уровень риска, этот интерфейс вызывается для попытки рассчитать скорректированный risk limit, и если это проверка
>проходит успешно (`retCode`=`0`), система поменяет отметку `isReduceOnly`=`True` на `isReduceOnly`=`False` в ответе на
>запрос [Получить информацию о позиции](<Получить информацию о позиции.md>).
>
>Рекомендуется вызвать функцию [Получить информацию о позиции](<Получить информацию о позиции.md>) для проверки
>поля `isReduceOnly`.

<a id="конечная-точка"></a>

## Конечная точка

`/v5/position/confirm-pending-mmr`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  POST /v5/position/confirm-pending-mmr HTTP/1.1
  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1698051123673
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  Content-Length: 53
  
  {
      "category": "linear",
      "symbol": "BTCUSDT"
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
  end_point = "/v5/position/confirm-pending-mmr"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "category": "linear",
      "symbol": "BTCUSDT",
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

| Параметр                                                                 | Обязательный  | Тип    | Комментарии                                                                                                                                                                                                                                           | По умолчанию |
|--------------------------------------------------------------------------|---------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [category](</19.Определения значений в запросах и ответах.md#category>)  | да            | string | ***Тип продукта.***<br><br>- классический аккаунт: `linear`, `inverse`<br>- [UTA2.0](</13.Различные режимы аккаунтов.md#единый-торговый-аккаунт-2.0>), [UTA1.0](</13.Различные режимы аккаунтов.md#единый-торговый-аккаунт-1.0>): `linear`, `inverse` | -            |
| [symbol](</19.Определения значений в запросах и ответах.md#symbol>)      | да            | string | ***Имя символа.***<br><br>- Только заглавными буквами                                                                                                                                                                                                 | -            |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {},
    "retExtInfo": {},
    "time": 1698051124588
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

Отсутствуют
