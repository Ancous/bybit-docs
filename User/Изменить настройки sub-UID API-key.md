- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос на изменения настройк API-key sub-UID.  
Для вызова этой конечной точки используйте либо API-key sub-UID, настройки которого требуется изменить, либо API-key
master-UID для управления ключами своего sub-UID.

> Важное замечание:
>
> API-key должен обладать одним из следующих разрешений для вызова этой конечной точки:
>
> - Для API-key sub-UID:
>   - "Account Transfer"
>   - "Sub Member Transfer"
>
> - Для API-key master-UID:
>   - "Account Transfer"
>   - "Sub Member Transfer"
>   - "Withdrawal"

<a id="конечная-точка"></a>

## Конечная точка

`/v5/user/update-sub-api`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  POST /v5/user/update-sub-api HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1676431795752
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  
  {
      "readOnly": 0,
      "ips": "*",
      "permissions": {
              "ContractTrade": [],
              "Spot": [
                  "SpotTrade"
              ],
              "Wallet": [
                  "AccountTransfer"
              ],
              "Options": [],
              "CopyTrading": [],
              "BlockTrade": [],
              "Exchange": [],
              "NFT": []
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
  end_point = "/v5/user/update-sub-api"
  complete_request = base_url + end_point
  
  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"
  
  data = {
      "ips": "*",
      "permissions": {
          "ContractTrade": [],
          "Spot": [
              "SpotTrade"
          ],
          "Wallet": [
              "AccountTransfer"
          ],
          "Options": [],
          "Derivatives": [],
          "CopyTrading": [],
          "BlockTrade": [],
          "Exchange": [],
          "NFT": []
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
  print(session.modify_sub_api_key(
      readOnly=0,
      ips="*",
      permissions={
              "ContractTrade": [],
              "Spot": [
                  "SpotTrade"
              ],
              "Wallet": [
                  "AccountTransfer"
              ],
              "Options": [],
              "Derivatives": [],
              "CopyTrading": [],
              "BlockTrade": [],
              "Exchange": [],
              "NFT": []
          }
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

| Параметр                                     | Обязательный | Тип     | Комментарии                                                                                                                                                                                                                                                                                                                | По умолчанию |
|----------------------------------------------|--------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| apikey                                       | нет          | string  | ***Sub-UID API-key.***<br><br>- Обязательно передавайте, если вы используете master-UID для управления настройками sub-UID API-key. <br>- Нельзя передавать, если вы вызываете эндпоинт с соответствующим sub-UID API-key (будет ошибка)                                                                                   | -            |
| readOnly                                     | нет          | integer | ***Уровень доступа.***<br><br>- `0`: Чтение и запись<br>- `1`: Только чтение                                                                                                                                                                                                                                               | `0`          |
| ips                                          | нет          | string  | ***Привязка к IP-адресам.***<br><br>- Пример: `"192.168.0.1,192.168.0.2"`<br>- Если не передавать этот параметр или передать значение `"*"`, привязки к IP не будет<br>- API-key без привязки к IP станет недействительным через 90 дней<br>- API-key станет недействительным через 7 дней после изменения пароля аккаунта | -            |
| permissions                                  | нет          | object  | ***Настройка типов разрешений.***<br><br>- Не передавайте этот параметр, если не хотите изменять разрешения                                                                                                                                                                                                                | -            |
| ContractTrade (данные объекта `permissions`) | нет          | array   | ***Контрактная торговля.***<br><br>- `["Order", "Position"]`<br>- На русском отвечает за настройку `Единый торговый аккаунт - Контракты - Ордера ("Order") или Позиции ("Position")`                                                                                                                                       | -            |
| Spot (данные объекта `permissions`)          | нет          | array   | ***Спотовая торговля.***<br><br>- `["SpotTrade"]`<br>- На русском отвечает за настройку `Единый торговый аккаунт - СПОТ - Торговать`                                                                                                                                                                                       | -            |
| Wallet (данные объекта `permissions`)        | да           | array   | ***Кошелек.*** (Настройка влияет на запросы через API!!!)<br><br>- `["AccountTransfer", "SubMemberTransfer"]`<br>- На русском отвечает за настройку `Активы - Кошелек - Перевод с аккаунта ("AccountTransfer") или Перевод с субаккаунта ("SubMemberTransfer")`                                                            | -            |
| Options (данные объекта `permissions`)       | нет          | array   | ***Контракты USDC.***<br><br>- `["OptionsTrade"]`<br>- На русском отвечает за настройку `Единый торговый аккаунт - USDC контракты - Торговаля деревативами USDC`                                                                                                                                                           | -            |
| Exchange (данные объекта `permissions`)      | нет          | array   | ***Конвертация.***<br><br>- `["ExchangeHistory"]`<br>- На русском отвечает за настройку `Активы - Обмен - Конвертер: история обмена`                                                                                                                                                                                       | -            |
| Earn (данные объекта `permissions`)          | нет          | array   | ***Продукты Earn.***<br><br>- `["Earn"]`<br>- На русском отвечает за настройку `Earn - Earn - Гибкие накопления и Ончейн Earn`                                                                                                                                                                                             | -            |
| Derivatives (данные объекта `permissions`)   | нет          | array   | ***Деривативы.***<br><br>- `["DerivativesTrade"]`                                                                                                                                                                                                                                                                          | -            |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "",
    "result": {
        "id": "16651472",
        "note": "testxxx",
        "apiKey": "xxxxxx",
        "readOnly": 0,
        "secret": "",
        "permissions": {
            "ContractTrade": [],
            "Spot": [
                "SpotTrade"
            ],
            "Wallet": [
                "AccountTransfer"
            ],
            "Options": [],
            "Derivatives": [],
            "CopyTrading": [],
            "BlockTrade": [],
            "Exchange": [],
            "NFT": []
        },
        "ips": [
            "*"
        ]
    },
    "retExtInfo": {},
    "time": 1676431796263
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

| Параметр          | Тип     | Комментарии                                                                     |
|-------------------|---------|---------------------------------------------------------------------------------|
| id                | string  | ***Уникальный идентификатор.***                                                 |
| note              | string  | ***Заметка к API-key.***                                                        |
| apiKey            | string  | ***API-key.***                                                                  |
| readOnly          | integer | ***Уровень доступа.***<br><br>- `0`: Чтение и запись<br>- `1`: Только чтение    |
| secret            | string  | ***Всегда возвращает `""`.***                                                   |
| permissions       | object  | ***Настроенные типы разрешений.***                                              |
| ContractTrade     | array   | ***Разрешения для контрактной торговли.***                                      |
| Spot              | array   | ***Разрешения для спотовой торговли.***                                         |
| Wallet            | array   | ***Разрешения для кошелька.***                                                  |
| Options           | array   | ***Разрешения для контрактов USDC.***                                           |
| Derivatives       | array   | ***Разрешения для унифицированного счёта.***                                    |
| Exchange          | array   | ***Разрешения для конвертации.***                                               |
| Earn              | array   | ***Разрешения для продуктов Earn.***                                            |
| BlockTrade        | array   | ***Неприменимо к sub-аккаунту.***<br><br>- Всегда возвращает пустой массив `[]` |
| Affiliate         | array   | ***Неприменимо к sub-аккаунту.***<br><br>- Всегда возвращает пустой массив `[]` |
| FiatP2P           | array   | ***Неприменимо к sub-аккаунту.***<br><br>- Всегда возвращает пустой массив `[]` |
| FiatBybitPay      | array   | ***Неприменимо к sub-аккаунту.***<br><br>- Всегда возвращает пустой массив `[]` |
| FiatConvertBroker | array   | ***Неприменимо к sub-аккаунту.***<br><br>- Всегда возвращает пустой массив `[]` |
| NFT               | array   | **Устаревшее поле.**<br><br>- Всегда возвращает пустой массив `[]`              |
| CopyTrading       | array   | **Устаревшее поле.**<br><br>- Всегда возвращает пустой массив `[]`              |
| ips               | array   | ***Список привязанных IP-адресов.***                                            |
