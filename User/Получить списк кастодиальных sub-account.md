- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Запрос списка своих кастодиальных sub-UID для институционального клиента.

> Важное замечание:
>
> API-ключ master-UID должен обладать одним из следующих разрешений для вызова этой конечной точки:
>
> - “Account Transfer”
> - “Subaccount Transfer”
> - “Withdrawal”

<a id="конечная-точка"></a>

## Конечная точка

`/v5/user/escrow_sub_members`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/user/escrow_sub_members?pageSize=2 HTTP/1.1

  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1739763787703
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  ```

- собственная реализация

  ```python
  import time
  import hmac
  import hashlib
  import requests
  
  from urllib.parse import urlencode
  
  base_url = "https://api-testnet.bybit.com"
  end_point = "/v5/user/escrow_sub_members"
  complete_request = base_url + end_point
  
  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"
  
  data = {
    "pageSize": 2
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
| pageSize    | нет           | string | ***Количество записей на странице.***<br><br>- Можно запросить до 100 записей за один раз.                             | -            |
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
                "uid": "104274894",
                "username": "Private_Wealth_Management",
                "memberType": 12,
                "status": 1,
                "remark": "earn fund",
                "accountMode": 3
            },
            {
                "uid": "104274884",
                "username": "Private_Wealth_Management",
                "memberType": 12,
                "status": 1,
                "remark": "earn fund",
                "accountMode": 3
            }
        ],
        "nextCursor": "344"
    },
    "retExtInfo": {},
    "time": 1739763788699
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

| Параметр    | Тип     | Комментарии                                                                                                            |
|-------------|---------|------------------------------------------------------------------------------------------------------------------------|
| subMembers  | array   | ***Массив объектов.***                                                                                                 |
| uid         | string  | ***UID sub-UID.***                                                                                                     |
| username    | string  | ***Имя пользователя sub-UID.***                                                                                        |
| memberType  | integer | ***Тип аккаунта.***<br><br>- `12`: Кастодиальный sub-UID                                                               |
| status      | integer | ***Статус аккаунта.***<br><br>- `1`: Активен<br>- `2`: Вход запрещен<br>- `4`: Заморожен                               |
| accountMode | integer | ***Режим аккаунта.***<br><br>- `1`: Классический аккаунт<br>- `3`: UTA-аккаунт                                         |
| remark      | string  | ***Примечание.***                                                                                                      |
| nextCursor  | string  | ***Курсор.***<br><br>- Используйте значение `nextCursor` из ответа для получения следующей страницы набора результатов |
