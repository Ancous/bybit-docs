- [Информация](#информация)
- [Конечная точка](#конечная-точка)
- [Примеры запроса](#примеры-запроса)
- [Параметры запроса](#параметры-запроса)
- [Пример ответа](#пример-ответа)
- [Параметры ответа](#параметры-ответа)

<a id="информация"></a>

Запрос записи о депозитах субсчета с помощью API-ключа основного UID.

>Важное замечание:
>
>- `endTime` - `startTime` должно быть меньше 30 дней. По умолчанию запрашиваются записи за последние
> 30 дней.

<a id="конечная-точка"></a>

## Конечная точка

`/v5/asset/deposit/query-sub-member-record`

<a id="примеры-запроса"></a>

## Примеры запроса

- HTTP

  ```http
  GET /v5/asset/deposit/query-sub-member-record?coin=USDT&limit=1&subMemberId=592334 HTTP/1.1
  Host: api-testnet.bybit.com
  X-BAPI-API-KEY: "<api_key от биржи bybit>"
  X-BAPI-SIGN: <подпись>
  X-BAPI-TIMESTAMP: 1672192441294
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
  end_point = "/v5/asset/deposit/query-sub-member-record"
  complete_request = base_url + end_point

  api_key = "<api_key от биржи bybit>"
  secret_key = "<secret_key от биржи bybit>"
  time_stamp = str(int(time.time() * 1000))
  recv_window = "5000"

  data = {
      "coin": "USDT",
      "limit": 1,
      "subMemberId": 592334,
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

- pybit

  ```python
  from pybit.unified_trading import HTTP

  session = HTTP(
      testnet=True,
      api_key="<api_key от биржи bybit>",
      api_secret="<secret_key от биржи bybit>",
  )
  print(session.get_sub_deposit_records(
      coin="USDT",
      limit=1,
      subMemberId=592334,
  ))
  ```

<a id="параметры-запроса"></a>

## Параметры запроса

|Параметр  	                  |Обязательный	 |Тип  	  |Комментарии       |По умолчанию|
|-----------------------------|--------------|--------|------------------|------------|
|id                     |нет           |string  |***Внутренний идентификатор***<br><br>Может использоваться для уникальной идентификации и фильтрации депозита. При совместном использовании с другими параметрами это поле имеет наивысший приоритет.      |-   |
|txID                     |нет           |string  |***Идентификатор транзакции***<br><br>Обратите внимание, что данные, сгенерированные до 1 января 2024 года, не могут быть запрошены с использованием идентификатора транзакции.          |-   |
|subMemberId                     |да           |string  |***sub-UID***                      |-   |
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
        "rows": [],
        "nextPageCursor": ""
    },
    "retExtInfo": {},
    "time": 1672192441742
}
```

<a id="параметры-ответа"></a>

## Параметры ответа

|Параметр   |Тип       |Комментарии                                             |
|-----------|----------|--------------------------------------------------------|
|rows       |array     |Массив объектов                                             |
|id   |string    |Уникальный идентификатор                                             |
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
|nextPageCursor  |string    |Метка для следующей страницы (используется в параметре запроса `cursor` для пагинации)          |
