- [Информация](#информация)
- [Поток данных](#поток-данных)
- [Подписка](#подписка)
- [Примеры подписки](#примеры-подписки)

<a id="информация"></a>

## Информация

Подписка на DCP, чтобы активировать функцию DCP.

>**Например:**
>
>***соединение A подписано на тему `dcp.future`, соединение C подписано на тему `dcp.option`, а соединение B — нет.***
>
>- Если соединение A активно, соединение B неактивно, соединение C активно, то в этом случае DCP не активируется.
>- Если соединение A активно, соединение B неактивно, соединение C неактивно, то в этом случае DCP не активируется.
>- Если соединение A неактивно, соединение B активно, соединение C неактивно, то DCP активируется при достижении
> порогового значения `timeWindow`.

<a id="поток-данных"></a>

## Поток данных

`dcp.future`\
`dcp.spot`\
`dcp.option`

<a id="подписка"></a>

## Подписка

```json
{
    "op": "subscribe",
    "args": [
        "dcp.future"
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
                  "dcp.future"
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
