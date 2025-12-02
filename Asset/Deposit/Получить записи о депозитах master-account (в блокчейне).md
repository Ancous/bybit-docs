- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос записей о депозитах

>Совет:
>
>- `endTime` - `startTime` должно быть меньше 30 дней. По умолчанию запрашиваются записи за последние
> 30 дней.
>- Поддерживается использование основного или дополнительного ключа API UID для запроса записей депозитов
> соответственно.

<a id="конечная-точка"></a>

## Конечная точка

`/v5/asset/deposit/query-record`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/asset/deposit/query-record?coin=USDT&limit=1 HTTP/1.1
  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1672191991544
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
  end_point = "/v5/asset/deposit/query-record"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  api_secret = "<api_secret от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "coin": "USDT",
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
  print(session.get_deposit_records(
      coin="USDT",
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

|Параметр  	                  |Обязательный	 |Тип  	  |Комментарии       |По умолчанию|
|-----------------------------|--------------|--------|------------------|------------|
|id                     |нет           |string  |***Внутренний идентификатор***<br><br>Может использоваться для уникальной идентификации и фильтрации депозита. При совместном использовании с другими параметрами это поле имеет наивысший приоритет.      |-   |
|txID                     |нет           |string  |***Идентификатор транзакции***<br><br>Обратите внимание, что данные, сгенерированные до 1 января 2024 года, не могут быть запрошены с использованием ID транзакции.          |-   |
|coin                     |нет           |string  |***Название монеты***<br><br>Только заглавными буквами       |-   |
|startTime  	                  |нет	 |integer   	  |***Временная метка начала выборки (в миллисекундах)***<br><br>Примечание: логика запроса фактически эффективна на основе второго уровня                       |-   |
|endTime  	                  |нет	 |integer   	  |***Временная метка конца выборки (в миллисекундах)***<br><br>Примечание: логика запроса фактически эффективна на основе второго уровня                      |-   |
|limit      |нет  |integer  |***Ограничение размера данных на странице.***<br><br>[`1`, `50`]          |`50`  |
|cursor	    |нет  |string   |***Курсор.***<br><br>- Используйте значение `nextPageCursor` из ответа для получения следующей страницы набора результатов   |-      |

<a id="пример-ответа"></a>

## Пример ответа

```json
{
    "retCode": 0,
    "retMsg": "success",
    "result": {
        "rows": [
            {
                "coin": "USDT",
                "chain": "TRX",
                "amount": "999.0496",
                "txID": "04bf3fbad2fc85b107a42cfdc5ff83110092b606ca754efa0f032f8b94b3262e",
                "status": 3,
                "toAddress": "TDGYpm5zPacnEqKV34TJPuhJhHom9hcXAy",
                "tag": "",
                "depositFee": "",
                "successAt": "1742728163000",
                "confirmations": "50",
                "txIndex": "0",
                "blockHash": "000000000436ab4dabc8a4a87beb2262d2d87f6761a825494c4f1d5ae11b27e8",
                "batchReleaseLimit": "-1",
                "depositType": "0",
                "fromAddress": "TJ7hhYhVhaxNx6BPyq7yFpqZrQULL3JSdb",
                "taxDepositRecordsId": "0",
                "taxStatus": 0,
                "id": "160237231"
            }
        ],
        "nextPageCursor": "eyJtaW5JRCI6MTYwMjM3MjMxLCJtYXhJRCI6MTYwMjM3MjMxfQ=="
    },
    "retExtInfo": {},
    "time": 1750798211884
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр   |Тип       |Комментарии                                             |
|-----------|----------|--------------------------------------------------------|
|rows       |array     |Массив объектов                                             |
|coin       |string    |Название монеты                                             |
|chain      |string    |Сеть                                             |
|amount     |string    |Сумма пополнения                                             |
|txID       |integer   |Идентификатор транзакции                                             |
|[status](</19.Определения значений в запросах и ответах.md#depositStatus>)  |string   |Статус депозита     |
|toAddress   |string    |Адрес для перевода                                             |
|tag   |string    |Тег адреса перевода                                             |
|depositFee   |string    |Комиссия за перевод                                            |
|successAt   |string    |Время успешного перевода                                             |
|confirmations   |string    |Количество блоков подтверждения                                             |
|txIndex   |string    |Порядковый номер транзакции                                             |
|blockHash   |string    |Номер хеша в цепочке                                             |
|batchReleaseLimit   |string    |Лимит депозита для этой монеты в этой цепочке.<br>`-1` означает отсутствие лимита.                                             |
|depositType   |string    |Тип депозита.<br>`0`: нормальный депозит<br>`10`: депозит достиг дневного лимита депозита<br>`20`: ненормальный депозит               |
|fromAddress   |string    |Адрес отправителя депозита<br>Отображается только когда депозит поступает с блокчейн-источника и адрес отправителя уникален, в противном случае возвращает `""`                                         |
|taxDepositRecordsId   |string    |Это поле используется в налоговых целях пользователями Bybit EU (Австрия). Укажите свой налоговый идентификатор.                                          |
|taxStatus   |integer   |Это поле используется для налоговых целей пользователями Bybit EU (Австрия)<br>`0`: Отчетность не требуется<br>`1`: Отчетность ожидается<br>`2`: Отчетность завершена                                         |
|id   |string    |Уникальный идентификатор                                             |
|nextPageCursor  |string    |Метка для следующей страницы (используется в параметре запроса `cursor` для пагинации)          |
