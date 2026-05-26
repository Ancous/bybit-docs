- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос информации об API-key

> Информация:
>
> Для вызова используется тот API-key, информацию о котором нужно получить. Подходит как для master-UID, так, и для
> sub-UID.
<!-- -->
> Важное замечание:
>
> Любое разрешение позволяет получить доступ к этой конечной точке.

<a id="конечная-точка"></a>

## Конечная точка

`/v5/user/query-api`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/user/query-api HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1676430842094
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
  end_point = "/v5/user/query-api"
  complete_request = base_url + end_point
  
  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"
  
  data = {}
  
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
  print(session.get_api_key_information())
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

Отсутствуют

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "",
    "result": {
        "id": "2208369",
        "note": "testnet",
        "apiKey": "XXXXXXXX",
        "readOnly": 1,
        "secret": "",
        "permissions": {
            "ContractTrade": [
                "Order",
                "Position"
            ],
            "Spot": [
                "SpotTrade"
            ],
            "Wallet": [
                "AccountTransfer",
                "SubMemberTransfer"
            ],
            "Options": [],
            "Derivatives": [
                "DerivativesTrade"
            ],
            "CopyTrading": [],
            "BlockTrade": [],
            "Exchange": [
                "ExchangeHistory"
            ],
            "NFT": [],
            "Affiliate": [],
            "Earn": [
                "Earn"
            ],
            "FiatP2P": [
                "FiatP2POrder",
                "Advertising"
            ],
            "FiatConvertBroker": [
                "FiatConvertBrokerOrder"
            ],
            "FiatGlobalPay": [],
            "FiatBitPay": [
                "FaitPayOrder"
            ],
            "BitCard": [
                "BitCard"
            ],
            "ByXPost": [
                "ByXPost"
            ]
        },
        "ips": [
            "18.181.170.164",
            "13.212.45.47",
            "13.212.45.48"
        ],
        "type": 1,
        "deadlineDay": -2,
        "expiredAt": "1970-01-01T00:00:00Z",
        "createdAt": "2025-10-13T03:20:45Z",
        "unified": 0,
        "uta": 1,
        "userID": 1448939,
        "inviterID": 0,
        "vipLevel": "PRO-1",
        "mktMakerLevel": "0",
        "affiliateID": 0,
        "rsaPublicKey": "",
        "isMaster": true,
        "parentUid": "0",
        "kycLevel": "LEVEL_1",
        "kycRegion": "MYS",
        "userIDInt64": "0",
        "inviterIDInt64": "0",
        "affiliateIDInt64": "0"
    },
    "retExtInfo": {},
    "time": 1776149990532
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

| Параметр            | Тип      | Комментарии                                                                                                                                             |
|---------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                  | string   | ***Уникальный ID.***                                                                                                                                    |
| note                | string   | ***Заметка к API-key.***                                                                                                                                |
| apiKey              | string   | ***API-key.***                                                                                                                                          |
| readOnly            | integer  | ***Уровень доступа.***<br><br>- `0`: Чтение и запись<br>- `1`: Только чтение                                                                            |
| secret              | string   | ***Всегда возвращает `""`.***                                                                                                                           |
| permissions         | object   | ***Настроенные типы разрешений.***                                                                                                                      |
| ContractTrade       | array    | ***Разрешения для контрактной торговли.***<br><br>- `Order`, `Position`                                                                                 |
| Spot                | array    | ***Разрешения для спотовой торговли.***<br><br>- `SpotTrade`                                                                                            |
| Wallet              | array    | ***Разрешения для кошелька.***<br><br>- `AccountTransfer`<br>- `SubMemberTransfer` (master)<br>- `SubMemberTransferList` (sub)<br>- `Withdraw` (master) |
| Options             | array    | ***Разрешения для контрактов USDC.***<br><br>- `OptionsTrade`                                                                                           |
| Derivatives         | array    | ***Разрешение по умолчанию.***<br><br>- `DerivativesTrade`                                                                                              |
| Exchange            | array    | ***Разрешения для конвертации.***<br><br>- `ExchangeHistory`                                                                                            |
| Earn                | array    | ***Разрешения для продуктов Earn.***<br><br>- `Earn`                                                                                                    |
| FiatP2P             | array    | ***Разрешения для P2P.***<br><br>- `FiatP2POrder`<br>- `Advertising`<br>- Не применяется к sub-аккаунту, всегда возвращает `[]`                         |
| FiatBitPay          | array    | ***Разрешения для Bybit Pay.***<br><br>- `FiatP2POrder`<br>- `Advertising`<br>- Не применяется к sub-аккаунту, всегда возвращает `[]`                   |
| FiatConvertBroker   | array    | ***Разрешения для фиатный конверт-брокер.***<br><br>- `FiatConvertBroker`<br>- Не применяется к sub-аккаунту, всегда возвращает `[]`                    |
| BitCard             | array    | ***Разрешения на использование карты Bybit.***<br><br>- `BitCard`<br>- Не применяется к sub-аккаунту                                                    |
| ByXPost             | array    | ***Разрешения на публикацию в сообществе.***<br><br>- `ByXPost`<br>- Не применяется к sub-аккаунту                                                      |
| Affiliate           | array    | ***Разрешения для партнёрской программы.***<br><br>- Только у партнёров, иначе `[]`                                                                     |
| BlockTrade          | array    | ***Разрешения для блочных сделок.***<br><br>- Неприменимо к sub-UID<br>- Всегда `[]`                                                                    |
| ips                 | array    | ***Список IP-адресов, к которым привязан ключ.***                                                                                                       |
| type                | integer  | ***Тип API-key.***<br><br>- `1`: Персональный.<br>- `2`: Подключен к стороннему приложению                                                              |
| deadlineDay         | integer  | ***Оставшееся количество дней действия API-key.***<br><br>- Только для ключей без привязки к IP или если пароль аккаунта был изменён                    |
| expiredAt           | datetime | ***Дата истечения срока действия API-key.***<br><br>- Только для ключей без привязки к IP или если пароль аккаунта был изменён                          |
| createdAt           | datetime | ***Дата создания API-key.***                                                                                                                            |
| uta                 | integer  | ***Перешёл ли аккаунт на унифицированную торговлю.***<br><br>- `0`: обычный аккаунт<br>- `1`: унифицированный торговый аккаунт                          |
| userID              | integer  | ***UID.***                                                                                                                                              |
| inviterID           | integer  | ***UID пригласившего.***                                                                                                                                |
| vipLevel            | string   | ***VIP-уровень.***                                                                                                                                      |
| mktMakerLevel       | string   | ***Уровень маркет-мейкера.***                                                                                                                           |
| affiliateID         | integer  | ***ID партнёрской программы.***<br><br>- `0` означает отсутствие привязки                                                                               |
| rsaPublicKey        | string   | ***RSA-публичный ключ.***                                                                                                                               |
| isMaster            | boolean  | ***Принадлежит ли этот API-key master-UID.***                                                                                                           |
| parentUid           | string   | ***UID основного аккаунта.***<br><br>- Возвращает `0`, если метод вызван с основного аккаунта                                                           |
| kycLevel            | string   | ***Уровень верификации (KYC) для персонального аккаунта.***<br><br>- `LEVEL_DEFAULT`, `LEVEL_1`, `LEVEL_2`                                              |
| kycRegion           | string   | ***Регион верификации (KYC) для персонального аккаунта.***                                                                                              |
| CopyTrading         | array    | **Устаревшее поле.**<br><br>- Всегда `[]`                                                                                                               |
| NFT                 | array    | **Устаревшее поле.**<br><br>- Всегда `[]`                                                                                                               |
| unified             | integer  | **Устаревшее поле.**                                                                                                                                    |
