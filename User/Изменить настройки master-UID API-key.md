- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос на изменения настройк API-key master-UID.  
Для вызова этой конечной точки используйте API-key, настройки которого требуется изменить.
Используется только API-key master-UID.

> Информация:
>
> Изменению подлежит только тот API-key, который используется для вызова данного интерфейса.
>
> Для API-key с доступом на чтение и запись: добавление или удаление разрешений FiatP2P, FiatBybitPay и
> FiatConvertBroker запрещено.
<!-- -->
> Важное замечание:
>
> API-key master-UID должен обладать одним из следующих разрешений для вызова этой конечной точки:
>
> - “Account Transfer”
> - “Subaccount Transfer”
> - “Withdrawal”

<a id="конечная-точка"></a>

## Конечная точка

`/v5/user/update-api`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  POST /v5/user/update-api HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1676431264739
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  
  {
      "readOnly": null,
      "ips": "*",
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
              "CopyTrading": [
                  "CopyTrading"
              ],
              "BlockTrade": [],
              "Exchange": [
                  "ExchangeHistory"
              ],
              "NFT": [
                  "NFTQueryProductList"
              ]
          }
  }
  ```

- собственная реализация

  ```python
  import time
  import hmac
  import hashlib
  import json
  import requests
  
  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/user/update-api"
  complete_request = base_url + end_point
  
  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"
  
  data = {
      "ips": "*",
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
          "Derivatives": [
              "DerivativesTrade"
          ],
          "CopyTrading": [
              "CopyTrading"
          ],
          "BlockTrade": [],
          "Exchange": [
              "ExchangeHistory"
          ],
          "NFT": [
              "NFTQueryProductList"
          ]
      }
  }

  param_str = time_stamp + api_key + recv_window + json.dumps(data)
  
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
  
  response = requests.post(url=complete_request, headers=headers, json=data, timeout=10)
  
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
  print(session.modify_master_api_key(
      ips="*",
      permissions={
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
              "Derivatives": [
                  "DerivativesTrade"
              ],
              "CopyTrading": [
                  "CopyTrading"
              ],
              "BlockTrade": [],
              "Exchange": [
                  "ExchangeHistory"
              ],
              "NFT": [
                  "NFTQueryProductList"
              ]
          }
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

| Параметр                                         | Обязательный | Тип     | Комментарии                                                                                                                                                                                                                                                                                                                | По умолчанию |
|--------------------------------------------------|--------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| readOnly                                         | нет          | integer | ***Уровень доступа.***<br><br>- `0`: чтение и запись<br>- `1`: только чтение                                                                                                                                                                                                                                               | `0`          |
| ips                                              | нет          | string  | ***Привязка к IP-адресам.***<br><br>- Пример: `"192.168.0.1,192.168.0.2"`<br>- Если не передавать этот параметр или передать значение `"*"`, привязки к IP не будет<br>- API-key без привязки к IP станет недействительным через 90 дней<br>- API-key станет недействительным через 7 дней после изменения пароля аккаунта | -            |
| permissions                                      | нет          | object  | ***Настройка типов разрешений.***<br><br>- Не передавайте этот параметр, если не хотите изменять разрешения                                                                                                                                                                                                                | -            |
| ContractTrade (данные объекта `permissions`)     | нет          | array   | ***Контрактная торговля.***<br><br>- `["Order", "Position"]`<br>- На русском отвечает за настройку `Единый торговый аккаунт - Контракты - Ордера ("Order") или Позиции ("Position")`                                                                                                                                       | -            |
| Spot (данные объекта `permissions`)              | нет          | array   | ***Спотовая торговля.***<br><br>- `["SpotTrade"]`<br>- На русском отвечает за настройку `Единый торговый аккаунт - СПОТ - Торговать`                                                                                                                                                                                       | -            |
| Wallet (данные объекта `permissions`)            | да           | array   | ***Кошелек.*** (Настройка влияет на запросы через API!!!)<br><br>- `["AccountTransfer", "SubMemberTransfer"]`<br>- На русском отвечает за настройку `Активы - Кошелек - Перевод с аккаунта ("AccountTransfer") или Перевод с субаккаунта ("SubMemberTransfer")`                                                            | -            |
| Options (данные объекта `permissions`)           | нет          | array   | ***Контракты USDC.***<br><br>- `["OptionsTrade"]`<br>- На русском отвечает за настройку `Единый торговый аккаунт - USDC контракты - Торговаля деревативами USDC`                                                                                                                                                           | -            |
| Exchange (данные объекта `permissions`)          | нет          | array   | ***Конвертация.***<br><br>- `["ExchangeHistory"]`<br>- На русском отвечает за настройку `Активы - Обмен - Конвертер: история обмена`                                                                                                                                                                                       | -            |
| Earn (данные объекта `permissions`)              | нет          | array   | ***Продукты Earn.***<br><br>- `["Earn"]`<br>- На русском отвечает за настройку `Earn - Earn - Гибкие накопления и Ончейн Earn`                                                                                                                                                                                             | -            |
| FiatP2P (данные объекта `permissions`)           | нет          | array   | ***P2P.***<br><br>- Если `readOnly`=`0` то нужно передовать  параметр `ips` для взаимодействием с этой настройкой<br>- [`FiatP2POrder`]<br>- [`Advertising`]<br>- На русском отвечает за настройку `Торговля в фиате - P2P - Ордера  ("FiatP2POrder") или Обьявления ("Advertising")`                                      | -            |
| FiatBybitPay (данные объекта `permissions`)      | нет          | array   | ***Bybit Pay.***<br><br>- Если `readOnly`=`0` то нужно передовать  параметр `ips` для взаимодействием с этой настройкой<br>- [`FaitPayOrder`]<br>- На русском отвечает за настройку `Торговля в фиате - BybitPay - Ордера`                                                                                                 | -            |
| FiatConvertBroker (данные объекта `permissions`) | нет          | array   | ***Фиатный конверт-брокер.***<br><br>- Если `readOnly`=`0` то нужно передовать  параметр `ips` для взаимодействием с этой настройкой<br> - [`FiatConvertBrokerOrder`]<br>- На русском отвечает за настройку `Торговля в фиате - Крипто-фиатный обмен (только брокерам) - Ордера`                                           | -            |
| Affiliate (данные объекта `permissions`)         | нет          | array   | ***Партнёрская программа.***<br><br>- `["Affiliate"]`<br>- Доступно только для партнёрской программы<br>- Если требуется это разрешение, убедитесь, что удалены все остальные разрешения                                                                                                                                   | -            |
| Derivatives (данные объекта `permissions`)       | нет          | array   | ***Деривативы.***<br><br>- `["DerivativesTrade"]`                                                                                                                                                                                                                                                                          | -            |
| BlockTrade (данные объекта `permissions`)        | нет          | array   | ***Блочные сделки.***<br><br>- `["BlockTrade"]`                                                                                                                                                                                                                                                                            | -            |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "",
    "result": {
        "id": "13770661",
        "note": "xxxxx",
        "apiKey": "xxxxx",
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
            "Derivatives": [
                "DerivativesTrade"
            ],
            "CopyTrading": [
                "CopyTrading"
            ],
            "BlockTrade": [],
            "Exchange": [
                "ExchangeHistory"
            ],
            "Earn": [],
            "NFT": [
                "NFTQueryProductList"
            ]
        },
        "ips": [
            "*"
        ]
    },
    "retExtInfo": {},
    "time": 1676431265427
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

| Параметр          | Тип     |   | Комментарии                                                                   |
|-------------------|---------|:--|-------------------------------------------------------------------------------|
| id                | string  |   | ***Уникальный идентификатор.***                                               |
| note              | string  |   | ***Заметка к API-key.***                                                      |
| apiKey            | string  |   | ***API-key.***                                                                |
| readOnly          | integer |   | ***Уровень доступа.***<br><br>- `0`: Чтение и запись<br>- `1`: Только чтение  |
| secret            | string  |   | ***Всегда возвращает `""`.***                                                 |
| permissions       | object  |   | ***Настроенные типы разрешений.***                                            |
| ContractTrade     | array   |   | ***Разрешения для контрактной торговли.***                                    |
| Spot              | array   |   | ***Разрешения для спотовой торговли.***                                       |
| Wallet            | array   |   | ***Разрешения для кошелька.***                                                |
| Options           | array   |   | ***Разрешения для контрактов USDC.***                                         |
| Derivatives       | array   |   | ***Разрешения для унифицированного счёта.***                                  |
| BlockTrade        | array   |   | ***Разрешения для блочных сделок.***                                          |
| Exchange          | array   |   | ***Разрешения для конвертации.***                                             |
| Earn              | array   |   | ***Разрешения для продуктов Earn.***                                          |
| Affiliate         | array   |   | ***Разрешения для партнёрской программы.***                                   |
| FiatP2P           | array   |   | ***Разрешения для P2P.***                                                     |
| FiatBybitPay      | array   |   | ***Разрешения для Bybit Pay.***                                               |
| FiatConvertBroker | array   |   | ***Разрешения для фиатного конверт-брокера.***                                |
| NFT               | array   |   | **Устаревшее поле.**<br><br>- Всегда возвращает `[]`                          |
| CopyTrading       | array   |   | **Устаревшее поле.**<br><br>- Всегда возвращает `[]`                          |
| ips               | array   |   | ***Список привязанных IP-адресов.***                                          |
