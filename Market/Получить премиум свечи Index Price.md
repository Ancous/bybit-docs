- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Примеры ответа](#примеры-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос исторических свечей
[премиум индексных цен](https://www.bybit.com/data/basic/linear/index-price/premium-index?symbol=BTCUSDT). Графики
возвращаются группами на основе заданного интервала.

>Охватывает:  
>USDT контракт / USDC контракт

## Конечная точка

`/v5/market/premium-index-price-kline`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```bash
  GET /v5/market/premium-index-price-kline?category=linear&symbol=BTCUSDT&interval=D&start=1652112000000&end=1652544000000 HTTP/1.1
  Host: api-testnet.bybit.com
  ```

- Python

  ```python
  import requests

  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/market/premium-index-price-kline"

  complete_request = base_url + end_point
  parameters = {
      "category": "linear",
      "symbol": "BTCUSDT",
      "interval": "D",
      "start": 1652112000000,
      "end": 1652544000000
  }
  
  response = requests.get(url=complete_request, params=parameters, timeout=10)

  print(response.json())
  ```

- pybit

  ```python
  from pybit.unified_trading import HTTP

  session = HTTP()
  print(session.get_premium_index_price_kline(
      category="linear",
      symbol="BTCUSDT",
      interval="D",
      start=1652112000000,
      end=1652544000000,
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

|Параметр  	         	         	         	         	            |Обязательный	 |Тип   	|Комментарии                                           |По умолчанию   |
|-----------------------------------------------------------------------|----------------|----------|------------------------------------------------------|---------------|
|[category](<../20.Определения значений в запросах и ответах.md#category>)	|нет             |string    |Тип продукта: `linear`                                |-              |
|[symbol](<../20.Определения значений в запросах и ответах.md#symbol>)	    |да              |string    |Имя символа: `BTCUSDT`, только заглавными буквами     |-              |
|[interval](<../20.Определения значений в запросах и ответах.md#interval>)    |да              |string    |Интервал свечей                                       |-              |
|start	         	         	         	         	                |нет      	     |integer   |Временная метка начала (мс)                           |-              |
|end            	         	         	         	                |нет          	 |integer   |Временная метка окончания (мс)                        |-              |
|limit	          	         	         	         	                |нет         	 |integer   |Лимит на размер данных на страницу. [1, 1000]         |200            |

<a id="примеры-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "symbol": "BTCUSDZ22",
        "category": "inverse",
        "list": [
            [
                "1670608800000",
                "17167.00",
                "17167.00",
                "17161.90",
                "17163.07"
            ],
            [
                "1670608740000",
                "17166.54",
                "17167.69",
                "17165.42",
                "17167.00"
            ]
        ]
    },
    "retExtInfo": {},
    "time": 1672026471128
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр  |Тип       |Комментарии                                                                                    |
|----------|----------|-----------------------------------------------------------------------------------------------|
|category  |string    |Тип продукта                                                                                   |
|symbol    |string    |Символ                                                                                         |
|list      |array     |Массив объекта с данными<br>Сортируется в обратном порядке по startTime             |
|list[0]   |string    |Время начала свечи (мс)                                                                        |
|list[1]   |string    |Цена открытия                                                                                  |
|list[2]   |string    |Максимальная цена                                                                              |
|list[3]   |string    |Минимальная цена                                                                               |
|list[4]   |string    |Цена закрытия. Является последней ценой сделки, если свеча не закрыта                          |
