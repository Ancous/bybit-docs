- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос на получение списка sub-UID более 10 000

> Информация:
>
> Возвращает более 10 000 sub-UID мастер-аккаунта. Используется только API-ключ master-пользователя.
<!-- -->
> Важное замечание:
>
> API-ключ master-UID должен обладать одним из следующих разрешений для вызова этой конечной точки:
>
> - “Account Transfer”
> - “Subaccount Transfer”
> - “Withdrawal”

<a id="конечная-точка"></a>

## Конечная точка

`/v5/user/submembers`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/user/submembers?pageSize=1 HTTP/1.1
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
  end_point = "/v5/user/submembers"
  complete_request = base_url + end_point
  
  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"
  
  data = {
    "pageSize": 1
  }
  
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

<a id="параметры-запроса"></a>

## Параметры запроса

| Параметр    | Обязательный  | Тип    | Комментарии                                                                                                            | По умолчанию |
|-------------|---------------|--------|------------------------------------------------------------------------------------------------------------------------|--------------|
| pageSize    | нет           | string | ***Количество записей на странице.***<br><br>- Можно запросить до 100 записей за раз.                                  | -            |
| nextCursor  | нет           | string | ***Курсор.***<br><br>- Используйте значение `nextCursor` из ответа для получения следующей страницы набора результатов | -            |

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
        ],
        "nextCursor": "0"
    },
    "retExtInfo": {},
    "time": 1760388041006
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

| Параметр    | Тип     | Комментарии                                                                                                                          |
|-------------|---------|--------------------------------------------------------------------------------------------------------------------------------------|
| subMembers  | array   | ***Массив объектов.***                                                                                                               |
| uid         | string  | ***Идентификатор sub-UID.***                                                                                                         |
| username    | string  | ***Имя пользователя.***                                                                                                              |
| memberType  | integer | ***Тип аккаунта.***<br><br>- `1`: стандартный sub-аккаунт<br>- `6`: кастодиальный sub-аккаунт                                        |
| status      | integer | ***Статус учётной записи.***<br><br>- `1`: активен<br>- `2`: вход запрещён<br>- `4`: заморожен                                       |
| accountMode | integer | ***Режим аккаунта.***<br><br>- `1`: Классический аккаунт<br>- `3`: UTA1.0<br>- `4`: UTA1.0 Pro<br>- `5`: UTA2.0<br>- `6`: UTA2.0 Pro |
| remark      | string  | ***Примечание.***                                                                                                                    |
| nextCursor  | string  | ***Курсор.***<br><br>- Используйте значение `nextCursor` из ответа для получения следующей страницы набора результатов               |
