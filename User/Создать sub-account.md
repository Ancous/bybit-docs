- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос на создание sub-account

>Информация:
>
>Для вызова необходим API-ключ master-account.
<!-- -->
>Важное замечание:
>
>API-ключ master-account должен обладать одним из следующих разрешений для вызова этой конечной точки:
>
>- "Account Transfer"
>- "Subaccount Transfer"
>- "Withdrawal"

<a id="конечная-точка"></a>

## Конечная точка

`/v5/user/create-sub-member`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  POST /v5/user/create-sub-member HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1676429344202
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  
  {
      "username": "xxxxx",
      "memberType": 1,
      "switch": 1,
      "note": "test"
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
  end_point = "/v5/user/create-sub-member"
  complete_request = base_url + end_point
  
  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"
  
  data = {
      "username": "xxxxx",
      "memberType": 1,
      "switch": 1,
      "note": "test",
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
  print(session.create_sub_uid(
      username="xxxxx",
      memberType=1,
      switch=1,
      note="test",
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

|Параметр  	                  |Обязательный	 |Тип  	  |Комментарии       |По умолчанию|
|-----------------------------|--------------|--------|------------------|------------|
|username  |да |string |***Имя пользователя для нового sub-account.***<br><br>- Должно быть от 6 до 16 символов.<br>- Должно содержать как цифры, так и буквы. <br>- Не должно совпадать с существующими или удаленными именами пользователей. |-   |
|password |нет |string |***Пароль для нового sub-account.***<br><br>- Должен быть от 8 до 30 символов. <br>- Должен содержать цифры, прописные и строчные буквы. |-   |
|memberType |да |integer |***Тип аккаунта***<br><br>- `1`: обычный субаккаунт<br>- `6`: кастодиальный sub-account |-   |
|switch |нет |integer |***Настройка быстрого входа***<br><br>- `0`: выключить быстрый вход<br>- `1`: включить быстрый вход. |`0`   |
|isUta |нет |boolean |***Устаревший параметр***<br><br>Аккаунт всегда создается как UTA-аккаунт. |-   |
|note |нет |string |Заметка или комментарий для sub-account.   |-   |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "",
    "result": {
        "uid": "53888000",
        "username": "xxxxx",
        "memberType": 1,
        "status": 1,
        "remark": "test"
    },
    "retExtInfo": {},
    "time": 1676429344734
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр  |Тип       |Комментарии                                             |
|----------|----------|--------------------------------------------------------|
|uid |string |Идентификатор sub-UID. |
|username |string |Имя нового sub-account.<br>- 6-16 символов, должно содержать как цифры, так и буквы. <br> • Не должно совпадать с существующими или удаленными именами. |
|memberType |integer |Тип аккаунта<br>- `1`: обычный sub-аккаунт<br>- `6`: кастодиальный sub-аккаунт |
|status |integer |Статус учетной записи пользователя<br>- `1`: активен<br>- `2`: вход запрещен<br>- `4`: заморожен |
|remark |string |Примечание. |
