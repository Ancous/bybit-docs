- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос на установку MMP

>Информация:
>
>Что такое MMP?
>
>Market Maker Protection (MMP) — это автоматизированный механизм, предназначенный для защиты маркет-мейкеров (MM) от
>рисков ликвидности и чрезмерной экспозиции на рынке. Он предотвращает одновременное исполнение сделок по котировкам,
>предоставленным MM, в течение короткого промежутка времени. MM может автоматически отзывать свои котировки, если
>количество контрактов, торгуемых по базовому активу, превышает настроенный порог в течение определенного временного
>интервала. После срабатывания MMP любые существующие ордера MMP автоматически отменяются, а новые ордера, помеченные
>как MMP, будут отклоняться в течение определенного периода — известного как период заморозки — чтобы MM могли
>переоценить рынок и скорректировать котировки.
>
>Как включить MMP?
>
>Отправьте письмо на адрес Bybit ([financial.inst@bybit.com](mailto:financial.inst@bybit.com)) или свяжитесь с вашим
>менеджером по развитию бизнеса (BD), чтобы подать заявку на MMP. После обработки настройки по умолчанию будут такими,
>как в таблице ниже:
>
>|Параметр	|Тип   |Комментарии    |Значение по умолчанию  |
>|----------|-------|---------------|------------------|
>|baseCoin	|string	|Базовая монета	|BTC|
>|window	|string	|Временное окно (миллисекунды)	|5000   |
>|frozenPeriod	|string	|Период заморозки (миллисекунды)	|100|
>|qtyLimit	|string	|Лимит количества	|100|
>|deltaLimit	|string	|Лимит дельты	|100|
>
>Применимо!
>
>Применяется только для `options`. При размещении ордера на `options` установите `mmp`=`true`, что означает, что
>вы помечаете этот ордер как MMP-ордер.
>
>Некоторые моменты для заметки!
>
>- В расчет `qtyLimit` и `deltaLimit` включается только количество maker-ордеров и дельта.
>- `qty_limit` — это сумма абсолютных значений qty каждой сделки.
>- `delta_limit` — абсолютное значение суммы qty * delta. Если любой из этих показателей достигает или превышает
> лимит, защита маркет-мейкера аккаунта будет активирована.

<a id="конечная-точка"></a>

## Конечная точка

`/v5/account/mmp-modify`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  POST /v5/account/mmp-modify HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1675833524616
  X-BAPI-RECV-WINDOW: 50000
  Content-Type: application/json
  
  {
      "baseCoin": "ETH",
      "window": "5000",
      "frozenPeriod": "100000",
      "qtyLimit": "50",
      "deltaLimit": "20"
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
  end_point = "/v5/account/mmp-modify"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "baseCoin": "ETH",
      "window": "5000",
      "frozenPeriod": "100000",
      "qtyLimit": "50",
      "deltaLimit": "20"
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
  print(session.set_mmp(
      baseCoin="ETH",
      window="5000",
      frozenPeriod="100000",
      qtyLimit="50",
      deltaLimit="20"
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

|Параметр	|Обязательный |Тип   |Комментарии    |По умолчанию  |
|----------|--------|-------|---------------|------------------|
|baseCoin	|да    |string	|***Базовая монета***<br><br>Только заглавными буквами	|`BTC`  |
|window	|да      |string	|***Временное окно (миллисекунды)***	|`5000`   |
|frozenPeriod	|да      |string	|***Период заморозки (миллисекунды)***<br><br>`0` означает, что сделка останется замороженной до тех пор, пока не будет сброшена вручную.	|`100`  |
|qtyLimit	|да      |string	|***Лимит количества***<br><br>Положительный и до 2 знаков после запятой   |`100`  |
|deltaLimit	|да      |string	|***Лимит дельты***<br><br>Положительный и до 2 знаков после запятой	|`100`  |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "success"
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

Отсутствуют
