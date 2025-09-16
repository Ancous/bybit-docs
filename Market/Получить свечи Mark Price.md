- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Примеры ответа](#примеры-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрашивает исторические свечей по
[mark price](https://www.bybit.com/en-US/help-center/s/article/Glossary-Bybit-Trading-Terms).
Графики возвращаются группами в зависимости от запрошенного интервала.

>Охватывает:
>
>USDT контракт / USDC контракт / Inverse контракт

## Конечная точка

`/v5/market/mark-price-kline`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```bash
  GET /v5/market/mark-price-kline?category=linear&symbol=BTCUSDT&interval=15&start=1670601600000&end=1670608800000&limit=1 HTTP/1.1
  Host: api-testnet.bybit.com
  ```

- Python

  ```python
  import requests

  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/market/mark-price-kline"

  complete_request = base_url + end_point
  parameters = {
      "category": "linear",
      "symbol": "BTCUSDT",
      "interval": "15",
      "start": 1670601600000,
      "end": 1670608800000,
      "limit": 1
  }
  
  response = requests.get(url=complete_request, params=parameters, timeout=10)

  print(response.json())
  ```

- pybit

  ```python
  from pybit.unified_trading import HTTP

  session = HTTP(testnet=True)
  print(session.get_mark_price_kline(
      category="linear",
      symbol="BTCUSDT",
      interval=15,
      start=1670601600000,
      end=1670608800000,
      limit=1,
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

|Параметр  	                                                            |Обязательный	 |Тип   	  |Комментарии                                         |По умолчанию|
|-----------------------------------------------------------------------|--------------|----------|----------------------------------------------------|------------|
|[category](<../99.Определения значений в запросах и ответах.md#category>)	  |нет           |string    |Тип продукта: `linear`, `inverse`                   |linear      |
|[symbol](<../99.Определения значений в запросах и ответах.md#symbol>)	      |да            |string    |Имя символа: `BTCUSDT`, только заглавными буквами   |-           |
|[interval](<../99.Определения значений в запросах и ответах.md#interval>)    |да            |string    |Интервал свечей                                     |-           |
|start	                                                                |нет      	   |integer   |Временная метка начала (мс)                         |-           |
|end                                                                    |нет      	   |integer   |Временная метка окончания (мс)                      |-           |
|limit	                                                                |нет      	   |integer   |Лимит на размер данных на страницу. [1, 1000]       |200         |

<a id="примеры-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "symbol": "BTCUSDT",
        "category": "linear",
        "list": [
            [
                "1670608800000",
                "17164.16",
                "17164.16",
                "17121.5",
                "17131.64"
            ]
        ]
    },
    "retExtInfo": {},
    "time": 1672026361839
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр  |Тип       |Комментарии                                                                                    |
|----------|----------|-----------------------------------------------------------------------------------------------|
|category  |string    |Тип продукта                                                                                   |
|symbol    |string    |Символ                                                                                         |
|list      |array     |Массив строк индивидуальных свечей.<br>Сортируется в обратном порядке по startTime             |
|list[0]   |string    |Время начала свечи (мс)                                                                        |
|list[1]   |string    |Цена открытия                                                                                  |
|list[2]   |string    |Максимальная цена                                                                              |
|list[3]   |string    |Минимальная цена                                                                               |
|list[4]   |string    |Цена закрытия. Является последней ценой сделки, если свеча не закрыта                          |
