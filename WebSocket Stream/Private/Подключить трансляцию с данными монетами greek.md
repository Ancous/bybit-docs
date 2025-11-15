- [Информация](#информация)
- [Поток данных](#поток-данных)
- [Подписка](#подписка)
- [Примеры подписки](#примеры-подписки)
- [Пример ответа при удачной подписки](#пример-ответа-при-удачной-подписки)
- [Пример получаемых данных](#пример-получаемых-данных)
- [Параметры получаемых данных](#параметры-получаемых-данных)

<a id="информация"></a>

Подписка на ленту новостей о greek монетах, чтобы видеть изменения в данных о greek монетах в режиме реального времени.
Только `option`.

<a id="поток-данных"></a>

## Поток данных

`greeks`

<a id="подписка"></a>

## Подписка

```json
{
    "op": "subscribe",
    "args": [
        "greeks"
    ]
}
```

<a id="примеры-подписки"></a>

## Примеры подписки

- собственная реализация

  ```python
  import hmac
  import json
  import time
  import websocket
  
  url = "wss://stream-testnet.bybit.com/v5/private"
  api_key = "<api_key от биржи bybit>"
  api_secret = "<api_secret от биржи bybit>"
  
  def on_message(ws, message):
      try:
          data = json.loads(message)
          print(f"Полученное сообщение: {message}")
      except json.JSONDecodeError:
          print(f"Не удалось распарсить сообщение: {message}")
          return
  
      if data.get("op") == "auth" and data.get("success") is True:
          print("Аутентификация успешна. Отправляю подписку на 'position'")
          subscribe_request = {
              "op": "subscribe",
              "args": [
                  "greeks"
              ]
          }
          ws.send(json.dumps(subscribe_request))
  
  def on_error(ws, error):
      print(f"Ошибка: {error}")
  
  def on_close(ws, close_status_code, close_msg):
      print(f"Соединение закрыто: {close_status_code} {close_msg}")
  
  def on_open(ws):
      print("Соединение открыто")
  
      expires = int((time.time() + 1) * 1000)
      signature = str(hmac.new(
          key=api_secret.encode("utf-8"),
          msg=f"GET/realtime{expires}".encode("utf-8"),
          digestmod="sha256"
      ).hexdigest())
  
      auth_request = {
          "op": "auth",
          "args": [
              api_key,
              expires,
              signature
          ]
      }
      ws.send(json.dumps(auth_request))

      print("Запрос аутентификации отправлен")
  
  def run_websocket():
      while True:
          ws = websocket.WebSocketApp(url)
          ws.on_message = on_message
          ws.on_error = on_error
          ws.on_close = on_close
          ws.on_open = on_open
  
          ws.run_forever(
              ping_interval=20,
              ping_timeout=5
          )
  
          print("Соединение потеряно. Попытка переподключения...")
          time.sleep(5)
  
  run_websocket()
  ```

- pybit

  ```python
  from time import sleep

  from pybit.unified_trading import WebSocket

  ws = WebSocket(
      testnet=True,
      channel_type="private",
      api_key="<api_key от биржи bybit>",
      api_secret="<api_secret от биржи bybit>",
  )

  def handle_message(message):
      print(message)

  ws.greek_stream(
    callback=handle_message
  )

  while True:
      sleep(1)
  ```

<a id="пример-ответа-при-удачной-подписки"></a>

## Пример ответа при удачной подписки

```json
{
    "success": true,
    "ret_msg": "",
    "op": "subscribe",
    "conn_id": "d266oeddaugoadim24og-76t74"
}
```

<a id="пример-получаемых-данных"></a>

## Пример получаемых данных

```json
{
    "id": "592324fa945a30-2603-49a5-b865-21668c29f2a6",
    "topic": "greeks",
    "creationTime": 1672364262482,
    "data": [
        {
            "baseCoin": "ETH",
            "totalDelta": "0.06999986",
            "totalGamma": "-0.00000001",
            "totalVega": "-0.00000024",
            "totalTheta": "0.00001314"
        }
    ]
}
```

<a id="параметры-получаемых-данных"></a>

## Параметры получаемых данных

|Параметр  |Тип       |Комментарии                                             |
|----------|----------|--------------------------------------------------------|
|id        |string    |Идентификатор сообщения                                             |
|topic     |string    |Название потока данных                                             |
|creationTime | number | Временная метка создания данных (в миллисекундах) |
|data | array | Массив объектов. |
|baseCoin   |string      |Базовая монета                                             |
|totalDelta   |string      |Значение Delta                                             |
|totalGamma   |string      |Значение Gamma                                             |
|totalVega   |string      |Значение Vega                                             |
|totalTheta   |string      |Значение Theta                                             |
