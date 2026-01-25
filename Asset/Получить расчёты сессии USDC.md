- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос записей о расчётах сессии USDC бессрочных контрактов и фьючерсов.

> Зона применения:  
>
> `linear` - контракт (расчет в USDT, USDC, ...)
>
> - `Perpetual` - контракт без даты экспирации
> - `Futures` - контракт с датой экспирации

<a id="конечная-точка"></a>

## Конечная точка

`/v5/asset/settlement-record`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/asset/settlement-record?category=linear HTTP/1.1
  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1672284883483
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
  end_point = "/v5/asset/settlement-record"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "category": "linear",
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

  response = requests.get(url=complete_request, headers=headers, params=data, timeout=10)

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
  print(session.get_usdc_contract_settlement(
      category="linear",
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

| Параметр                                                                | Обязательный  | Тип     | Комментарии                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | По умолчанию     |
|-------------------------------------------------------------------------|---------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| [category](</19.Определения значений в запросах и ответах.md#category>) | да            | string  | ***Тип продукта.***<br><br>- `linear`                                                                                                                                                                                                                                                                                                                                                                                                                                                               | -                |
| [symbol](</19.Определения значений в запросах и ответах.md#symbol>)     | нет           | string  | ***Имя символа.***<br><br>- Только заглавными буквами<br>- Пример: `BTCPERP`                                                                                                                                                                                                                                                                                                                                                                                                                        | -                |
| startTime                                                               | нет           | integer | ***Временная метка начала выборки (в миллисекундах).***<br><br>- **Если `startTime` и `endTime` не передаются**:<br>&nbsp;&nbsp;&nbsp;по умолчанию возвращается 30 дней<br>- **Если передан только `startTime`**:<br>&nbsp;&nbsp;&nbsp;возвращается диапазон между `startTime` + 30 дней<br>- **Если передан только `endTime`**:<br>&nbsp;&nbsp;&nbsp;возвращается диапазон между `endTime` - 30 дней.<br>- **Если переданы оба**:<br>&nbsp;&nbsp;&nbsp;правило: `endTime` - `startTime` <= 30 дней | -                |
| endTime                                                                 | нет           | integer | ***Временная метка конца выборки (в миллисекундах).***                                                                                                                                                                                                                                                                                                                                                                                                                                              | -                |
| limit                                                                   | нет           | integer | ***Ограничение размера данных на странице.***<br><br>- [`1`, `50`]                                                                                                                                                                                                                                                                                                                                                                                                                                  | `20`             |
| cursor                                                                  | нет           | string  | ***Курсор.***<br><br>- Используйте значение `nextPageCursor` из ответа для получения следующей страницы набора результатов                                                                                                                                                                                                                                                                                                                                                                          | -                |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "nextPageCursor": "116952%3A1%2C116952%3A1",
        "category": "linear",
        "list": [
            {
                "realisedPnl": "-71.28",
                "symbol": "BTCPERP",
                "side": "Buy",
                "markPrice": "16620",
                "size": "1.5",
                "createdTime": "1672214400000",
                "sessionAvgPrice": "16620"
            }
        ]
    },
    "retExtInfo": {},
    "time": 1672284884285
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

| Параметр        | Тип    | Комментарии                                                                                          |
|-----------------|--------|------------------------------------------------------------------------------------------------------|
| category        | string | ***Тип продукта.***                                                                                  |
| list            | array  | ***Массив объектов.***                                                                               |
| symbol          | string | ***Название инструмента.***                                                                          |
| side            | string | ***Сторона.***<br><br>- `Buy`,`Sell`                                                                 |
| size            | string | ***Размер позиции.***                                                                                |
| sessionAvgPrice | string | ***Расчетная цена.***                                                                                |
| markPrice       | string | ***Mark Price.***                                                                                    |
| realisedPnl     | string | ***Реализованный PnL.***                                                                             |
| createdTime     | string | ***Временная метка создания ордера (в миллисекундах).***                                             |
| nextPageCursor  | string | ***Метка для следующей страницы.***<br><br>- Используется в параметре запроса `cursor` для пагинации |
