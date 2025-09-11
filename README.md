# Содержание

- [Market](#id69)
  - [Получить серверное время Bybit](#id70)
    - [Конечная точка](#id71)
    - [Примеры запроса](#id72)
    - [Параметры запроса](#id73)
    - [Примеры ответа](#id74)
    - [Параметры ответа](#id75)
  - [Получить свечи](#id76)
    - [Конечная точка](#id77)
    - [Примеры запроса](#id78)
    - [Параметры запроса](#id79)
    - [Примеры ответа](#id80)
    - [Параметры ответа](#id81)
  - [Получить свечи Mark Price](#id82)
    - [Конечная точка](#id83)
    - [Примеры запроса](#id84)
    - [Параметры запроса](#id85)
    - [Примеры ответа](#id86)
    - [Параметры ответа](#id87)
  - [Получить индексную цену свечи](#id88)
    - [Конечная точка](#id89)
    - [Примеры запроса](#id90)
    - [Параметры запроса](#id91)
    - [Примеры ответа](#id92)
    - [Параметры ответа](#id93)
  - [Получить премиум индексную цену свечи](#id94)
    - [Конечная точка](#id95)
    - [Примеры запроса](#id96)
    - [Параметры запроса](#id97)
    - [Примеры ответа](#id98)
    - [Параметры ответа](#id99)
  - [Получить информацию об инструментах](#id)
    - [linear](#id)
      - [Конечная точка](#id)
      - [Примеры запроса](#id)
      - [Параметры запроса](#id)
      - [Примеры ответа](#id)
      - [Параметры ответа](#id)
    - [option](#id)
      - [Конечная точка](#id)
      - [Примеры запроса](#id)
      - [Параметры запроса](#id)
      - [Примеры ответа](#id)
      - [Параметры ответа](#id)
    - [spot](#id)
      - [Конечная точка](#id)
      - [Примеры запроса](#id)
      - [Параметры запроса](#id)
      - [Примеры ответа](#id)
      - [Параметры ответа](#id)

## Market<p id="id69"></p>

### Получить свечи<p id="id76"></p>

Запрос исторических свечей. Графики возвращаются группами на основе запрошенного интервала.

>Охватывает: Спот / USDT-контракты / USDC-контракты / Инверсные контракты

#### Конечная точка<p id="id77"></p>

`/v5/market/kline`

#### Примеры запроса<p id="id78"></p>

- HTTP

  ```bash
  GET /v5/market/kline?category=inverse&symbol=BTCUSD&interval=60&start=1670601600000&end=1670608800000 HTTP/1.1
  Host: api-testnet.bybit.com
  ```

- Python

  ```python
  import requests

  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/market/kline"

  complete_request = base_url + end_point
  parameters = {
      "category": "inverse",
      "symbol": "BTCUSDT",
      "interval": "60",
      "start": 1670601600000,
      "end": 1670608800000
  }
  
  response = requests.get(url=complete_request, params=parameters, timeout=10)

  print(response.json())
  ```

- pybit

  ```python
  from pybit.unified_trading import HTTP
  
  session = HTTP(testnet=True)
  print(session.get_kline(
      category="inverse",
      symbol="BTCUSD",
      interval=60,
      start=1670601600000,
      end=1670608800000,
  ))
  ```

#### Параметры запроса<p id="id79"></p>

|Параметр  	          |Обязательный	 |Тип   	  |Комментарии                                      |По умолчанию|
|---------------------|--------------|----------|-------------------------------------------------|------------|
|[category](#idi)	    |false         |string    |Тип продукта                                     |linear      |
|[symbol](#idj)	      |true       	 |string    |Имя символа                                      |-           |
|[interval](#idk)     |true       	 |string    |Интервал свечей                                  |-           |
|start	              |false      	 |integer   |Временная метка начала (мс)                      |-           |
|end                  |false      	 |integer   |Временная метка окончания (мс)                   |-           |
|limit	              |false      	 |integer   |Лимит на размер данных на страницу. [1, 1000]    |200         |

#### Пример ответа<p id="id80"></p>

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "symbol": "BTCUSD",
        "category": "inverse",
        "list": [
            [
                "1670608800000",
                "17071",
                "17073",
                "17027",
                "17055.5",
                "268611",
                "15.74462667"
            ],
            [
                "1670605200000",
                "17071.5",
                "17071.5",
                "17061",
                "17071",
                "4177",
                "0.24469757"
            ],
            [
                "1670601600000",
                "17086.5",
                "17088",
                "16978",
                "17071.5",
                "6356",
                "0.37288112"
            ]
        ]
    },
    "retExtInfo": {},
    "time": 1672025956592
}
```

#### Параметры ответа<p id="id81"></p>

|Параметр  |Тип       |Комментарии                                                                                                                                              |
|----------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|category  |string    |Тип продукта                                                                                                                                             |
|symbol    |string    |Символ                                                                                                                                                   |
|list      |array     |Массив строк индивидуальных свечей.<br>Сортируется в обратном порядке по startTime                                                                       |
|list[0]   |string    |Время начала свечи (мс)                                                                                                                                  |
|list[1]   |string    |Цена открытия                                                                                                                                            |
|list[2]   |string    |Максимальная цена                                                                                                                                        |
|list[3]   |string    |Минимальная цена                                                                                                                                         |
|list[4]   |string    |Цена закрытия. Является последней ценой сделки, если свеча не закрыта                                                                                    |
|list[5]   |string    |Объём торгов.<br>USDT или USDC-контракты: единица - базовая монета (например, BTC)<br>Инверсные контракты: единица - квотируемая монета (например, USD)  |
|list[6]   |string    |Оборот.<br>USDT или USDC-контракты: единица - квотируемая монета (например, USDT)<br>Инверсные контракты: единица - базовая монета (например, BTC)       |

### Получить свечи Mark Price<p id="id82"></p>

Запрос исторических свечей по
[mark price](https://www.bybit.com/en-US/help-center/s/article/Glossary-Bybit-Trading-Terms).
Графики возвращаются группами в зависимости от запрошенного интервала.

>Охватывает: USDT-контракты / USDC-контракты / Инверсные контракты

#### Конечная точка<p id="id83"></p>

`/v5/market/mark-price-kline`

#### Примеры запроса<p id="id84"></p>

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

#### Параметры запроса<p id="id85"></p>

|Параметр  	          |Обязательный	 |Тип   	|Комментарии                                        |По умолчанию|
|---------------------|--------------|----------|-------------------------------------------------|------------|
|[category](#idi)	    |false      	 |string    |Тип продукта                                     |linear      |
|[symbol](#idj)	      |true       	 |string    |Имя символа                                      |-           |
|[interval](#idk)     |true       	 |string    |Интервал свечей                                  |-           |
|start	              |false      	 |integer   |Временная метка начала (мс)                      |-           |
|end                  |false      	 |integer   |Временная метка окончания (мс)                   |-           |
|limit	              |false      	 |integer   |Лимит на размер данных на страницу. [1, 1000]    |200         |

#### Пример ответа<p id="id86"></p>

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

#### Параметры ответа<p id="id87"></p>

|Параметр  |Тип       |Комментарии                                                                                                                                              |
|----------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|category  |string    |Тип продукта                                                                                                                                             |
|symbol    |string    |Символ                                                                                                                                                   |
|list      |array     |Массив строк индивидуальных свечей.<br>Сортируется в обратном порядке по startTime                                                                       |
|list[0]   |string    |Время начала свечи (мс)                                                                                                                                  |
|list[1]   |string    |Цена открытия                                                                                                                                            |
|list[2]   |string    |Максимальная цена                                                                                                                                        |
|list[3]   |string    |Минимальная цена                                                                                                                                         |
|list[4]   |string    |Цена закрытия. Является последней ценой сделки, если свеча не закрыта                                                                                    |

### Получить индексную цену свечи<p id="id88"></p>

Запрашивает исторические свечи индексных цен. Графики возвращаются группами на основе заданного интервала.

>Охватывает: USDT-контракты / USDC-контракты / Инверсные контракты

#### Конечная точка<p id="id89"></p>

`/v5/market/index-price-kline`

#### Примеры запроса<p id="id90"></p>

- HTTP

  ```bash
  GET /v5/market/index-price-kline?category=inverse&symbol=BTCUSDZ22&interval=1&start=1670601600000&end=1670608800000&limit=2 HTTP/1.1
  Host: api-testnet.bybit.com
  ```

- Python

  ```python
  import requests

  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/market/index-price-kline"

  complete_request = base_url + end_point
  parameters = {
      "category": "inverse",
      "symbol": "BTCUSDZ22",
      "interval": "1",
      "start": 1670601600000,
      "end": 1670608800000,
      "limit": 2
  }
  
  response = requests.get(url=complete_request, params=parameters, timeout=10)

  print(response.json())
  ```

- pybit

  ```python
  from pybit.unified_trading import HTTP

  session = HTTP(testnet=True)
  print(session.get_index_price_kline(
      category="inverse",
      symbol="BTCUSDZ22",
      interval=1,
      start=1670601600000,
      end=1670608800000,
      limit=2,
  ))
  ```

#### Параметры запроса<p id="id91"></p>

|Параметр  	          |Обязательный	 |Тип   	|Комментарии                                        |По умолчанию|
|---------------------|--------------|----------|-------------------------------------------------|------------|
|[category](#idi)	    |false      	 |string    |Тип продукта                                     |linear      |
|[symbol](#idj)	      |true       	 |string    |Имя символа                                      |-           |
|[interval](#idk)     |true      	   |string    |Интервал свечей                                  |-           |
|start	              |false      	 |integer   |Временная метка начала (мс)                      |-           |
|end                  |false      	 |integer   |Временная метка окончания (мс)                   |-           |
|limit	              |false      	 |integer   |Лимит на размер данных на страницу. [1, 1000]    |200         |

#### Пример ответа<p id="id92"></p>

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

#### Параметры ответа<p id="id93"></p>

|Параметр  |Тип       |Комментарии                                                                                                                                              |
|----------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|category  |string    |Тип продукта                                                                                                                                             |
|symbol    |string    |Символ                                                                                                                                                   |
|list      |array     |Массив строк индивидуальных свечей.<br>Сортируется в обратном порядке по startTime                                                                       |
|list[0]   |string    |Время начала свечи (мс)                                                                                                                                  |
|list[1]   |string    |Цена открытия                                                                                                                                            |
|list[2]   |string    |Максимальная цена                                                                                                                                        |
|list[3]   |string    |Минимальная цена                                                                                                                                         |
|list[4]   |string    |Цена закрытия. Является последней ценой сделки, если свеча не закрыта                                                                                    |

### Получить премиум индексную цену свечи<p id="id94"></p>

Запрашивает исторические свечи премиум индексных цен. Графики возвращаются группами на основе заданного интервала.

>Охватывает:  Бессрочные контракты USDT и USDC.

#### Конечная точка<p id="id95"></p>

`/v5/market/premium-index-price-kline`

#### Примеры запроса<p id="id96"></p>

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

#### Параметры запроса<p id="id97"></p>

|Параметр  	          |Обязательный	 |Тип   	|Комментарии                                        |По умолчанию|
|---------------------|--------------|----------|-------------------------------------------------|------------|
|[category](#idi)	    |false      	 |string    |Тип продукта                                     |linear      |
|[symbol](#idj)	      |true       	 |string    |Имя символа                                      |-           |
|[interval](#idk)     |true      	   |string    |Интервал свечей                                  |-           |
|start	              |false      	 |integer   |Временная метка начала (мс)                      |-           |
|end                  |false      	 |integer   |Временная метка окончания (мс)                   |-           |
|limit	              |false      	 |integer   |Лимит на размер данных на страницу. [1, 1000]    |200         |

#### Пример ответа<p id="id98"></p>

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

#### Параметры ответа<p id="id99"></p>

|Параметр  |Тип       |Комментарии                                                                                                                                              |
|----------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|category  |string    |Тип продукта                                                                                                                                             |
|symbol    |string    |Символ                                                                                                                                                   |
|list      |array     |Массив строк индивидуальных свечей.<br>Сортируется в обратном порядке по startTime                                                                       |
|list[0]   |string    |Время начала свечи (мс)                                                                                                                                  |
|list[1]   |string    |Цена открытия                                                                                                                                            |
|list[2]   |string    |Максимальная цена                                                                                                                                        |
|list[3]   |string    |Минимальная цена                                                                                                                                         |
|list[4]   |string    |Цена закрытия. Является последней ценой сделки, если свеча не закрыта                                                                                    |

### Получить премиум индексную цену свечи<p id="id"></p>

Запрашивает исторические свечи премиум индексных цен. Графики возвращаются группами на основе заданного интервала.

>Охватывает:  Бессрочные контракты USDT и USDC.

#### linear<p id="id"></p>

##### Конечная точка<p id="id"></p>

`/v5/market/premium-index-price-kline`

##### Примеры запроса<p id="id"></p>

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

##### Параметры запроса<p id="id"></p>

|Параметр  	          |Обязательный	 |Тип   	|Комментарии                                        |По умолчанию|
|---------------------|--------------|----------|-------------------------------------------------|------------|
|[category](#idi)	    |false      	 |string    |Тип продукта                                     |linear      |
|[symbol](#idj)	      |true       	 |string    |Имя символа                                      |-           |
|[interval](#idk)     |true      	   |string    |Интервал свечей                                  |-           |
|start	              |false      	 |integer   |Временная метка начала (мс)                      |-           |
|end                  |false      	 |integer   |Временная метка окончания (мс)                   |-           |
|limit	              |false      	 |integer   |Лимит на размер данных на страницу. [1, 1000]    |200         |

##### Пример ответа<p id="id"></p>

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

##### Параметры ответа<p id="id"></p>

|Параметр  |Тип       |Комментарии                                                                                                                                              |
|----------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|category  |string    |Тип продукта                                                                                                                                             |
|symbol    |string    |Символ                                                                                                                                                   |
|list      |array     |Массив строк индивидуальных свечей.<br>Сортируется в обратном порядке по startTime                                                                       |
|list[0]   |string    |Время начала свечи (мс)                                                                                                                                  |
|list[1]   |string    |Цена открытия                                                                                                                                            |
|list[2]   |string    |Максимальная цена                                                                                                                                        |
|list[3]   |string    |Минимальная цена                                                                                                                                         |
|list[4]   |string    |Цена закрытия. Является последней ценой сделки, если свеча не закрыта                                                                                    |

#### option<p id="id"></p>

##### Конечная точка<p id="id"></p>

`/v5/market/premium-index-price-kline`

##### Примеры запроса<p id="id"></p>

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

##### Параметры запроса<p id="id"></p>

|Параметр  	          |Обязательный	 |Тип   	|Комментарии                                        |По умолчанию|
|---------------------|--------------|----------|-------------------------------------------------|------------|
|[category](#idi)	    |false      	 |string    |Тип продукта                                     |linear      |
|[symbol](#idj)	      |true       	 |string    |Имя символа                                      |-           |
|[interval](#idk)     |true      	   |string    |Интервал свечей                                  |-           |
|start	              |false      	 |integer   |Временная метка начала (мс)                      |-           |
|end                  |false      	 |integer   |Временная метка окончания (мс)                   |-           |
|limit	              |false      	 |integer   |Лимит на размер данных на страницу. [1, 1000]    |200         |

##### Пример ответа<p id="id"></p>

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

##### Параметры ответа<p id="id"></p>

|Параметр  |Тип       |Комментарии                                                                                                                                              |
|----------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|category  |string    |Тип продукта                                                                                                                                             |
|symbol    |string    |Символ                                                                                                                                                   |
|list      |array     |Массив строк индивидуальных свечей.<br>Сортируется в обратном порядке по startTime                                                                       |
|list[0]   |string    |Время начала свечи (мс)                                                                                                                                  |
|list[1]   |string    |Цена открытия                                                                                                                                            |
|list[2]   |string    |Максимальная цена                                                                                                                                        |
|list[3]   |string    |Минимальная цена                                                                                                                                         |
|list[4]   |string    |Цена закрытия. Является последней ценой сделки, если свеча не закрыта                                                                                    |

#### spot<p id="id"></p>

##### Конечная точка<p id="id"></p>

`/v5/market/premium-index-price-kline`

##### Примеры запроса<p id="id"></p>

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

##### Параметры запроса<p id="id"></p>

|Параметр  	          |Обязательный	 |Тип   	|Комментарии                                        |По умолчанию|
|---------------------|--------------|----------|-------------------------------------------------|------------|
|[category](#idi)	    |false      	 |string    |Тип продукта                                     |linear      |
|[symbol](#idj)	      |true       	 |string    |Имя символа                                      |-           |
|[interval](#idk)     |true      	   |string    |Интервал свечей                                  |-           |
|start	              |false      	 |integer   |Временная метка начала (мс)                      |-           |
|end                  |false      	 |integer   |Временная метка окончания (мс)                   |-           |
|limit	              |false      	 |integer   |Лимит на размер данных на страницу. [1, 1000]    |200         |

##### Пример ответа<p id="id"></p>

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

##### Параметры ответа<p id="id"></p>

|Параметр  |Тип       |Комментарии                                                                                                                                              |
|----------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
|category  |string    |Тип продукта                                                                                                                                             |
|symbol    |string    |Символ                                                                                                                                                   |
|list      |array     |Массив строк индивидуальных свечей.<br>Сортируется в обратном порядке по startTime                                                                       |
|list[0]   |string    |Время начала свечи (мс)                                                                                                                                  |
|list[1]   |string    |Цена открытия                                                                                                                                            |
|list[2]   |string    |Максимальная цена                                                                                                                                        |
|list[3]   |string    |Минимальная цена                                                                                                                                         |
|list[4]   |string    |Цена закрытия. Является последней ценой сделки, если свеча не закрыта                                                                                    |

## Определения перечислений

### locale<p id="ida"></p>

- de-DE
- en-US
- es-AR
- es-ES
- es-MX
- fr-FR
- kk-KZ
- id-ID
- uk-UA
- ja-JP
- ru-RU
- th-TH
- pt-BR
- tr-TR
- vi-VN
- zh-TW
- ar-SA
- hi-IN
- fil-PH

### announcementType<p id="idb"></p>

- new_crypto
- latest_bybit_news
- delistings
- latest_activities
- product_updates
- maintenance_updates
- new_fiat_listings
- other

### announcementTag<p id="idc"></p>

- Spot
- Derivatives
- Spot Listings
- BTC
- ETH
- Trading Bots
- USDC
- Leveraged Tokens
- USDT
- Margin Trading
- Partnerships
- Launchpad
- Upgrades
- ByVotes
- Delistings
- VIP
- Futures
- Institutions
- Options
- WEB3
- Copy Trading
- Earn
- Bybit Savings
- Dual Asset
- Liquidity Mining
- Shark Fin
- Launchpool
- NFT GrabPic
- Buy Crypto
- P2P Trading
- Fiat Deposit
- Crypto Deposit
- Спот
- Спот лістинги
- Торгові боти
- Токени з кредитним плечем
- Маржинальна торгівля
- Партнерство
- Оновлення
- Делістинги
- Ф'ючерси
- Опціони
- Копітрейдинг
- Bybit Накопичення
- Бівалютні інвестиції
- Майнінг ліквідності
- Купівля криптовалюти
- P2P торгівля
- Фіатні депозити
- Криптодепозити
- Копитрейдинг
- Торговые боты
- Деривативы
- P2P
- Спот листинги
- Деривативи
- MT4
- Lucky Draw
- Unified Trading Account
- Єдиний торговий акаунт
- Единый торговый аккаунт
- Институциональный трейдинг
- Інституціональний трейдинг
- Делистинг

### state<p id="idd"></p>

- scheduled (Запланирован)
- ongoing (Выполняется или "Активен")
- completed (Завершен)
- canceled (Отменен)

### serviceTypes<p id="ide"></p>

- 1 Trading service (Торговый сервис)
- 2 Trading service via http request (Торговый сервис через HTTP-запрос)
- 3 Trading service via websocket (Торговый сервис через WebSocket)
- 4 Private websocket stream (Приватный поток WebSocket)
- 5 Market data service (Сервис рыночных данных)

### product<p id="idf"></p>

- 1 Futures (Фьючерсы)
- 2 Spot (Спот)
- 3 Option (Опционы)
- 4 Spread (Спред)

### maintainType<p id="idg"></p>

- 1 Planned maintenance (Запланированное обслуживание)
- 2 Temporary maintenance (Временное обслуживание)
- 3 Incident (Инцидент)

### env<p id="idh"></p>

- 1 Production (Продакшн)
- 2 Production Demo service (Демо-сервис продакшн)

### category<p id="idi"></p>

Unified Account (Унифицированный аккаунт)

- spot (Спот-торговля)
- linear (USDT-вечные контракты, USDT- фьючерсы и USDC-контракты, включая USDC-вечные и USDC-фьючерсы)
- inverse (Инверсные контракты, включая инверсные вечные и инверсные фьючерсы)
- option (Опционы)

Classic Account (Классический аккаунт)

- linear (USDT-вечные контракты)
- inverse (Инверсные контракты, включая инверсные вечные и инверсные фьючерсы)
- spot (Спот-торговля)

### symbol<p id="idj"></p>

>Это примеры того как должны выглядеть символы относительно площадки

***USDT Perpetual:***

- BTCUSDT
- ETHUSDT

***USDT Futures:***

>Контракты USDT Futures, предлагаемые Bybit, включают следующие типы:
>
>- Weekly (Недельные)
>- Bi-Weekly (Двухнедельные)
>- Tri-Weekly (Трехнедельные)
>- Monthly (Месячные)
>- Bi-Monthly (Двухмесячные)
>- Quarterly (Квартальные)
>- Bi-Quarterly (Полугодовые)
>- Tri-Quarterly (Девятимесячные)

- BTCUSDT-21FEB25
- ETHUSDT-14FEB25

***USDC Perpetual:***

- BTCPERP
- ETHPERP
  
***USDC Futures:***

- BTC-24MAR23

***Inverse Perpetual:***

- BTCUSD
- ETHUSD
  
***Inverse Futures:***

- BTCUSDH23 (H23: первый квартал 2023 года)
- BTCUSDM23 (M23: второй квартал 2023 года)
- BTCUSDU23 (U23: третий квартал 2023 года)
- BTCUSDZ23 (Z23: четвертый квартал 2023 года)

***Spot:***

- BTCUSDT
- ETHUSDC

***Option:***

- BTC-13FEB25-89000-P-USDT
- ETH-28FEB25-2800-C

### interval<p id="idk"></p>

- 1, 3, 5, 15, 30, 60, 120, 240, 360, 720 (минуты)
- D (день)
- W (неделя)
- M (месяц)
