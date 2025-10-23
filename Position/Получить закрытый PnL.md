- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос на получение реализованного PnL по каждой закрытой позиций пользователя

>Зона применения:  
>
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
<!-- -->
>Информация:
>
>- Классический счёт: результаты сортируются по `updatedTime` в порядке убывания.
>- [UTA2.0](<../13.Различные режимы аккаунтов.md#единый-торговый-аккаунт-2.0>),
> [UTA1.0](<../13.Различные режимы аккаунтов.md#единый-торговый-аккаунт-1.0>) (кроме `inverse`): результаты сортируются
> `createdTime` в порядке убывания, впоследствии это значение будет постоянным для классического счёта.
>- [UTA2.0](<../13.Различные режимы аккаунтов.md#единый-торговый-аккаунт-2.0>),
> [UTA1.0](<../13.Различные режимы аккаунтов.md#единый-торговый-аккаунт-1.0>) (кроме `inverse`): поддерживают получение
> исторических данных за последние 730 дней.

<a id="конечная-точка"></a>

## Конечная точка

`/v5/position/closed-pnl`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/position/closed-pnl?category=linear&limit=1 HTTP/1.1
  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1672284128523
  X-BAPI-RECV-WINDOW: 5000
  ```

- requests

  ```python
  import time
  import hmac
  import hashlib
  import requests

  from urllib.parse import urlencode

  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/position/closed-pnl"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  secret_key = "<api_secret от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "category": "linear",
      "limit": 1,
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
      api_secret="<api_secret от биржи bybit>",
  )
  print(session.get_closed_pnl(
      category="linear",
      limit=1,
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

|Параметр  	                  |Обязательный	 |Тип  	  |Комментарии &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;               |По умолчанию|
|-----------------------------|------------|----------|---------------------------|------------|
|[category](<../19.Определения значений в запросах и ответах.md#category>)	|да           |string    |***Тип продукта.***<br><br>- классический аккаунт: `linear`, `inverse`<br>- [UTA2.0](<../13.Различные режимы аккаунтов.md#единый-торговый-аккаунт-2.0>), [UTA1.0](<../13.Различные режимы аккаунтов.md#единый-торговый-аккаунт-1.0>): `linear`, `inverse`, `option`  |-   |
|[symbol](<../19.Определения значений в запросах и ответах.md#symbol>)	    |нет            |string    |***Имя символа.***<br><br>Только заглавными буквами |-   |
|startTime                     |нет  |integer     |***Временная метка начала выборки (в миллисекундах)***<br><br>- Если `startTime` и `endTime` не передаются, по умолчанию<br>&nbsp;&nbsp;&nbsp;возвращается 7 дней.<br>- Если передан только `startTime`, возвращается диапазон между<br>&nbsp;&nbsp;&nbsp;`startTime` и `startTime` + 7 дней<br>- Если передан только `endTime`, возвращается диапазон между<br>&nbsp;&nbsp;&nbsp;`endTime` - 7 дней и `endTime`<br>- Если переданы оба, правило: `endTime` - `startTime` <= 7 дней       |-   |
|endTime                     |нет  |integer     |Временная метка конца выборки (в миллисекундах)       |-   |
|limit                     |нет  |integer     |Ограничение размера данных на странице. [`1`, `100`]       |`50`   |
|cursor                     |нет  |string     |Курсор. Используйте значение `nextPageCursor` из ответа для получения следующей страницы набора результатов       |-   |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "nextPageCursor": "5a373bfe-188d-4913-9c81-d57ab5be8068%3A1672214887231423699%2C5a373bfe-188d-4913-9c81-d57ab5be8068%3A1672214887231423699",
        "category": "linear",
        "list": [
            {
                "symbol": "ETHPERP",
                "orderType": "Market",
                "leverage": "3",
                "updatedTime": "1672214887236",
                "side": "Sell",
                "orderId": "5a373bfe-188d-4913-9c81-d57ab5be8068",
                "closedPnl": "-47.4065323",
                "avgEntryPrice": "1194.97516667",
                "qty": "3",
                "cumEntryValue": "3584.9255",
                "createdTime": "1672214887231",
                "orderPrice": "1122.95",
                "closedSize": "3",
                "avgExitPrice": "1180.59833333",
                "execType": "Trade",
                "fillCount": "4",
                "cumExitValue": "3541.795"
            }
        ]
    },
    "retExtInfo": {},
    "time": 1672284129153
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр  |Тип       |Комментарии                                             |
|----------|----------|--------------------------------------------------------|
|[category](<../19.Определения значений в запросах и ответах.md#category>)   |string      |Тип продукта               |
|list   |array      |Массив объектов                                             |
|symbol   |string      |Название символа                                             |
|orderId   |string      |Идентификатор ордера                                             |
|side   |string      |Сторона сделки<br>- `Buy`<br>- `Sell`                                             |
|qty   |string      |Количество ордера                                             |
|orderPrice   |string      |Цена сделки                                             |
|[orderType](<../19.Определения значений в запросах и ответах.md#orderType>)   |string      |Тип ордера<br>- `Market`<br>- `Limit`             |
|execType   |string      |Тип исполнения<br>- `Trade`<br>- `BustTrade`<br>- `SessionSettlePnL`<br>- `Settle`<br>- `MovePosition`                                             |
|closedSize   |string      |Размер закрытой позиции                                             |
|cumEntryValue   |string      |Суммарное значение позиции                                             |
|avgEntryPrice   |string      |Средняя цена входа                                             |
|cumExitValue   |string      |Накопленная стоимость позиции выхода                                             |
|avgExitPrice   |string      |Средняя цена выхода                                             |
|closedPnl   |string      |Закрытый PnL                                             |
|fillCount   |string      |Количество заполнений в одном заказе                                             |
|leverage   |string      |Кредитное плечо                                             |
|openFee   |string      |Комиссия за открытые позиции                                             |
|closeFee   |string      |Комиссия за закрытие позиции                                             |
|createdTime     |string    |Временная метка создания ордера (в миллисекундах)|
|updatedTime     |string    |Временная метка обновления ордера (в миллисекундах)|
|nextPageCursor   |string      |Метка для следующей страницы (используется в параметре запроса `cursor` для пагинации)                                             |
