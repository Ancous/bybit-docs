- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос на получение компонентов Index Price

> Зона применения:  
>
> `spot` - спот  
> `option` - опцион  
> `linear` - контракт (расчет в USDT, USDC, ...)
>
> - `Perpetual` - контракт без даты экспирации
> - `Futures` - контракт с датой экспирации
>
> `inverse` - контракт (расчет в BTC, ETH, ...)
>
> - `Perpetual` - контракт без даты экспирации
> - `Futures` - контракт с датой экспирации

<a id="конечная-точка"></a>

## Конечная точка

`/v5/market/index-price-components`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/market/index-price-components?indexName=1000BTTUSDT HTTP/1.1
  Host: api-testnet.bybit.com
  ```

- собственная реализация

  ```python
  import requests

  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/market/index-price-components"

  complete_request = base_url + end_point
  parameters = {
      "indexName": "1000BTTUSDT",
  }
  
  response = requests.get(url=complete_request, params=parameters, timeout=10)

  print(response.json())
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

| Параметр    | Обязательный  | Тип    | Комментарии                                | По умолчанию |
|-------------|---------------|--------|--------------------------------------------|--------------|
| indexName   | да            | string | ***Название индекса.***<br><br>- `BTCUSDT` | -            |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
  "retCode": 0,
  "retMsg": "",
  "result": {
    "indexName": "1000BTTUSDT",
    "lastPrice": "0.0006496",
    "updateTime": "1758182745072",
    "components": [
      {
        "exchange": "GateIO",
        "spotPair": "BTT_USDT",
        "equivalentPrice": "0.0006485",
        "multiplier": "1000",
        "price": "0.0006485",
        "weight": "0.1383220862762299"
      },
      {
        "exchange": "Bybit",
        "spotPair": "BTTUSDT",
        "equivalentPrice": "0.0006502",
        "multiplier": "1000",
        "price": "0.0006502",
        "weight": "0.0407528429737999"
      },
      {
        "exchange": "Bitget",
        "spotPair": "BTTUSDT",
        "equivalentPrice": "0.000648",
        "multiplier": "1000",
        "price": "0.000648",
        "weight": "0.1629044859431618"
      },
      {
        "exchange": "BitMart",
        "spotPair": "BTT_USDT",
        "equivalentPrice": "0.000649",
        "multiplier": "1000",
        "price": "0.000649",
        "weight": "0.0432327388538453"
      },
      {
        "exchange": "Binance",
        "spotPair": "BTTCUSDT",
        "equivalentPrice": "0.00065",
        "multiplier": "1000",
        "price": "0.00065",
        "weight": "0.5322401401714303"
      },
      {
        "exchange": "Mexc",
        "spotPair": "BTTUSDT",
        "equivalentPrice": "0.0006517",
        "multiplier": "1000",
        "price": "0.0006517",
        "weight": "0.0825477057815328"
      }
    ]
  },
  "retExtInfo": {},
  "time": 1758182745621
}

```

<a id="параметры-ответа"></a>

## Параметры ответа

| Параметр        | Тип    | Комментарии                                                    |
|-----------------|--------|----------------------------------------------------------------|
| indexName       | string | ***Название индекса.***                                        |
| lastPrice       | string | ***Последняя цена индекса.***                                  |
| updateTime      | string | ***Временная метка последнего обновления (в миллисекундах).*** |
| components      | array  | ***Список компонентов, формирующих цену индекса.***            |
| exchange        | string | ***Название биржи.***                                          |
| spotPair        | string | ***Спотовая торговая пара на бирже.***                         |
| equivalentPrice | string | ***Эквивалентная цена.***                                      |
| multiplier      | string | ***Множитель, используемый для цены компонента.***             |
| price           | string | ***Фактическая цена.***                                        |
| weight          | string | ***Вес в расчете индекса.***                                   |
