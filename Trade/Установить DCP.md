- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос на настройку DCP

>Зона применения:  
>
>`spot` - спот  
>`option` - опцион  
>`linear` - контракт (расчет в USDT, USDC, ...)
>
> - `Perpetual` - контракт без даты экспирации
> - `Futures` - контракт с датой экспирации
>
>`inverse` - контракт (расчет в BTC, ETH, ...)
>
> - `Perpetual` - контракт без даты экспирации
> - `Futures` - контракт с датой экспирации
<!-- -->
>Важно:
>
>На [UTA1.0](</13.Различные режимы аккаунтов.md#единый-торговый-аккаунт-1.0>) `inverse` конечная точка не
>поддерживается
<!-- -->
>Информация:
>
>Окно времени по умолчанию — 10 секунд.
>
>***Что такое Disconnection Protect (DCP)?***  
>На основе механизма частного подключения через WebSocket и heartbeat, Bybit предоставляет функцию защиты от отключения.
>Таймер запускается с момента первого отключения. Если сервер Bybit не получает сигнал на переподключение от клиента в
>течение более 10 (по умолчанию) секунд и возобновление heartbeat "ping", тогда клиент переходит в состояние
>"disconnection protect", и все активные `Futures` / `option` / `spot` ордера клиента будут автоматически
>отменены. Если в течение 10 секунд клиент переподключится и возобновит heartbeat "ping", таймер сбросится и
>перезапустится при следующем отключении.
>
>***Как включить DCP***  
>Если вам нужно включить/выключить функцию, вы можете обратиться к вашему менеджеру по работе с клиентами для
>консультации и подачи заявки.
>
>Вы можете использовать эту [конечную точку](</Account/Получить информацию DCP.md>) для получения текущей конфигурации DCP.
>
>Для успешного запуска DCP ваше приватное веб-сокетное соединение должно быть подписано на
> [поток-данных «dcp»](</WebSocket Stream/Private/Подключить трансляцию DCP.md>).
<!-- -->
>Совет:
>
>После успешной отправки запроса системе требуется определённое время для вступления запроса в силу. Рекомендуется
>повторить запрос или установку через 10 секунд.

<a id="конечная-точка"></a>

## Конечная точка

`/v5/order/disconnected-cancel-all`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  POST v5/order/disconnected-cancel-all HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1675852742375
  X-BAPI-RECV-WINDOW: 50000
  Content-Type: application/json
  
  {
    "timeWindow": 40
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
  end_point = "/v5/order/disconnected-cancel-all"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "timeWindow": 40,
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
  print(session.set_dcp(
      timeWindow=40,
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

|Параметр  	                  |Обязательный	 |Тип  	  |Комментарии       |По умолчанию|
|-----------------------------|--------------|--------|------------------|------------|
|timeWindow                     |да  |integer     |Время окна отключения. [`3`, `300`], единица измерения: секунда       |-   |
|product                     |нет  |string     |`OPTIONS`, `DERIVATIVES`, `SPOT`       |`OPTIONS`   |

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
