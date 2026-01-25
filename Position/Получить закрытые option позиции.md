- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос на получение полной информации о каждой закрытой позиций по `option`, отсортированных по времени закрытия в порядке убывания.

> Зона применения:  
>
> `option` - опцион  
<!-- -->
> Информация:
>
> - Поддерживает только запросы по закрытым `option` позициям за последние 6 месяцев.
> - Комиссия и цена отображаются с конечными нулями до 8 знаков после запятой.

<a id="конечная-точка"></a>

## Конечная точка

`/v5/position/get-closed-positions`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/position/get-closed-positions?category=option&limit=1 HTTP/1.1
  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1672284128523
  X-BAPI-RECV-WINDOW: 5000
  ```

- собственная реализация

  ```python
  import time
  import hmac
  import hashlib
  import json

  from urllib.parse import urlencode

  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/position/get-closed-positions"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "category": "spot",
      "symbol": "BTCUSDT",
      "side": "Buy",
      "orderType": "Limit",
      "qty": "0.1",
      "price": "15600",
      "timeInForce": "PostOnly",
      "orderLinkId": "spot-test-postonly",
      "isLeverage": 0,
      "orderFilter": "Order"
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

<a id="параметры-запроса"></a>

## Параметры запроса

| Параметр                                                                 | Обязательный  | Тип     | Комментарии                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | По умолчанию |
|--------------------------------------------------------------------------|---------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| [category](</19.Определения значений в запросах и ответах.md#category>)  | да            | string  | ***Тип продукта.***<br><br>- `option`                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `option`     |
| [symbol](</19.Определения значений в запросах и ответах.md#symbol>)      | нет           | string  | ***Имя символа.***<br><br>- Только заглавными буквами                                                                                                                                                                                                                                                                                                                                                                                                                                           | -            |
| startTime                                                                | нет           | integer | ***Временная метка начала выборки (в миллисекундах).***<br><br>- **Если `startTime` и `endTime` не передаются**:<br>&nbsp;&nbsp;&nbsp;по умолчанию возвращается 7 дней<br>- **Если передан только `startTime`**:<br>&nbsp;&nbsp;&nbsp;возвращается диапазон между `startTime` + 7 дней<br>- **Если передан только `endTime`**:<br>&nbsp;&nbsp;&nbsp;возвращается диапазон между `endTime` - 7 дней.<br>- **Если переданы оба**:<br>&nbsp;&nbsp;&nbsp;правило: `endTime` - `startTime` <= 7 дней | -            |
| endTime                                                                  | нет           | integer | ***Временная метка конца выборки (в миллисекундах).***                                                                                                                                                                                                                                                                                                                                                                                                                                          | -            |
| limit                                                                    | нет           | integer | ***Ограничение размера данных на странице.***<br><br>- [`1`, `100`]                                                                                                                                                                                                                                                                                                                                                                                                                             | `50`         |
| cursor                                                                   | нет           | string  | ***Курсор.***<br><br>- Используйте значение `nextPageCursor` из ответа для получения следующей страницы набора результатов                                                                                                                                                                                                                                                                                                                                                                      | -            |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "nextPageCursor": "1749726002161%3A0%2C1749715220240%3A1",
        "category": "option",
        "list": [
            {
                "symbol": "BTC-12JUN25-104019-C-USDT",
                "side": "Sell",
                "totalOpenFee": "0.94506647",
                "deliveryFee": "0.32184533",
                "totalCloseFee": "0.00000000",
                "qty": "0.02",
                "closeTime": 1749726002161,
                "avgExitPrice": "107281.77405000",
                "deliveryPrice": "107281.77405031",
                "openTime": 1749722990063,
                "avgEntryPrice": "3371.50000000",
                "totalPnl": "0.90760719"
            },
            {
                "symbol": "BTC-12JUN25-104000-C-USDT",
                "side": "Buy",
                "totalOpenFee": "0.86379999",
                "deliveryFee": "0.32287622",
                "totalCloseFee": "0.00000000",
                "qty": "0.02",
                "closeTime": 1749715220240,
                "avgExitPrice": "107625.40470150",
                "deliveryPrice": "107625.40470159",
                "openTime": 1749710568608,
                "avgEntryPrice": "3946.50000000",
                "totalPnl": "-7.60858218"
            }
        ]
    },
    "retExtInfo": {},
    "time": 1749736532193
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

| Параметр                                                                | Тип     | Комментарии                                                                                          |
|-------------------------------------------------------------------------|---------|------------------------------------------------------------------------------------------------------|
| [category](</19.Определения значений в запросах и ответах.md#category>) | string  | ***Тип продукта.***                                                                                  |
| list                                                                    | array   | ***Массив объектов.***                                                                               |
| symbol                                                                  | string  | ***Название символа.***                                                                              |
| side                                                                    | string  | ***Сторона сделки.***<br><br>- `Buy`<br>- `Sell`                                                     |
| totalOpenFee                                                            | string  | ***Общая комиссия за открытие.***                                                                    |
| deliveryFee                                                             | string  | ***Плата за экспирацию.***                                                                           |
| totalCloseFee                                                           | string  | ***Общая комиссия за закрытие.***                                                                    |
| qty                                                                     | string  | ***Количество ордера.***                                                                             |
| closeTime                                                               | integer | ***Время закрытия (в миллисекундах).***                                                              |
| avgExitPrice                                                            | string  | ***Средняя цена выхода.***                                                                           |
| deliveryPrice                                                           | string  | ***Цена экспирации.***                                                                               |
| openTime                                                                | integer | ***Время открытия (в миллисекундах).***                                                              |
| avgEntryPrice                                                           | string  | ***Средняя цена входа.***                                                                            |
| totalPnl                                                                | string  | ***Общий PnL.***                                                                                     |
| nextPageCursor                                                          | string  | ***Метка для следующей страницы.***<br><br>- Используется в параметре запроса `cursor` для пагинации |
