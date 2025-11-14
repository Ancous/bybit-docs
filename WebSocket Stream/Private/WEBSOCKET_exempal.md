- [Информация](#информация)
- [Поток данных](#поток-данных)
- [Примеры подписки](#примеры-подписки)
- [Пример ответа при удачной подписки](#пример-ответа-при-удачной-подписки)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Подписка

<a id="поток-данных"></a>

## Поток данных

`xxxxx`

***Пример:***  
**xxxxx**

<a id="примеры-подписки"></a>

## Примеры подписки

- собственная реализация

  ```python
  import json
  import time
  import websocket
  
  URL = "wss://stream-testnet.bybit.com/v5/private"
  
  def on_message(ws, message):
      print(f"Полученное сообщение: {message}")
  
  def on_error(ws, error):
      print(f"Ошибка: {error}")
  
  def on_close(ws, close_status_code, close_msg):
      print(f"Соединение закрыто: {close_status_code} {close_msg}")
  
  def on_open(ws):
      print("Соединение открыто")
      request = {
          "op": "subscribe",
          "args": [
              "xxxxx"
          ]
      }
      ws.send(json.dumps(request))
  
  def run_websocket():
      while True:
          ws = websocket.WebSocketApp(URL)
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
  
  ```

<a id="пример-ответа-при-удачной-подписки"></a>

## Пример ответа при удачной подписки

```json
{
    "success":true,
    "ret_msg": "",
    "conn_id": "d427n9atbetr53r4s1eg-d2mt",
    "req_id": "",
    "op": "subscribe"
}
```

<a id="пример-ответа"></a>

## Пример ответа

```json

```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр  |Тип       |Комментарии                                             |
|----------|----------|--------------------------------------------------------|
|Параметр   |Тип      |Комментарии                                             |
|Параметр   |Тип      |Комментарии                                             |
|Параметр   |Тип      |Комментарии                                             |

x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x<br>
