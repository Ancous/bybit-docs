- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос информации об API-ключе

> Информация:
>
> Для вызова используется тот API-ключ, информацию о котором нужно получить. Подходит как для master-UID,
> так, и для sub-UID.
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
        "id": "13770661",
        "note": "readwrite api key",
        "apiKey": "XXXXXX",
        "readOnly": 0,
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
            "Options": [
                "OptionsTrade"
            ],
            "Derivatives": [],
            "CopyTrading": [],
            "BlockTrade": [],
            "Exchange": [],
            "NFT": [],
            "Affiliate": [],
            "Earn": []
        },
        "ips": [
            "*"
        ],
        "type": 1,
        "deadlineDay": 66,
        "expiredAt": "2023-12-22T07:20:25Z",
        "createdAt": "2022-10-16T02:24:40Z",
        "unified": 0,
        "uta": 0,
        "userID": 24617703,
        "inviterID": 0,
        "vipLevel": "No VIP",
        "mktMakerLevel": "0",
        "affiliateID": 0,
        "rsaPublicKey": "",
        "isMaster": true,
        "parentUid": "0",
        "kycLevel": "LEVEL_DEFAULT",
        "kycRegion": ""
    },
    "retExtInfo": {},
    "time": 1697525990798
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

| Параметр      | Тип      | Комментарии                                                                                                                                             |
|---------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| id            | string   | ***Уникальный ID.***                                                                                                                                    |
| note          | string   | ***Заметка к API-ключу.***                                                                                                                              |
| apiKey        | string   | ***API-ключ.***                                                                                                                                         |
| readOnly      | integer  | ***Уровень доступа.***<br><br>- `0`: Чтение и запись<br>- `1`: Только чтение                                                                            |
| secret        | string   | ***Всегда возвращает `""`.***                                                                                                                           |
| permissions   | Object   | ***Настроенные типы разрешений.***                                                                                                                      |
| ContractTrade | array    | ***Разрешения для контрактной торговли.***<br><br>- `Order`, `Position`                                                                                 |
| Spot          | array    | ***Разрешения для спотовой торговли.***<br><br>- `SpotTrade`                                                                                            |
| Wallet        | array    | ***Разрешения для кошелька.***<br><br>- `AccountTransfer`<br>- `SubMemberTransfer` (master)<br>- `SubMemberTransferList` (sub)<br>- `Withdraw` (master) |
| Options       | array    | ***Разрешения для контрактов USDC.***<br><br>- `OptionsTrade`                                                                                           |
| Derivatives   | array    | ***Разрешение по умолчанию.***<br><br>- `DerivativesTrade`                                                                                              |
| Exchange      | array    | ***Разрешения для конвертации.***<br><br>- `ExchangeHistory`                                                                                            |
| Earn          | array    | ***Разрешения для продуктов Earn.***<br><br>- `Earn`                                                                                                    |
| NFT           | array    | **Устаревшее поле.**<br><br>- Всегда `[]`                                                                                                               |
| BlockTrade    | array    | ***Разрешения для блочных сделок.***<br><br>- Неприменимо к sub-UID<br>- Всегда `[]`                                                                    |
| Affiliate     | array    | ***Разрешения для партнёрской программы.***<br><br>- Только у партнёров, иначе `[]`                                                                     |
| CopyTrading   | array    | Всегда `[]`, так как мастер-трейдеры используют разрешение `ContractTrade` для CopyTrading                                                              |
| ips           | array    | ***Список IP-адресов, к которым привязан ключ.***                                                                                                       |
| type          | integer  | ***Тип API-ключа.***<br><br>- `1`: Персональный.<br>- `2`: Подключен к стороннему приложению                                                            |
| deadlineDay   | integer  | ***Оставшееся количество дней действия API-ключа.***<br><br>- Только для ключей без привязки к IP или если пароль аккаунта был изменён                  |
| expiredAt     | datetime | ***Дата истечения срока действия API-ключа.***<br><br>- Только для ключей без привязки к IP или если пароль аккаунта был изменён                        |
| createdAt     | datetime | ***Дата создания API-ключа.***                                                                                                                          |
| unified       | integer  | **Устаревшее поле.**                                                                                                                                    |
| uta           | integer  | ***Перешёл ли аккаунт на унифицированную торговлю.***<br><br>- `0`: обычный аккаунт<br>- `1`: унифицированный торговый аккаунт                          |
| userID        | integer  | ***UID.***                                                                                                                                              |
| inviterID     | integer  | ***UID пригласившего.***                                                                                                                                |
| vipLevel      | string   | ***VIP-уровень.***                                                                                                                                      |
| mktMakerLevel | string   | ***Уровень маркет-мейкера.***                                                                                                                           |
| affiliateID   | integer  | ***ID партнёрской программы.***<br><br>- `0` означает отсутствие привязки                                                                               |
| rsaPublicKey  | string   | ***RSA-публичный ключ.***                                                                                                                               |
| isMaster      | boolean  | ***Принадлежит ли этот API-ключ master-UID.***                                                                                                          |
| parentUid     | string   | ***UID основного аккаунта.***<br><br>- Возвращает `0`, если метод вызван с основного аккаунта                                                           |
| kycLevel      | string   | ***Уровень верификации (KYC) для персонального аккаунта.***<br><br>- `LEVEL_DEFAULT`, `LEVEL_1`, `LEVEL_2`                                              |
| kycRegion     | string   | ***Регион верификации (KYC) для персонального аккаунта.***                                                                                              |
