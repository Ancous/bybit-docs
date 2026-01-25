- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос информации обо всех API-ключах, принадлежащих указанному sub-UID

> Важное замечание:
>
> - Любое разрешение позволяет получить доступ к этой конечной точке.
> - Вызывать метод может только master-UID.

<a id="конечная-точка"></a>

## Конечная точка

`/v5/user/sub-apikeys`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/user/sub-apikeys?subMemberId=100400345 HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1699515251088
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  ```

- собственная реализация

  ```python
  import time
  import hmac
  import hashlib
  import requests
  
  from urllib.parse import urlencode
  
  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/user/sub-apikeys"
  complete_request = base_url + end_point
  
  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"
  
  data = {
      "accountType": "UNIFIED",
      "coin": "BTC",
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

| Параметр    | Обязательный  | Тип     | Комментарии                                                                                                                | По умолчанию |
|-------------|---------------|---------|----------------------------------------------------------------------------------------------------------------------------|--------------|
| subMemberId | да            | string  | ***Sub-UID.***                                                                                                             | -            |
| limit       | нет           | integer | ***Количество записей на странице.***<br><br>- `[1, 20]`                                                                   | `20`         |
| cursor      | нет           | string  | ***Курсор.***<br><br>- Используйте значение `nextPageCursor` из ответа для получения следующей страницы набора результатов | -            |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "",
    "result": {
        "result": [
            {
                "id": "24828209",
                "ips": [
                    "*"
                ],
                "apiKey": "XXXXXX",
                "note": "UTA",
                "status": 3,
                "expiredAt": "2023-12-01T02:36:06Z",
                "createdAt": "2023-08-25T06:42:39Z",
                "type": 1,
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
                        "SubMemberTransferList"
                    ],
                    "Options": [
                        "OptionsTrade"
                    ],
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
                    "Earn": []
                },
                "secret": "******",
                "readOnly": false,
                "deadlineDay": 21,
                "flag": "hmac"
            }
        ],
        "nextPageCursor": ""
    },
    "retExtInfo": {},
    "time": 1699515251698
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

| Параметр       | Тип      | Комментарии                                                                                                                   |
|----------------|----------|-------------------------------------------------------------------------------------------------------------------------------|
| result         | array    | ***Массив объектов.***                                                                                                        |
| id             | string   | ***Уникальный ID.***                                                                                                          |
| ips            | array    | ***Список IP-адресов, к которым привязан ключ.***                                                                             |
| apiKey         | string   | ***API-ключ.***                                                                                                               |
| note           | string   | ***Заметка к API-ключу.***                                                                                                    |
| status         | integer  | ***Статус ключа.***<br><br>- `1`: постоянный<br>- `2`: просрочен<br>- `3`: действующий<br>- `4`: скоро истечёт (менее 7 дней) |
| expiredAt      | datetime | ***Дата истечения срока действия.***<br><br>- Только для ключей без привязки к IP или если пароль аккаунта был изменён        |
| createdAt      | datetime | ***Дата создания ключа.***                                                                                                    |
| type           | integer  | ***Тип API-ключа.***<br><br>- `1`: Персональный<br>- `2`: Подключен к стороннему приложению                                   |
| permissions    | Object   | ***Настроенные типы разрешений.***                                                                                            |
| ContractTrade  | array    | ***Контрактная торговля.***<br><br>- `Order`, `Position`                                                                      |
| Spot           | array    | ***Спотовая торговля.***<br><br>- `SpotTrade`                                                                                 |
| Wallet         | array    | ***Кошелёк.***<br><br>- `AccountTransfer`, `SubMemberTransferList`                                                            |
| Options        | array    | ***Контракты USDC.***<br><br>- `OptionsTrade`                                                                                 |
| Derivatives    | array    | ***Разрешение по умолчанию.***<br><br>- `DerivativesTrade`                                                                    |
| Exchange       | array    | ***Конвертация.***<br><br>- `ExchangeHistory`                                                                                 |
| Earn           | array    | ***Продукты Earn.***<br><br>- `Earn`                                                                                          |
| CopyTrading    | array    | Всегда `[]`. Мастер-трейдер использует разрешение `ContractTrade` для CopyTrading                                             |
| BlockTrade     | array    | ***Блочные сделки.***<br><br>- Неприменимо к sub-UID<br>- Всегда `[]`                                                         |
| Affiliate      | array    | ***Партнёрская программа.***<br><br>- Неприменимо к sub-UID<br>- Всегда `[]`                                                  |
| secret         | string   | ***Secret-API.***<br><br>- Всегда возвращает `"******"`                                                                       |
| readOnly       | boolean  | ***Режим только для чтения.***<br><br>- `true` или `false`                                                                    |
| deadlineDay    | integer  | ***Оставшееся количество дней действия.***<br><br>- Только для ключей без привязки к IP или если пароль аккаунта был изменён  |
| flag           | string   | ***Тип API-ключа.***                                                                                                          |
| nextPageCursor | string   | ***Метка для следующей страницы.***<br><br>- Используется в параметре запроса `cursor` для пагинации                          |
| NFT            | array    | **Устаревшее поле.**<br><br>- Всегда `[]`                                                                                     |
