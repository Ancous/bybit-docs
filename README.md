# Содержание

- [Сервис Demo Trading](#id42)
  - [Введение](#id43)
  - [Создать API Ключ](#id44)
  - [Правила использования](#id45)
  - [Домен](#id46)
  - [Подсказки](#id47)
  - [Список доступных API](#id48)
  - [Запрос средств для Demo Trading](#id49)
    - [Конечная точка](#id50)
    - [Примеры запроса](#id51)
    - [Параметры запроса](#id52)
  - [Создание демо-аккаунта](#id53)
    - [Конечная точка](#id54)
    - [Примеры запроса](#id55)
    - [Параметры запроса](#id56)
    - [Примеры ответа](#id57)
    - [Параметры ответа](#id58)
  - [Создать API ключ демо-аккаунта](#id59)
  - [Обновить API ключ демо-аккаунта](#id60)
  - [Получить информацию о API ключе демо-аккаунта](#id61)
  - [Удалить API ключ демо-аккаунта](#id62)
- [Получить статус системы](#id63)
  - [Конечная точка](#id64)
  - [Примеры запроса](#id65)
  - [Параметры запроса](#id66)
  - [Примеры ответа](#id67)
  - [Параметры ответа](#id68)
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

## Сервис Demo Trading<p id="id42"></p>

### Введение<p id="id43"></p>

Bybit v5 Open API поддерживает аккаунт для демо-торговли, но обратите внимание, что не все API доступны для аккаунта
демо-торговли, поскольку демо-сервис предназначен главным образом для опыта торговли, поэтому у него не полный
функционал по сравнению с реальной торговлей.

### Создать API Ключ<p id="id44"></p>

Вам нужно войти в свой [mainnet](https://www.bybit.com/) аккаунт.
Переключитесь на Demo Trading. Обратите внимание, что это независимый аккаунт только для демо-торговли, и у него свой
собственный пользовательский ID.  
Наведите мышку на аватар пользователя, затем нажмите "API", чтобы сгенерировать api ключ и секрет.

### Правила использования<p id="id45"></p>

Основные правила торговли такие же, как и в реальной торговле.
Ордера, сгенерированные в демо-торговле, хранятся 7 дней.
Лимиты по умолчанию, не поддаются повышению.

### Домен<p id="id46"></p>

Rest API: `https://api-demo.bybit.com`  
Websocket: `wss://stream-demo.bybit.com` (обратите внимание, что поддерживаются только приватные стримы; для публичных
стримов `wss://stream.bybit.com`; WS Trade не поддерживается).

### Подсказки<p id="id47"></p>

Обратите внимание, что демо-торговля — это изолированный модуль. Когда вы создаёте ключ из демо-торговли, пожалуйста,
используйте вышеуказанный домен для подключения.  
Кстати, бессмысленно использовать демо-сервис торгов на [testnet](https://testnet.bybit.com/) сайте, поэтому не
создавайте ключ из Testnet demo trading.

### Список доступных API<p id="id48"></p>

<table class="iksweb">
		<tr>
			<td>Категория</td>
			<td>Название</td>
			<td>Эндпоинт</td>
		</tr>
		<tr>
			<td>Market</td>
			<td>Все</td>
			<td>Все эндпоинты</td>
		</tr>
		<tr>
			<td rowspan="10">Position</td>
			<td><a href="#id1">Place Order</a></td>
			<td>/v5/order/create</td>
		</tr>
		<tr>
			<td><a href="#id1">Amend Order</a></td>
			<td>/v5/order/amend</td>
		</tr>
		<tr>
			<td><a href="#id1">Cancel order</a></td>
			<td>/v5/order/cancel</td>
		</tr>
		<tr>
			<td><a href="#id1">Get Open Orders</a></td>
			<td>/v5/order/realtime</td>
		</tr>
		<tr>
			<td><a href="#id1">Cancel All Orders</a></td>
			<td>/v5/order/cancel-all</td>
		</tr>
		<tr>
			<td><a href="#id1">Get Order History</a></td>
			<td>/v5/order/history</td>
		</tr>
		<tr>
			<td><a href="#id1">Get Trade History</a></td>
			<td>/v5/execution/list</td>
		</tr>
		<tr>
			<td><a href="#id1">Batch Place Order</a></td>
			<td>/v5/order/create-batch</td>
		</tr>
		<tr>
			<td><a href="#id1">Batch Amend Order</a></td>
			<td>/v5/order/amend-batch</td>
		</tr>
		<tr>
			<td><a href="#id1">Batch Cancel Order</a></td>
			<td>/v5/order/cancel-batch</td>
		</tr>
		<tr>
			<td rowspan="7">Position</td>
			<td><a href="#id1">Get Position Info</a></td>
			<td>/v5/position/list</td>
		</tr>
		<tr>
			<td><a href="#id1">Set Leverage</a></td>
			<td>/v5/position/set-leverage</td>
		</tr>
		<tr>
			<td><a href="#id1">Switch Position Mode</a></td>
			<td>/v5/position/switch-mode</td>
		</tr>
		<tr>
			<td><a href="#id1">Set Trading Stop</a></td>
			<td>/v5/position/trading-stop</td>
		</tr>
		<tr>
			<td><a href="#id1">Set Auto Add Margin</a></td>
			<td>/v5/position/set-auto-add-margin</td>
		</tr>
		<tr>
			<td><a href="#id1">Add Or Reduce Margin</a></td>
			<td>/v5/position/add-margin</td>
		</tr>
		<tr>
			<td><a href="#id1">Get Closed PnL</a></td>
			<td>/v5/position/closed-pnl</td>
		</tr>
		<tr>
			<td rowspan="9">Account</td>
			<td><a href="#id1">Get Wallet Balance</a></td>
			<td>/v5/account/wallet-balance</td>
		</tr>
		<tr>
			<td><a href="#id1">Get Borrow History</a></td>
			<td>/v5/account/borrow-history</td>
		</tr>
		<tr>
			<td><a href="#id1">Set Collateral Coin</a></td>
			<td>/v5/account/set-collateral-switch</td>
		</tr>
		<tr>
			<td><a href="#id1">Get Collateral Info</a></td>
			<td>/v5/account/collateral-info</td>
		</tr>
		<tr>
			<td><a href="#id1">Get Coin Greeks</a></td>
			<td>/v5/asset/coin-greeks</td>
		</tr>
		<tr>
			<td><a href="#id1">Get Account Info</a></td>
			<td>/v5/account/info</td>
		</tr>
		<tr>
			<td><a href="#id1">Get Transaction Log</a></td>
			<td>/v5/account/transaction-log</td>
		</tr>
		<tr>
			<td><a href="#id1">Set Margin Mode</a></td>
			<td>/v5/account/set-margin-mode</td>
		</tr>
		<tr>
			<td><a href="#id1">Set Spot Hedging</a></td>
			<td>/v5/account/set-hedging-mode</td>
		</tr>
		<tr>
			<td rowspan="2">Asset</td>
			<td><a href="#id1">Get Delivery Record</a></td>
			<td>/v5/asset/delivery-record</td>
		</tr>
		<tr>
			<td><a href="#id1">Get USDC Session Settlement</a></td>
			<td>/v5/asset/settlement-record</td>
		</tr>
		<tr>
			<td rowspan="3">Spot Margin Trade</td>
			<td><a href="#id1">Toggle Margin Trade</a></td>
			<td>/v5/spot-margin-trade/switch-mode</td>
		</tr>
		<tr>
			<td><a href="#id1">Set Leverage</a></td>
			<td>/v5/spot-margin-trade/set-leverage</td>
		</tr>
		<tr>
			<td><a href="#id1">Get Status And Leverage</a></td>
			<td>/v5/spot-margin-uta/status</td>
		</tr>
		<tr>
			<td><a href="#id1">WS Private</a></td>
			<td>order,execution,position,wallet,greeks</td>
			<td>/v5/private</td>
		</tr>
</table>

### Запрос средств для Demo Trading<p id="id49"></p>

>Ограничение скорости API: 1 запрос в минуту

#### Конечная точка<p id="id50"></p>

`/v5/account/demo-apply-money`

#### Примеры запроса<p id="id51"></p>

- HTTP

  ```bash
  POST /v5/account/demo-apply-money HTTP/1.1
  Host: api-demo.bybit.com
  X-BAPI-SIGN: XXXXXXX
  X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx
  X-BAPI-TIMESTAMP: 1711420489915
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  
  {
      "adjustType": 0,
      "utaDemoApplyMoney": [
          {
              "coin": "USDT",
              "amountStr": "109"
          },
          {
              "coin": "ETH",
              "amountStr": "1"
          }
      ]
  }
  ```

#### Параметры запроса<p id="id52"></p>

|Параметр       	  |Обязательный	  |Тип   	  |Комментарии                                                 |По умолчанию|
|-------------------|---------------|---------|------------------------------------------------------------|------------|
|adjustType	        |false      	  |integer  |0: добавить демо-средства; 1: уменьшить демо-средства       |0           |
|utaDemoApplyMoney	|false      	  |array    |-                                                           |-           |
|coin	              |false      	  |string	  |Запрашиваемая монета, поддерживаются BTC, ETH, USDT, USDC   |-           |
|amountStr	        |false      	  |string   |Запрашиваемая сумма                                         |-           |

>Максимальная запрашиваемая сумма в каждом запросе
>
>- BTC: "15"
>- ETH: "200"
>- USDT: "100000"
>- USDC: "100000"

### Создание демо-аккаунта<p id="id53"></p>

#### Конечная точка<p id="id54"></p>

`/v5/user/create-demo-member`

#### Примеры запроса<p id="id55"></p>

- HTTP

  ```bash
  POST /v5/user/create-demo-member HTTP/1.1
  Host: api.bybit.com
  X-BAPI-SIGN: XXXXXXX
  X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx
  X-BAPI-TIMESTAMP: 1728460942776
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  Content-Length: 2
  
  {}
  ```

#### Параметры запроса<p id="id56"></p>

none

#### Пример ответа<p id="id57"></p>

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "subMemberId": "1565431531513541"
    },
    "retExtInfo": {},
    "time": 1679415136117
}
```

#### Параметры ответа<p id="id58"></p>

|Параметр	          |Тип            |Комментарии        |
|-------------------|---------------|-------------------|
|subMemberId        |string    	    |ID демо-аккаунта   |

### [Создать API ключ демо-аккаунта](#id1)<p id="id59"></p>

>Информация:  
>Введите сгенерированный UID демо-аккаунта.
>Используйте ключ основного аккаунта для вызова интерфейса, домен должен быть "api.bybit.com".

### [Обновить API ключ демо-аккаунта](#id1)<p id="id60"></p>

>Информация:  
>Используйте ключ основного аккаунта для вызова интерфейса, домен должен быть "api.bybit.com".

### [Получить информацию о API ключе демо-аккаунта](#id1)<p id="id61"></p>

>Информация:  
>Используйте соответствующий ключ демо-аккаунта для вызова интерфейса, домен должен быть "api-demo.bybit.com".

### [Удалить API ключ демо-аккаунта](#id1)<p id="id62"></p>

>Информация:  
>Используйте ключ основного аккаунта для вызова интерфейса, домен должен быть "api.bybit.com".

## Получить статус системы<p id="id63"></p>

### Конечная точка<p id="id64"></p>

`/v5/system/status`

### Примеры запроса<p id="id65"></p>

- HTTP

  ```bash
  GET /v5/system/status HTTP/1.1
  Host: api.bybit.com
  ```

### Параметры запроса<p id="id66"></p>

|Параметр     	|Обязательный	  |Тип   	  |Комментарии                        |По умолчанию|
|---------------|---------------|---------|-----------------------------------|------------|
|id	            |false        	|string   |ID. Уникальный идентификатор       |-           |
|[state](#idd)	|false        	|string   |Состояние системы                  |-           |

### Пример ответа<p id="id67"></p>

```json
{
    "retCode": 0,
    "retMsg": "",
    "result": {
        "list": [
            {
                "id": "4d95b2a0-587f-11f0-bcc9-56f28c94d6ea",
                "title": "t06",
                "state": "completed",
                "begin": "1751596902000",
                "end": "1751597011000",
                "href": "",
                "serviceTypes": [
                    2,
                    3,
                    4,
                    5
                ],
                "product": [
                    1,
                    2
                ],
                "uidSuffix": [],
                "maintainType": 1,
                "env": 1
            },
            {
                "id": "19bb6f82-587f-11f0-bcc9-56f28c94d6ea",
                "title": "t05",
                "state": "completed",
                "begin": "1751254200000",
                "end": "1751254500000",
                "href": "",
                "serviceTypes": [
                    1,
                    4
                ],
                "product": [
                    1
                ],
                "uidSuffix": [],
                "maintainType": 3,
                "env": 1
            },
            {
                "id": "25f4bc8c-533c-11f0-bcc9-56f28c94d6ea",
                "title": "t04",
                "state": "completed",
                "begin": "1751017967000",
                "end": "1751018096000",
                "href": "",
                "serviceTypes": [
                    2
                ],
                "product": [
                    2
                ],
                "uidSuffix": [],
                "maintainType": 1,
                "env": 1
            },
            {
                "id": "679a9c5f-533b-11f0-bcc9-56f28c94d6ea",
                "title": "t03",
                "state": "completed",
                "begin": "1751017532000",
                "end": "1751017658000",
                "href": "",
                "serviceTypes": [
                    5,
                    4
                ],
                "product": [
                    1,
                    2
                ],
                "uidSuffix": [],
                "maintainType": 2,
                "env": 1
            },
            {
                "id": "c8990f96-5332-11f0-8fd3-c241b123dd9e",
                "title": "t02",
                "state": "completed",
                "begin": "1751013817000",
                "end": "1751013890000",
                "href": "",
                "serviceTypes": [
                    5,
                    4,
                    3,
                    2,
                    1
                ],
                "product": [
                    4,
                    3,
                    2,
                    1
                ],
                "uidSuffix": [],
                "maintainType": 2,
                "env": 1
            },
            {
                "id": "f9d6842d-5331-11f0-8fd3-c241b123dd9e",
                "title": "t01",
                "state": "completed",
                "begin": "1751012688000",
                "end": "1751012760000",
                "href": "",
                "serviceTypes": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "product": [
                    1,
                    2,
                    3,
                    4
                ],
                "uidSuffix": [],
                "maintainType": 3,
                "env": 2
            }
        ]
    },
    "retExtInfo": {},
    "time": 1751858399649
}
```

### Параметры ответа<p id="id68"></p>

|Параметр	             |Тип             |Комментарии                                                                                                           |
|----------------------|----------------|----------------------------------------------------------------------------------------------------------------------|
|id                    |string    	    |Уникальный идентификатор записи                                                                                       |
|title                 |string    	    |Название обслуживания                                                                                                 |
|[state](#idd)     	   |string    	    |Состояние системы                                                                                                     |
|begin                 |string    	    |Время начала обслуживания в формате timestamp (миллисекунды)                                                          |
|end                   |string    	    |Время окончания обслуживания в формате timestamp (миллисекунды). До окончания — прогнозируемое, после — фактическое   |
|href                  |string    	    |Ссылка на подробности обслуживания. По умолчанию пустая строка                                                        |
|[serviceTypes](#ide)  |array<int>      |Типы сервисов (Service Type), которые затрагивает обслуживание                                                        |
|[product](#idf)       |array<int>      |Затронутые продукты                                                                                                   |
|uidSuffix             |array<int>      |Затронутые конечные номера UID пользователей                                                                          |
|[maintainType](#idg)  |string          |Тип технического обслуживания                                                                                         |
|[env](#idh)           |string    	    |Окружение (Environment), в котором проводится обслуживание                                                            |

## Market<p id="id69"></p>

### Получить серверное время Bybit<p id="id70"></p>

#### Конечная точка<p id="id71"></p>

`/v5/market/time`

#### Примеры запроса<p id="id72"></p>

- HTTP

  ```bash
  GET /v5/market/time HTTP/1.1
  Host: api.bybit.com
  ```

- Python

  ```python
  import requests

  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/market/time"

  complete_request = base_url + end_point

  response = requests.get(url=complete_request, timeout=10)

  print(response.json())
  ```

- pybit

  ```python
  from pybit.unified_trading import HTTP
  
  session = HTTP(testnet=True)
  print(session.get_server_time())
  ```

#### Параметры запроса<p id="id73"></p>

none

#### Пример ответа<p id="id74"></p>

```json
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "timeSecond": "1757404648",
        "timeNano": "1757404648942446966"
    },
    "retExtInfo": {},
    "time": 1757404648942
}
```

#### Параметры ответа<p id="id75"></p>

|Параметр	     |Тип       |Комментарии                        |
|--------------|----------|-----------------------------------|
|timeSecond    |string    |Время сервера Bybit (секунды)      |
|timeNano      |string    |Время сервера Bybit (наносекунды)  |

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
