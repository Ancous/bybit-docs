# Содержание

- [Market](#id69)

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
