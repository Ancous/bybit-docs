# Содержание

- [Введение](#id1)
  - [Обзор](#id2)
  - [Текущий охват API](#id3)
  - [Ключевые улучшения](#id4)
    - [Выравнивание продуктовых линеек](#id5)
    - [Повышение эффективности капитала](#id6)
    - [Кредитование унифицированного аккаунта](#id7)
    - [Режим портфельной маржи](#id8)
    - [Стандарт именования интерфейсов API](#id9)
    - [Отмена ордеров по валюте расчетов](#id10)
    - [Добавление интерфейса страхового фонда](#id11)
    - [Улучшения читаемости документации API](#id12)
- [Руководство по интеграции](#id13)
  - [Ресурсы API и каналы поддержки](#id14)
  - [Аутентификация](#id15)
    - [Выбор типа API-ключа](#id16)
    - [HTTP-заголовки для аутентифицированных конечных точек](#id17)
    - [Создание запроса](#id18)
  - [Общие параметры ответа](#id19)
- [Различные режимы аккаунтов](#id20)
  - [Унифицированный аккаунт 2.0 (UTA 2.0)](#id21)
  - [Унифицированный аккаунт 1.0 (UTA 1.0)](#id22)
  - [Классический аккаунт](#id23)
  - [Определение режима аккаунта через API](#id24)
  - [Изменения в использовании API для UTA 2.0](#id25)
- [Получить объявление](#id26)
  - [Конечная точка](#id27)
  - [Пример запроса](#id28)
  - [Параметры запроса](#id29)
  - [Пример ответа](#id30)
  - [Параметры ответа](#id31)
- [SMP](#id32)
  - [Что такое SMP?](#id33)
  - [Как настроить SMP?](#id34)
  - [Что такое SMP Trade Group?](#id35)
  - [Как управлять моими UID и SMP Trade Group?](#id36)
- [Как начать Copy Trading](#id37)
  - [Стать Master Trader](#id38)
  - [Создать API KEY](#id39)
  - [Область применения](#id40)
  - [Разместить ордер Copy Trading](#id41)
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

## Введение<p id="id1"></p>

### Обзор<p id="id2"></p>

API V5 приносит единообразие и эффективность в продуктовые линейки Bybit, объединяя Спот, Деривативы и Опционы в одном наборе спецификаций.

### Текущий охват API<p id="id3"></p>

<table class="iksweb">
		<tr>
			<td rowspan="2">OpenAPI Version</td>
			<td rowspan="2">Account Type</td>
			<td colspan="3">Linear</td>
			<td colspan="2">Inverse</td>
			<td rowspan="2">Spot</td>
			<td rowspan="2">Options</td>
		</tr>
		<tr>
			<td>USDT Perpetual</td>
			<td>USDC Perpetual</td>
			<td>USDC Futures</td>
			<td>Perpetual</td>
			<td>Futures</td>
		</tr>
		<tr>
			<td rowspan="2">V5</td>
			<td>Unified trading account</td>
			<td>✓</td>
			<td>✓</td>
			<td>✓</td>
			<td>✓</td>
			<td>✓</td>
			<td>✓</td>
			<td>✓</td>
		</tr>
		<tr>
			<td>Classic account</td>
			<td>✓</td>
			<td></td>
			<td></td>
			<td>✓</td>
			<td>✓</td>
			<td>✓</td>
			<td></td>
		</tr>
</table>

### Ключевые улучшения<p id="id4"></p>

#### Выравнивание продуктовых линеек<p id="id5"></p>

V5 унифицирует API различных торговых продуктов в один, предоставляя пользователям возможность торговать Спот, Деривативами и контрактами Опционов с помощью единого API, отличая транзакции через различные параметры ордеров. Следовательно, нет необходимости переключаться между множественными интерфейсами при построении различных продуктов – независимо от задач, таких как управление ордерами или запрос данных кошелька – поскольку один и тот же API может использоваться для запросов и возврата результатов.
Глобальный словарь в V5 уникально определен, чтобы избежать сценариев, где разные термины используются для одних и тех же целей или где один термин имеет множественные ссылки. Это упрощает процесс устранения неисправностей для пользователей.

Например, при создании ордера с `POST V5/order/create` пользователи могут указать `category=spot/linear/inverse/option` для создания множественных ордеров по различным продуктам.

#### Повышение эффективности капитала<p id="id6"></p>

V5 предоставляет пользователям возможность обновить аккаунты до единого аккаунта, что позволяет совместно использовать и кросс-использовать средства между спотовой торговлей, бессрочными контрактами USDT, бессрочными контрактами USDC и опционами. Пользователи также могут компенсировать прибыль и убытки по разным позициям, что дополнительно повышает эффективность использования капитала.

#### Кредитование унифицированного аккаунта<p id="id7"></p>

API V5 поддерживает кредитование в режиме унифицированного аккаунта. Пользователи могут заложить множественные активы в качестве залога, чтобы получить маржу для торговли по различным продуктам.
Например: Трейдер Alice открывает позицию по контракту BTCUSDT, рассчитанному в USDT, имея только активы BTC. Если возникает плавающий убыток, будет записан долг, и будет взиматься процент почасово.

#### Режим портфельной маржи<p id="id8"></p>

Унифицированные аккаунты теперь поддерживают комбинированную маржу между Обратными пожизненными, Обратными фьючерсами, USDT пожизненными, USDC пожизненными, USDC фьючерсами и Опционами.

#### Стандарт именования интерфейсов API<p id="id9"></p>

API V5 предлагает более ясные определения путей для улучшения ясности и снижения неоднозначности. Новая версия делит путь API на модули: рыночные данные, управление ордерами, управление позициями, управление аккаунтами, управление активами и другие.

`<host>/<version>/<product>/<module>`

`Пример: api.bybit.com/v5/market/recent-trade`

|Сегмент адреса	        |Описание                                                                                                             |
|-----------------------|---------------------------------------------------------------------------------------------------------------------|
|v5/market/           	|Свечи, стакан, тикер, платформенные транзакционные данные, базовые финансовые правила, правила контроля рисков       |
|v5/order/        	    |Управление ордерами                                                                                                  |
|v5/position/	        |Управление позициями                                                                                                 |
|v5/account/	        |Операции только для одного аккаунта – унифицированный фондовый аккаунт, ставки и т.д.                                |
|v5/asset/	            |Операции с несколькими аккаунтами — управление активами, управление фондами и т.д.                                   |
|v5/spot-lever-token/  	|Получить котировки по Leveraged Tokens на спотовом рынке, а также выполнения функции покупки и погашения (выкупа)    |
|v5/spot-margin-trade/  |Управление Маржинальной торговлей на Споте                                                                           |

#### Отмена ордеров по валюте расчетов<p id="id10"></p>

Пользователи могут отменить все ордера Деривативов, рассчитанные одной и той же валютой, с помощью `settleCoin`.

#### Добавление интерфейса страхового фонда<p id="id11"></p>

Это добавление интерфейса позволяет запрашивать страховой пул, который пользователи могут использовать для проверки обновлений страхового фонда на платформе Bybit.

#### Улучшения читаемости документации API<p id="id12"></p>

Документация API была пересмотрена и отредактирована для улучшения ясности и снижения путаницы. Любые части предыдущей документации, которые были неясны, были пересмотрены для предоставления лучших объяснений.

## Руководство по интеграции<p id="id13"></p>

> Совет:  
>Чтобы узнать больше о V5 API, пожалуйста, прочитайте [введение](#id1).

### Ресурсы API и каналы поддержки<p id="id14"></p>
- [Центр помощи](https://www.bybit.com/en/help-center/topic-list?language=en_US)
- [Официальный Python SDK](https://github.com/bybit-exchange/pybit)
- [Официальный Go SDK](https://github.com/bybit-exchange/bybit.go.api)
- [Официальный Java SDK](https://github.com/bybit-exchange/bybit-java-api)
- [Официальный .Net SDK](https://github.com/bybit-exchange/bybit.net.api)
- [Сообщественный Node.js SDK](https://www.npmjs.com/package/bybit-api)
- [Telegram - Группа обсуждения API](https://t.me/BybitAPI)
- [Discord](https://discord.gg/3ZDjGBNvKR)
- [Коллекция Postman](https://github.com/bybit-exchange/QuickStartWithPostman)
- [Примеры использования API](https://github.com/bybit-exchange/api-usage-examples)

### Аутентификация<p id="id15"></p>

>Информация:  
>Пожалуйста, посетите [тестовую сеть](https://testnet.bybit.com/app/user/api-management) или [основную сеть](https://www.bybit.com/app/user/api-management) Bybit для генерации API-ключа.

Базовый эндпоинт REST API:
  - Тестовая сеть:
  `https://api-testnet.bybit.com`

  - Основная сеть (доступны оба эндпоинта):
  `https://api.bybit.com`
  `https://api.bytick.com`

>Важно:
>- Пользователи из Нидерландов: используйте https://api.bybit.nl для основной сети
>- Пользователи из Турции: используйте https://api.bybit-tr.com для основной сети
>- Пользователи из Казахстана: используйте https://api.bybit.kz для основной сети
>- Пользователи из Грузии: используйте https://api.bybitgeorgia.ge для основной сети
>- Пользователи из ОАЭ: используйте https://api.bybit.ae для основной сети

#### Выбор типа API-ключа<p id="id16"></p>

API-ключи, сгенерированные системой:
API-ключ, созданный системой Bybit, работает с шифрованием HMAC. Вам будет предоставлена пара публичного и приватного ключей. Пожалуйста, относитесь к этой паре ключей как к паролям и храните их в безопасности.

  - Следуйте примерам [скриптов HMAC](https://github.com/bybit-exchange/api-usage-examples) для завершения процедуры шифрования.

Автоматически сгенерированные API-ключи:
API-ключи, созданные самостоятельно, работают с шифрованием RSA. Вы должны создать свои публичный и приватный ключи с помощью программного обеспечения, а затем предоставить только публичный ключ Bybit — приватный ключ мы никогда не храним.

  - Используйте [api-rsa-generator](https://github.com/bybit-exchange/api-rsa-generator) для создания RSA приватного и публичного ключей.
  - Следуйте примерам [скриптов RSA](https://github.com/bybit-exchange/api-usage-examples) для завершения процедуры шифрования.

#### HTTP-заголовки для аутентифицированных конечных точек<p id="id17"></p>

Следующие ключи HTTP-заголовков должны использоваться для аутентификации:

  - `X-BAPI-API-KEY` - API-ключ
  - `X-BAPI-TIMESTAMP` - временная метка UTC в миллисекундах
  - `X-BAPI-SIGN` - подпись, полученная из параметров запроса
  - `X-Referer` или `Referer` - заголовок только для пользователей брокера

Мы также предоставляем X-BAPI-RECV-WINDOW (единица измерения в миллисекундах, значение по умолчанию 5000) для указания срока действия HTTP-запроса. Он также используется для предотвращения повторных атак.

Меньшее значение `X-BAPI-RECV-WINDOW` более безопасно, но ваш запрос может завершиться неудачей, если время передачи превышает ваше `X-BAPI-RECV-WINDOW`.

>Внимание:  
>Пожалуйста, убедитесь, что параметр timestamp соответствует следующему правилу:  
>`server_time - recv_window <= timestamp < server_time + 1000`  
>это означает, что ваш timestamp должен находиться в диапазоне: [server_time - recv_window; server_time + 1000)  
>server_time обозначает время сервера Bybit, которое можно запросить через эндпоинт [/v5/market/time](#).. Помните, что настоятельно рекомендуется использовать время локального устройства для timestamp и всегда держать его синхронизированным с NTP.

#### Создание запроса<p id="id18"></p>

>Совет:  
>Для помощи в диагностике сложных проблем сети вы можете рассмотреть добавление `cdn-request-id` в заголовки вашего запроса. Его значение должно быть уникальным для каждого запроса.

Основные шаги:

  1. Вычислите строку, которую хотите подписать, следующим образом:
     - Для GET-запросов:
       `timestamp + API key + recv_window + queryString`.
     - Для POST-запросов:
       `timestamp + API key + recv_window + jsonBodyString`.
  2. Используйте алгоритм **HMAC_SHA256** или **RSA_SHA256** для подписания строки из шага 1 и преобразуйте её в строку в нижнем регистре HEX для HMAC_SHA256 или base64 для RSA_SHA256, чтобы получить строковое значение  вашей подписи.
  3. Добавьте вашу подпись в заголовок `X-BAPI-API-KEY` и отправьте HTTP-запрос.

>Информация:  
>Примеры алгоритмов подписи можно найти [здесь](https://github.com/bybit-exchange/api-usage-examples).

Пример того, как создать простой текст для шифрования:
  - GET
    ```
    # правило:
    timestamp+api_key+recv_window+queryString
    
    # Примерные значения:
    timestamp = "1658384314791"
    api_key = "XXXXXXXXXX"
    recv_window = "5000"
    queryString = "category=option&symbol=BTC-29JUL22-25000-C"
    
    # Результирующая строка, которая должна быть подписана:
    "1658384314791XXXXXXXXXX5000category=option&symbol=BTC-29JUL22-25000-C"
    
    # Пример результирующей подписи для HMAC:
    "410e0f387bafb7afd0f1722c068515e09945610124fa11774da1da857b72f30b"
    ```
  - POST
    ```
    # правило:
    timestamp+api_key+recv_window+jsonBodyString
    
    # Примерные значения:
    timestamp = 1658385579423
    api_key = XXXXXXXXXX
    recv_window = 5000
    jsonBodyString = {"category": "option"}
    
    # Результирующая строка, которая должна быть подписана:
    1658385579423XXXXXXXXXX5000{"category": "option"}
    
    # Пример результирующей подписи для HMAC:
    "f0da71972ce1811c882ca5e3fd1779791fb1fed499bef40e5558e50259acfd66"
    ```

Примеры HTTP-запросов:
  - GET
    ```
    GET /v5/order/realtime?category=option&symbol=BTC-29JUL22-25000-C HTTP/1.1
    Host: api-testnet.bybit.com
    -H 'X-BAPI-SIGN: XXXXXXXXXX' \
    -H 'X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx' \
    -H 'X-BAPI-TIMESTAMP: 1658384431891' \
    -H 'X-BAPI-RECV-WINDOW: 5000'
    ```
  - POST
    ```
    POST /v5/order/create HTTP/1.1
    Host: api-testnet.bybit.com
    -H 'X-Referer: XXXXXXXXXX' \    [the header for broker users only]
    -H 'X-BAPI-SIGN: XXXXXXXXXX' \
    -H 'X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx' \
    -H 'X-BAPI-TIMESTAMP: 1658385589135' \
    -H 'X-BAPI-RECV-WINDOW: 5000' \
    -H 'Content-Type: application/json' \
    -d '{"category": "option"}'
    ```

### Общие параметры ответа<p id="id19"></p>

```
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {},
    "retExtInfo": {},
    "time": 1671017382656
}
```

|Parameter  |Type	|Comments                                                                                                 |
|-----------|-------|---------------------------------------------------------------------------------------------------------|
|retCode    |number	|Код успеха/ошибки                                                                                        |
|retMsg     |string	|Сообщение успеха/ошибки. `"OK"`, `"success"`, `"SUCCESS"` или пустая строка указывают на успешный ответ  |
|result	    |Object |Результат бизнес-данных                                                                                  |
|retExtInfo |Object |Расширенная информация. В большинстве случаев это `{}`                                                   |
|time	    |number |Текущая временная метка (мс)                                                                             |

## Различные режимы аккаунтов<p id="id20"></p>

В настоящее время на платформе Bybit существует три режима аккаунтов: классический аккаунт, унифицированный аккаунт 1.0 и унифицированный аккаунт 2.0.

### Унифицированный аккаунт 2.0 (UTA 2.0)<p id="id21"></p>

Этот режим аккаунта является конечной версией унифицированного аккаунта, объединяющей инверсные контракты, USDT Perpetuals, USDT Futures, USDC Perpetuals, USDC Futures, спот и опционы в единую торговую систему. В режимах кросс-маржи и портфельной маржи маржа распределяется между всеми сделками.

### Унифицированный аккаунт 1.0 (UTA 1.0)<p id="id22"></p>

В этом режиме аккаунта сделки с инверсными контрактами ведутся в отдельном торговом счёте, и соответствующая маржинальная валюта должна быть внесена на «счёт инверсных производных» перед началом торговли. Маржа между инверсными контрактами и другими инструментами не распространяется и не делится. Сделки с USDT Perpetual, USDT Futures, USDC Perpetual, USDC Futures, спотом и опционами осуществляются внутри системы «унифицированной торговли».

### Классический аккаунт<p id="id23"></p>

В этом режиме аккаунта транзакции с контрактами и спотовые транзакции разделены. Транзакции с инверсными контрактами и USDT Perpetuals завершаются в "счёте производных", а спотовые транзакции — в "спотовом счёте".

### Определение режима аккаунта через API<p id="id24"></p>

Используйте ключ соответствующего аккаунта для вызова метода Get Account Info и посмотрите значение поля unifiedMarginStatus:

|Значение   |	Режим аккаунта                  |
|-----------|-----------------------------------|
|1      	|классический аккаунт               |
|3	        |UTA 1.0                            |
|4	        |UTA 1.0 (профессиональная версия)  |
|5	        |UTA 2.0                            |
|6	        |UTA 2.0 (профессиональная версия)  |

>Примечание:  
>UTA и UTA (pro) — это по сути одинаковые режимы, но версия Pro имеет небольшое преимущество в производительности при торговле через API.

### Изменения в использовании API для UTA 2.0<p id="id25"></p>

<table class="iksweb">
		<tr>
			<td rowspan="2">Категория API</td>
			<td rowspan="2">API</td>
			<td>UTA 2.0</td>
			<td>UTA 1.0</td>
		</tr>
		<tr>
			<td>category=inverse</td>
			<td>category=inverse</td>
		</tr>
		<tr>
			<td>Market</td>
			<td><a href="#id1">/v5/market/instruments-info</a></td>
			<td>"unifiedMarginTrade" имеет значение true после реализации UTA 2.0</td>
			<td>"unifiedMarginTrade" имеет значение false</td>
		</tr>
		<tr>
			<td rowspan="8">Trade</td>
			<td><a href="#id1">/v5/order/create</a></td>
			<td>Инверсные фьючерсы больше не поддерживают hedge-мод, поэтому "positionIdx" всегда `0`</td>
			<td>Инверсные фьючерсы поддерживают hedge-мод, поэтому "positionIdx" может быть `0`, `1`, `2`</td>
		</tr>
		<tr>
			<td><a href="#id1">/v5/order/realtime</a></td>
			<td>Для запроса заказов с конечным статусом используется `openOnly`=1, и сохраняются только последние 500 заказов</td>
			<td>Для запроса заказов с конечным статусом используется `openOnly`=2</td>
		</tr>
		<tr>
			<td><a href="#id1">/v5/order/history</a></td>
			<td>1. `orderStatus` не передаётся, по умолчанию запрашиваются все конечные заказы<br>2. Поддерживаются параметры `baseCoin` и `settleCoin`<br>3. Запрос активных заказов не поддерживается, некоторые конечные заказы ограничены для запроса<br>4. Отменённые заказы сохраняются до 24 часов<br>5. Могут быть запрошены только заказы, созданные после обновления</td>
			<td>1. `orderStatus` не передаётся, по умолчанию запрашиваются активные и конечные заказы<br>2. Параметры `baseCoin` и `settleCoin` не поддерживаются<br>3. Активные заказы и различные конечные заказы всегда поддерживаются<br>4. Нет такого ограничения</td>
		</tr>
		<tr>
			<td><a href="#id1">/v5/execution/list</a></td>
			<td>1. Поддерживает запрос по `baseCoin`<br>2. Возвращаемый `createType` имеет значение<br>3. Могут быть запрошены только транзакции, созданные после обновления</td>
			<td>1. Запрос по `baseCoin` не поддерживается<br>2. Возвращаемый `createType` всегда пустая строка `""`</td>
		</tr>
		<tr>
			<td><a href="#id1">/v5/order/create-batch</a></td>
			<td>Поддерживает инверсные контракты</td>
			<td>Не поддерживает инверсные контракты</td>
		</tr>
		<tr>
			<td><a href="#id1">/v5/order/amend-batch</a></td>
			<td>Поддерживает инверсные контракты</td>
			<td>Не поддерживает инверсные контракты</td>
		</tr>
		<tr>
			<td><a href="#id1">/v5/order/cancel-batch</a></td>
			<td>Поддерживает инверсные контракты</td>
			<td>Не поддерживает инверсные контракты</td>
		</tr>
		<tr>
			<td><a href="#id1">/v5/order/disconnected-cancel-all</a></td>
			<td>Поддерживает инверсные контракты; торговые заказы на инверсные будут отменены при срабатывании DCP</td>
			<td>Не поддерживает инверсные контракты; торговые заказы на инверсные не будут отменены при срабатывании DCP</td>
		</tr>
		<tr>
			<td rowspan="3">Pre-upgrade</td>
			<td><a href="#id1">/v5/pre-upgrade/order/history</a></td>
			<td>Поддерживает запрос заказов, созданных при состоянии классического аккаунта или унифицированного аккаунта 1.0</td>
			<td>-</td>
		</tr>
		<tr>
			<td><a href="#id1">/v5/pre-upgrade/execution/list</td>
			<td>Поддерживает запрос транзакций, созданных при состоянии классического аккаунта или унифицированного аккаунта 1.0</td>
			<td>-</td>
		</tr>
		<tr>
			<td><a href="#id1">/v5/pre-upgrade/position/closed-pnl</a></td>
			<td>Поддерживает запрос закрытого PnL, созданного при состоянии классического аккаунта или унифицированного аккаунта 1.0</td>
			<td>-</td>
		</tr>
		<tr>
			<td rowspan="5">Position</td>
			<td><a href="#id1">/v5/position/list</a></td>
			<td>1. Передача нескольких символов не поддерживается<br>2. В ответе изменились значения или использование полей `tradeMode`, `liqPrice`, `bustPrice`</td>
			<td>1. Поддерживает передачу нескольких символов</td>
		</tr>
		<tr>
			<td><a href="#id1">/v5/position/closed-pnl</a></td>
			<td>Может быть запрошен только закрытый PnL, созданный после обновления</td>
			<td>-</td>
		</tr>
		<tr>
			<td><a href="#id1">/v5/position/set-leverage</a></td>
			<td>Инверсные perpetual и инверсные фьючерсы поддерживают только односторонний режим позиций, и плечо(leverage) для buy и sell должны быть равны</td>
			<td>Инверсные фьючерсы поддерживают hedge-режим позиций, и плечо(leverage) для buy и sell могут быть неравными</td>
		</tr>
		<tr>
			<td><a href="#id1">/v5/position/switch-isolated</a></td>
			<td>Режим маржи стал на уровне аккаунта, этот интерфейс больше не применим</td>
			<td>Инверсные контракты поддерживают использование этого интерфейса</td>
		</tr>
		<tr>
			<td><a href="#id1">/v5/position/switch-mode</a></td>
			<td>Инверсные фьючерсы больше не поддерживают hedge-режим позиций</td>
			<td>Инверсные фьючерсы поддерживают hedge-режим позиций</td>
		</tr>
		<tr>
			<td rowspan="3">Account</td>
			<td><a href="#id1">/v5/account/wallet-balance</a></td>
			<td>Не поддерживает accountType=CONTRACT</td>
			<td>Поддерживает accountType=CONTRACT</td>
		</tr>
		<tr>
			<td><a href="#id1">/v5/account/transaction-log</a></td>
			<td>Журналы транзакций для инверсных контрактов будут включены</td>
			<td>Журнал транзакций инверсного контракта необходимо получать через интерфейс ниже</td>
		</tr>
		<tr>
			<td><a href="#id1">/v5/account/contract-transaction-log</a></td>
			<td>После обновления до UTA 2.0 этот интерфейс больше не применим</td>
			<td>Данные из UTA 1.0 или классического аккаунта могут быть получены</td>
		</tr>
		<tr>
			<td rowspan="2">Asset</td>
			<td><a href="#id1">/v5/asset/delivery-record</a></td>
			<td>Поддерживает записи доставки инверсных фьючерсов</td>
			<td>Не поддерживает записи доставки инверсных фьючерсов</td>
		</tr>
		<tr>
			<td>Все интерфейсы, включающие `accountType` в этом каталоге</td>
			<td>CONTRACT больше не поддерживается, поскольку "inverse derivatives account" больше не существует</td>
			<td>Поддерживает CONTRACT (inverse derivatives account)</td>
		</tr>
		<tr>
			<td rowspan="2">WebSocket Stream/Trade</td>
			<td><a href="#id1">wss://stream.bybit.com/v5/trade</a></td>
			<td>Поддерживает инверсные контракты</td>
			<td>Не поддерживает инверсные контракты</td>
		</tr>
</table>

## Получить объявление<p id="id26"></p>

### Конечная точка<p id="id27"></p>

`GET /v5/announcements/index`

### Пример запроса<p id="id28"></p>
  - HTTP
    ```
    GET /v5/announcements/index?locale=en-US&limit=1 HTTP/1.1
    Host: api.bybit.com
    ```
  - Python
    ```
    from pybit.unified_trading import HTTP
    session = HTTP(testnet=True)
    print(session.get_announcement(
        locale="en-US",
        limit=1,
    ))
    ```

### Параметры запроса<p id="id29"></p>

|Параметр        	  |Обязательный	  |Тип	  |Комментарии                             |По умолчанию  |
|---------------------|---------------|---------|----------------------------------------|--------------|
|[locale](#ida)       |да	          |string   |Символ языка                            |-             |
|[type](#idb)         |нет            |string   |Тип объявления                          |-             |
|[tag](#idc)       	  |нет            |string   |Тег объявления                          |-             |
|page                 |нет            |integer  |Номер страницы                          |1             |
|limit	              |нет            |integer  |Ограничение размера данных на странице  |20            |

### Пример ответа<p id="id30"></p>

```
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "total": 735,
        "list": [
            {
                "title": "New Listing: Arbitrum (ARB) — Deposit, Trade and Stake ARB to Share a 400,000 USDT Prize Pool!",
                "description": "Bybit is excited to announce the listing of ARB on our trading platform!",
                "type": {
                    "title": "New Listings",
                    "key": "new_crypto"
                },
                "tags": [
                    "Spot",
                    "Spot Listings"
                ],
                "url": "https://announcements.bybit.com/en-US/article/new-listing-arbitrum-arb-deposit-trade-and-stake-arb-to-share-a-400-000-usdt-prize-pool--bltf662314c211a8616/",
                "dateTimestamp": 1679045608000,
                "startDateTimestamp": 1679045608000,
                "endDateTimestamp": 1679045608000
            }
        ]
    },
    "retExtInfo": {},
    "time": 1679415136117
}
```

### Параметры ответа<p id="id31"></p>

|Параметр	        |Тип            |Комментарии                                                                                              |
|-------------------|---------------|---------------------------------------------------------------------------------------------------------|
|total              |integer    	|Общее количество записей                                                                                 |
|list	            |array      	|Объект                                                                                                   |
|title	            |string     	|Заголовок объявления                                                                                     |
|description	    |string     	|Описание объявления                                                                                      |
|type	            |object     	|-                                                                                                         |
|title	            |string     	|Заголовок типа объявления                                                                                |
|[key](#idb)        |string     	|Ключ типа объявления                                                                                     |
|[tags](#idc)  	    |array<string>	|Тег объявления                                                                                           |
|url	            |string	        |URL объявления                                                                                           |
|dateTimestamp	    |number     	|Временная метка, которую заполняет автор                                                                 |
|startDataTimestamp	|number     	|Начальная временная метка (мс) события (действительна только при list.type.key == "latest_activities")   |
|endDataTimestamp	|number     	|Конечная временная метка (мс) события (действительна только при list.type.key == "latest_activities")    |
|publishTime	    |number     	|Временная метка публикации объявления                                                                    |


## Предотвращение самосовпадения (Self Match Prevention, SMP)<p id="id32"></p>

### Что такое SMP?<p id="id33"></p>

Функция Self Match Prevention позволяет пользователям выбирать способ исполнения при размещении ордера. Когда контрагент — тот же самый UID или принадлежит к той же указанной группе SMP, исполнение происходит следующим образом:

- Cancel maker: отменить мейкер-ордер при исполнении; тейкер-ордер остаётся.
- Cancel taker: отменить тейкер-ордер при исполнении; мейкер-ордер остаётся.
- Cancel both: отменить оба — и тейкер, и мейкер — при исполнении.
  
После того как ордер размещён в книге ордеров, его smpType становится недействительным. Это означает, например, что если вы размещаете тейкер-ордер без smpType (`smpType=None`), который совпадает с вашим существующим мейкер-ордером, установленным с `smpType=CancelMaker`, тейкер-ордер будет исполнен. Это происходит потому, что `smpType=CancelMaker` у мейкер-ордера становится недействительным после попадания в книгу ордеров.

### Как настроить SMP?<p id="id34"></p>

Проверьте параметры запроса [/v5/order/create](#id1). Укажите параметр `smpType` при размещении ордера.

### Что такое SMP Trade Group? (Группа торговли SMP)<p id="id35"></p>

SMP доступен для любого пользователя на уровне UID.
Управление SMP Trade Group в настоящее время доступно только для учреждений.

SMP Trade Group: относится к группе UID. Когда любой из UID в этой группе размещает ордер и выбрана политика исполнения SMP, она будет активирована, если мейкер-ордер под любым из UID в этой группе будет совпасть.

Подробности:

- Каждый UID может входить только в одну SMP Trade Group.
- SMP Trade Group является группой управления на уровне UID, поэтому когда основной аккаунт присоединяется к SMP Trade Group, все субаккаунты под этим основным аккаунтом автоматически присоединятся к данной группе торговли.
- Если основной аккаунт уже присоединился к SMP Trade Group и субаккаунт создан после этого, этот новый субаккаунт автоматически присоединится к той же SMP Trade Group по умолчанию.
- Субаккаунт не обязательно должен быть привязан к той же SMP Trade Group, что и основной аккаунт. Это только поведение по умолчанию. Его можно вручную перевести в другие группы при необходимости.
- Связь между SMP Trade Group и UID может изменяться: когда UID присоединяется к новой SMP Trade Group или удаляется из SMP Trade Group. Эта операция не влияет на существующие ордера, она влияет только на вновь размещаемые ордера после изменения связи.
- Заметки: На основе этого мы настоятельно рекомендуем, что при изменении SMP Trade Group вы должны отменить все существующие ордера, чтобы избежать неожиданного исполнения.
Приоритет SMP Trade Group выше в исполнении SMP, поэтому индивидуальный UID учитывается только при отсутствии SMP Trade Group на любой стороне.

После того как ордер находится в книге ордеров, его флаг SMP больше не имеет значения. Система всегда следует тегу на последнем ордере.

***Примеры:***  
1 января: UID1 присоединяется к SMP Trade Group A и размещает Order1.  
2 января: UID1 удаляется из SMP Trade Group A, но Order1 всё ещё активен и "новый".

- Кейс 1: Если UID1 присоединился к SMP Trade Group B и разместил Order2, если Order2 встречает Order1, он будет исполнен, поскольку они принадлежат к двум разным группам.
- Кейс 2: Если UID1 не присоединился к другим группам после удаления из SMP Trade Group A и разместил Order2, если Order2 встречает Order1, SMP будет активирован, потому что UID1 не имел группы при размещении Order2, поэтому SMP был активирован на уровне UID (тот же UID1).

### Как управлять моими UID и SMP Trade Group?<p id="id36"></p>

Вы можете связаться с вашим менеджером по институциональным вопросам или отправить email Bybit на: institutional_services@bybit.com.

## Как начать Copy Trading<p id="id37"></p>

### Стать Master Trader<p id="id38"></p>

Перейдите [сюда](https://www.bybit.com/copyTrade/), чтобы подать заявку на становление Master Trader.

### Создать API KEY<p id="id39"></p>

Разрешения "Contract - Orders & Positions" обязательны для ордеров Copy Trading.

### Область применения<p id="id40"></p>

Начиная с этого времени, как классический аккаунт, так и unified аккаунт поддерживают Copy Trading, но могут торговать только USDT Perpetual символами. Пожалуйста, проверьте поле `copyTrading` в [/v5/market/instruments-info](#id1).

### Разместить ордер Copy Trading<p id="id41"></p>

Используйте endpoint V5 [/v5/order/create](#id1) для размещения ордера Copy Trading.

Примеры запроса:
  - HTTP
    ```
    POST /v5/order/create HTTP/1.1
    Host: api-testnet.bybit.com
    X-BAPI-SIGN: XXXXXX
    X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx
    X-BAPI-TIMESTAMP: 1698376189371
    X-BAPI-RECV-WINDOW: 5000
    Content-Type: application/json
    Content-Length: 207
    ```

Примеры ответа:

    ```
    {
        "symbol": "BTCUSDT",
        "side": "Buy",
        "orderType": "Limit",
        "category": "linear",
        "qty": "0.1",
        "price": "29000",
        "timeInForce": "GTC",
        "positionIdx": 1
    }
    ```

## Сервис Demo Trading<p id="id42"></p>

### Введение<p id="id43"></p>

Bybit v5 Open API поддерживает аккаунт для демо-торговли, но обратите внимание, что не все API доступны для аккаунта демо-торговли, поскольку демо-сервис предназначен главным образом для опыта торговли, поэтому у него не полный функционал по сравнению с реальной торговлей.

### Создать API Ключ<p id="id44"></p>

Вам нужно войти в свой [mainnet](https://www.bybit.com/) аккаунт.
Переключитесь на Demo Trading. Обратите внимание, что это независимый аккаунт только для демо-торговли, и у него свой собственный пользовательский ID.
Наведите мышку на аватар пользователя, затем нажмите "API", чтобы сгенерировать api ключ и секрет.

### Правила использования<p id="id45"></p>

Основные правила торговли такие же, как и в реальной торговле.
Ордера, сгенерированные в демо-торговле, хранятся 7 дней.
Лимиты по умолчанию, не поддаются повышению. 

### Домен<p id="id46"></p>

Rest API: `https://api-demo.bybit.com`  
Websocket: `wss://stream-demo.bybit.com` (обратите внимание, что поддерживаются только приватные стримы; для публичных стримов `wss://stream.bybit.com`; WS Trade не поддерживается).

### Подсказки<p id="id47"></p>

Обратите внимание, что демо-торговля — это изолированный модуль. Когда вы создаёте ключ из демо-торговли, пожалуйста, используйте вышеуказанный домен для подключения.
Кстати, бессмысленно использовать демо-сервис торгов на [testnet](https://testnet.bybit.com/) сайте, поэтому не создавайте ключ из Testnet demo trading.

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
    ```
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

|Параметр       	|Обязательный	|Тип   	  |Комментарии                                                 |По умолчанию|
|-------------------|---------------|---------|------------------------------------------------------------|------------|
|adjustType	        |false      	|integer  |0: добавить демо-средства; 1: уменьшить демо-средства       |0           |
|utaDemoApplyMoney	|false      	|array    |-                                                           |-           |	
|coin	            |false      	|string	  |Запрашиваемая монета, поддерживаются BTC, ETH, USDT, USDC   |-           |
|amountStr	        |false      	|string   |Запрашиваемая сумма                                         |-           |

>Максимальная запрашиваемая сумма в каждом запросе
>- BTC: "15"
>- ETH: "200"
>- USDT: "100000"
>- USDC: "100000"

### Создание демо-аккаунта<p id="id53"></p>

#### Конечная точка<p id="id54"></p>

`/v5/user/create-demo-member`

#### Примеры запроса<p id="id55"></p>

  - HTTP
    ```
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

```
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

|Параметр	        |Тип            |Комментарии        |
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
    ```
    GET /v5/system/status HTTP/1.1
    Host: api.bybit.com
    ```

### Параметры запроса<p id="id66"></p>

|Параметр     	|Обязательный	|Тип   	  |Комментарии                        |По умолчанию|
|---------------|---------------|---------|-----------------------------------|------------|
|id	            |false      	|string   |ID. Уникальный идентификатор       |-           |
|[state](#idd)	|false      	|string   |Состояние системы                  |-           |	

### Пример ответа<p id="id67"></p>

```
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

|Параметр	           |Тип             |Комментарии                                                                                                           |
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
    ```
    GET /v5/market/time HTTP/1.1
    Host: api.bybit.com
    ```
  - Python
    ```
    import requests

    url = "https://api-testnet.bybit.com/v5/market/time"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    ```
  - pybit
    ```
    from pybit.unified_trading import HTTP
    
    session = HTTP(testnet=True)
    print(session.get_server_time())
    ```

#### Параметры запроса<p id="id73"></p>

none

#### Пример ответа<p id="id74"></p>

```
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

|Параметр	   |Тип       |Комментарии                        |
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
    ```
    GET /v5/market/kline?category=inverse&symbol=BTCUSD&interval=60&start=1670601600000&end=1670608800000 HTTP/1.1
    Host: api-testnet.bybit.com
    ```
  - Python
    ```
    import requests

    url = "https://api-testnet.bybit.com/v5/market/kline"

    payload={}
    headers = {}
    parameters = {
        "category": "inverse",
        "symbol": "BTCUSDT",
        "interval": "60",
        "start": 1670601600000,
        "end": 1670608800000
    }
    
    response = requests.request("GET", url, data=payload, headers=headers, params=parameters)

    print(response.text)
    ```
  - pybit
    ```
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

|Параметр  	          |Обязательный	 |Тип   	|Комментарии                                      |По умолчанию|
|---------------------|--------------|----------|-------------------------------------------------|------------|
|[category](#idi)	  |true      	 |string    |Тип продукта                                     |linear      |
|[symbol](#idj)	      |true       	 |string    |Имя символа                                      |-           |	
|[interval](#idk)     |false      	 |string    |Интервал свечей                                  |-           |
|start	              |false      	 |integer   |Временная метка начала (мс)                      |-           |	
|end                  |false      	 |integer   |Временная метка окончания (мс)                   |-           |
|limit	              |false      	 |integer   |Лимит на размер данных на страницу. [1, 1000]    |200         |	

#### Пример ответа<p id="id80"></p>

```
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

Запрос исторических свечей по [mark price](https://www.bybit.com/en-US/help-center/s/article/Glossary-Bybit-Trading-Terms). Графики возвращаются группами в зависимости от запрошенного интервала.

>Охватывает: USDT-контракты / USDC-контракты / Инверсные контракты

#### Конечная точка<p id="83"></p>

`/v5/market/mark-price-kline`

#### Примеры запроса<p id="id84"></p>

  - HTTP
    ```
    GET /v5/market/mark-price-kline?category=linear&symbol=BTCUSDT&interval=15&start=1670601600000&end=1670608800000&limit=1 HTTP/1.1
    Host: api-testnet.bybit.com
    ```
  - Python
    ```
    import requests

    url = "https://api-testnet.bybit.com/v5/market/mark-price-kline"

    payload={}
    headers = {}
    parameters = {
        "category": "linear",
        "symbol": "BTCUSDT",
        "interval": "15",
        "start": 1670601600000,
        "end": 1670608800000,
        "limit": 1
    }
    
    response = requests.request("GET", url, data=payload, headers=headers, params=parameters)

    print(response.text)
    ```
  - pybit
    ```
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

|Параметр  	          |Обязательный	 |Тип   	|Комментарии                                      |По умолчанию|
|---------------------|--------------|----------|-------------------------------------------------|------------|
|[category](#idi)	  |false      	 |string    |Тип продукта                                     |linear      |
|[symbol](#idj)	      |true       	 |string    |Имя символа                                      |-           |	
|[interval](#idk)     |false      	 |string    |Интервал свечей                                  |-           |
|start	              |false      	 |integer   |Временная метка начала (мс)                      |-           |	
|end                  |false      	 |integer   |Временная метка окончания (мс)                   |-           |
|limit	              |false      	 |integer   |Лимит на размер данных на страницу. [1, 1000]    |200         |	

#### Пример ответа<p id="id86"></p>

```
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
- 2 Production Demo service (Демо-сервис продакшена)

### category<p id="idi"></p>

Unified Account (Унифицированный аккаунт)

- spot (Спот-торговля)
- linear (USDT-вечные контракты, USDT- фьючерсы и USDC-контракты, включая USDC-твечные и USDC-фьючерсы)
- inverse (Инверсные контракты, включая инверсные вечные и инверсные фьючерсы)
- option (Опционы)

Classic Account (Классический аккаунт)

- linear (USDT-вечные контракты)
- inverse (Инверсные контракты, включая инверсные вечные и инверсные фьючерсы)
- spot (Спот-торговля)

### symbol<p id="idj"></p>

>Это примеры того как должны ваглядить символы относительно плошадки

***USDT Perpetual:***

- BTCUSDT
- ETHUSDT

***USDT Futures:***

>Контракты USDT Futures, предлагаемые Bybit, включают следующие типы:
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
