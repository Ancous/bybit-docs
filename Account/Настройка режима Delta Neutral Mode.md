- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

## Информация

Режим дельта-нейтральности предназначен для улучшения условий торговли пользователей, применяющих дельта-нейтральные
стратегии. Когда этот режим включён, позиции, соответствующие критериям дельта-нейтральности, получают более низкий
приоритет в очереди ADL (Auto-Deleveraging — автоматическое снижение плеча), что снижает риск их принудительного
закрытия в условиях экстремальной волатильности рынка.
Подробнее см. в статье справки [Delta Neutral Mode](https://www.bybit.com/en/help-center/article?id=1772092051700).

Вы можете включить или отключить режим дельта-нейтральности. Чтобы проверить текущий статус, используйте эндпоинт
[Получить лимит ценового поведения](<Получить лимит ценового поведения.md>) и найдите поле `deltaEnable` в ответе.

<a id="конечная-точка"></a>

## Конечная точка

`/v5/account/set-delta-mode`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  POST /v5/account/set-delta-mode HTTP/1.1
  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1773113846000
  X-BAPI-RECV-WINDOW: 5000
  Content-Type: application/json
  Content-Length: 20
  
  {
      "deltaEnable": "1"
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
  end_point = "v5/account/set-delta-mode"
  complete_request = base_url + end_point
  
  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"
  
  data = {
      "deltaEnable": "1"
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

<a id="параметры-запроса"></a>

## Параметры запроса

| Параметр     | Обязательный  | Тип         | Комментарии                               | По умолчанию |
|--------------|---------------|-------------|-------------------------------------------|--------------|
| deltaEnable  | да            | string      | - `1`: включить<br>- `0`: выключить       | -            |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "success",
    "result": {},
    "retExtInfo": {},
    "time": 1773113846355
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

| Параметр      | Тип           | Комментарии                                  |
|---------------|---------------|----------------------------------------------|
| resultStatus  | integer       | - `success`: успех<br>- `failed`: неудача    |
