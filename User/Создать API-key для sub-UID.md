- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос на создание нового API-key для недавно созданного sub-UID.

> Информация:
>
> Используется только API-key master-UID.
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

`/v5/user/create-sub-api`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  POST /v5/user/create-sub-api HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1676430005459
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  
  {
      "subuid": 53888000,
      "note": "testxxx",
      "readOnly": 0,
      "permissions": {
          "Wallet": [
              "AccountTransfer"
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
  end_point = "/v5/user/create-sub-api"
  complete_request = base_url + end_point
  
  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"
  
  data = {
      "subuid": 53888000,
      "note": "testxxx",
      "readOnly": 0,
      "permissions": {
          "Wallet": [
              "AccountTransfer"
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
  print(session.create_sub_api_key(
      subuid=53888000,
      note="testxxx",
      readOnly=0,
      permissions={
          "Wallet": [
              "AccountTransfer"
          ]
      },
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

| Параметр                                     | Обязательный  | Тип     | Комментарии                                                                                                                                                                                                                                                                                           | По умолчанию |
|----------------------------------------------|---------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| subuid                                       | да            | integer | ***Идентификатор sub-UID.***                                                                                                                                                                                                                                                                          | -            |
| note                                         | нет           | string  | ***Заметка для API-key.***                                                                                                                                                                                                                                                                            | -            |
| readOnly                                     | да            | integer | ***Уровень доступа***<br><br>- `0`: Чтение и запись<br>- `1`: Только чтение                                                                                                                                                                                                                           | -            |
| ips                                          | нет           | string  | ***Привязка к IP-адресам.***<br><br>- Если не передавать этот параметр или передать значение `*`, привязки к IP не будет<br>- API-key без привязки к IP станет недействительным через 90 дней<br>- API-key без привязки к IP станет недействительным через 7 дней после изменения пароля аккаунта     | -            |
| permissions                                  | да            | object  | ***Настройка типов разрешений.***<br><br>- Должен быть указан хотя бы один тип, иначе вернется ошибка                                                                                                                                                                                                 | -            |
| ContractTrade (данные объекта `permissions`) | нет           | array   | ***Контрактная торговля.***<br><br>- Пример и допустимые значения: [`"Order"`, `"Position"`]                                                                                                                                                                                                          | -            |
| Spot (данные объекта `permissions`)          | нет           | array   | ***Спотовая торговля.***<br><br>- Пример и допустимые значения: [`"SpotTrade"`]                                                                                                                                                                                                                       | -            |
| Options (данные объекта `permissions`)       | нет           | array   | ***Контракты USDC.***<br><br>- Пример и допустимые значения: [`"OptionsTrade"`]                                                                                                                                                                                                                       | -            |
| Wallet (данные объекта `permissions`)        | нет           | array   | ***Кошелек.***<br><br>- Пример и допустимые значения: [`"AccountTransfer"`, `"SubMemberTransferList"`] <br>- Аккаунты типа `Fund Custodial` не поддерживаются                                                                                                                                         | -            |
| Exchange (данные объекта `permissions`)      | нет           | array   | ***Конвертация.***<br><br>- Пример и допустимые значения: [`"ExchangeHistory"`]                                                                                                                                                                                                                       | -            |
| Earn (данные объекта `permissions`)          | нет           | array   | ***Продукты Earn.***<br><br>- Пример и допустимые значения: [`"Earn"`]                                                                                                                                                                                                                                | -            |
| Derivatives (данные объекта `permissions`)   | нет           | array   | **Устаревший параметр.**<br><br>- Система автоматически добавляет это разрешение в зависимости от типа вашего аккаунта (UTA или Classic)                                                                                                                                                              | -            |
| CopyTrading (данные объекта `permissions`)   | нет           | array   | **Устаревший параметр.** <br><br>- Теперь используется [Как начать Copy Trading](</16.Как начать Copy Trading.md>)<br><br>- Пример и допустимые значения: [`"CopyTrading"`]                                                                                                                           | -            |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "",
    "result": {
        "id": "16651283",
        "note": "testxxx",
        "apiKey": "xxxxx",
        "readOnly": 0,
        "secret": "xxxxxxxx",
        "permissions": {
            "ContractTrade": [],
            "Spot": [],
            "Wallet": [
                "AccountTransfer"
            ],
            "Options": [],
            "CopyTrading": [],
            "BlockTrade": [],
            "Exchange": [],
            "NFT": [],
            "Earn": ["Earn"]
        }
    },
    "retExtInfo": {},
    "time": 1676430007643
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

| Параметр      | Тип     | Комментарии                                                                                                                       |
|---------------|---------|-----------------------------------------------------------------------------------------------------------------------------------|
| id            | string  | ***Уникальный идентификатор.***                                                                                                   |
| note          | string  | ***Заметка к API-key.***                                                                                                          |
| apiKey        | string  | ***Созданный API-key.***                                                                                                          |
| readOnly      | integer | ***Уровень доступа.***<br><br>- `0`: Чтение и запись<br>- `1`: Только чтение                                                      |
| secret        | string  | ***Секретный ключ, связанный с API-key.***<br>- **Важно:** Секретный ключ нельзя получить через GET API. Сохраните его надежно    |
| permissions   | object  | ***Настроенные типы разрешений.***                                                                                                |
| ContractTrade | array   | ***Разрешения для контрактной торговли.***                                                                                        |
| Spot          | array   | ***Разрешения для спотовой торговли.***                                                                                           |
| Wallet        | array   | ***Разрешения для кошелька.***                                                                                                    |
| Options       | array   | ***Разрешения для контрактов USDC.***                                                                                             |
| Derivatives   | array   | ***Разрешения для Unified account.***                                                                                             |
| Exchange      | array   | ***Разрешения для конвертации.***                                                                                                 |
| Earn          | array   | ***Разрешения для продуктов Earn.***                                                                                              |
| BlockTrade    | array   | ***Разрешения для блочных сделок.***<br><br>- Неприменимо к sub-UID<br>- Всегда возвращает `[]`                                   |
| CopyTrading   | array   | **Устаревшее поле**<br><br>- Всегда возвращает `[]`                                                                               |
| NFT           | array   | **Устаревшее поле**<br><br>- Всегда возвращает `[]`                                                                               |
