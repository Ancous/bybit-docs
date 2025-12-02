- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос информации об адресе депозита для master-account.

<a id="конечная-точка"></a>

## Конечная точка

`/v5/asset/deposit/query-address`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/asset/deposit/query-address?coin=USDT&chainType=ETH HTTP/1.1
  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1672192792371
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
  end_point = "/v5/asset/deposit/query-address"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  api_secret = "<api_secret от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "coin": "USDT",
      "chainType": "ETH",
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

  response = requests.get(url=complete_request, headers=headers, json=data, timeout=10)

  print(response.json())
  ```

- pybit

  ```python
  from pybit.unified_trading import HTTP

  session = HTTP(
      testnet=True,
      api_key="<api_key от биржи bybit>",
      api_secret="<api_secret от биржи bybit>",
  )
  print(session.get_master_deposit_address(
      coin="USDT",
      chainType="ETH",
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

|Параметр    |Обязательный	 |Тип  	  |Комментарии                                                     |По умолчанию|
|------------|---------------|--------|----------------------------------------------------------------|------------|
|coin        |да   |string  |***Название монеты***<br><br>Только заглавными буквами       |-   |
|chainType       |нет   |string |Пожалуйста, используйте значение `chain` из [coin-info](</Asset/Получить информацию о монете.md>)        |-  |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "success",
    "result": {
        "coin": "USDT",
        "chains": [
            {
                "chainType": "Ethereum (ERC20)",
                "addressDeposit": "XXXXXX",
                "tagDeposit": "",
                "chain": "ETH",
                "batchReleaseLimit": "-1",
                "contractAddress": "831ec7"
            }
        ]
    },
    "retExtInfo": {},
    "time": 1736394811459
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр   |Тип       |Комментарии                                             |
|-----------|----------|--------------------------------------------------------|
|coin       |string    |Название монеты                                             |
|chains      |array    |Массив объектов                                             |
|chainType       |string     |Тип сети                                             |
|addressDeposit   |string    |Адрес депозита                                             |
|tagDeposit     |string    |Тег депозита                                             |
|chain       |string   |Сеть                                             |
|batchReleaseLimit   |string    |Лимит депозита для этой монеты в этой цепочке.<br>`"-1"` означает отсутствие лимита.                                             |
|contractAddress   |string    |Адрес контракта монеты.<br>Отображаются только последние 6 символов.<br>Если адрес контракта отсутствует, отображается `""`.      |
