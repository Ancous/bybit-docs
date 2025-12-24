- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос на получение списка sub-UID не более 10 000

> Информация:
>
> Возвращает не более 10 000 sub-UID мастер-аккаунта. Используется только API-ключ master-пользователя.
<!-- -->
> Важное замечание:
>
> API-ключ master-UID должен обладать одним из следующих разрешений для вызова этой конечной точки:
>
>- “Account Transfer”
>- “Subaccount Transfer”
>- “Withdrawal”

<a id="конечная-точка"></a>

## Конечная точка

`/v5/user/query-sub-members`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/user/query-sub-members HTTP/1.1
  Host: api.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1676430318405
  X-BAPI-RECV-WINDOW: 5000
  ```

- собственная реализация

  ```python
  import time
  import hmac
  import hashlib
  import requests
  
  from urllib.parse import urlencode
  
  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/user/query-sub-members"
  complete_request = base_url + end_point
  
  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"
  
  data = {}
  
  param_str = time_stamp + api_key + recv_window + urlencode(data)
  
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
  
  response = requests.get(url=complete_request, headers=headers, params=data, timeout=10)

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
  print(session.get_sub_uid())
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

Отсутствуют

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "",
    "result": {
        "subMembers": [
            {
                "uid": "106314365",
                "username": "xxxx02",
                "memberType": 1,
                "status": 1,
                "remark": "",
                "accountMode": 5
            },
            {
                "uid": "106279879",
                "username": "xxxx01",
                "memberType": 1,
                "status": 1,
                "remark": "",
                "accountMode": 6
            }
        ]
    },
    "retExtInfo": {},
    "time": 1760388036728
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

| Параметр    | Тип     | Комментарии                                                                                                                          |
|-------------|---------|--------------------------------------------------------------------------------------------------------------------------------------|
| subMembers  | array   | ***Массив объектов.***                                                                                                               |
| uid         | string  | ***Идентификатор sub-UID.***                                                                                                         |
| username    | string  | ***Имя пользователя.***                                                                                                              |
| memberType  | integer | ***Тип аккаунта.***<br><br>- `1`: обычный sub-аккаунт<br>- `6`: кастодиальный sub-аккаунт                                            |
| status      | integer | ***Статус учётной записи.***<br><br>- `1`: активен<br>- `2`: вход запрещён<br>- `4`: заморожен                                       |
| accountMode | integer | ***Режим аккаунта.***<br><br>- `1`: Классический аккаунт<br>- `3`: UTA1.0<br>- `4`: UTA1.0 Pro<br>- `5`: UTA2.0<br>- `6`: UTA2.0 Pro |
| remark      | string  | ***Примечание.***                                                                                                                    |
