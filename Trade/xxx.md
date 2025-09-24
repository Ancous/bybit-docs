## Разместить ордер

Product type
UTA2.0, UTA1.0: linear, inverse, spot, option
classic account: linear, inverse, spot

-----------------------------------------------------------------------------------------------------------

Symbol name, like BTCUSDT, uppercase only

-----------------------------------------------------------------------------------------------------------

Whether to borrow. Unified account Spot trading only.
0(default): false, spot trading
1: true, margin trading, make sure you turn on margin trading, and set the relevant currency as collateral

-----------------------------------------------------------------------------------------------------------

Buy, Sell

-----------------------------------------------------------------------------------------------------------

Market, Limit

-----------------------------------------------------------------------------------------------------------

Order quantity
UTA account
Spot: Market Buy order by value by default, you can set marketUnit field to choose order by value or qty for market orders
Perps, Futures & Option: always order by qty
classic account
Spot: Market Buy order by value by default
Perps, Futures: always order by qty
Perps & Futures: if you pass qty="0" and specify reduceOnly=true&closeOnTrigger=true, you can close the position up to maxMktOrderQty or maxOrderQty shown on Get Instruments Info of current symbol

-----------------------------------------------------------------------------------------------------------

Select the unit for qty when create Spot market orders for UTA account
baseCoin: for example, buy BTCUSDT, then "qty" unit is BTC
quoteCoin: for example, sell BTCUSDT, then "qty" unit is USDT

-----------------------------------------------------------------------------------------------------------

Slippage tolerance Type for market order, TickSize, Percent
Support linear, inverse, spot trading, but take profit, stoploss, conditional orders are not supported
TickSize:
the highest price of Buy order = ask1 + slippageTolerance x tickSize;
the lowest price of Sell order = bid1 - slippageTolerance x tickSize
Percent:
the highest price of Buy order = ask1 x (1 + slippageTolerance x 0.01);
the lowest price of Sell order = bid1 x (1 - slippageTolerance x 0.01)

-----------------------------------------------------------------------------------------------------------

Slippage tolerance value
TickSize: range is [1, 10000], integer only
Percent: range is [0.01%, 10%], up to 2 decimals

-----------------------------------------------------------------------------------------------------------

Order price
Market order will ignore this field
Please check the min price and price precision from instrument info endpoint
If you have position, price needs to be better than liquidation price

-----------------------------------------------------------------------------------------------------------

Conditional order param. Used to identify the expected direction of the conditional order.
1: triggered when market price rises to triggerPrice
2: triggered when market price falls to triggerPrice
Valid for linear & inverse

-----------------------------------------------------------------------------------------------------------

If it is not passed, Order by default.
Order
tpslOrder: Spot TP/SL order, the assets are occupied even before the order is triggered
StopOrder: Spot conditional order, the assets will not be occupied until the price of the underlying asset reaches the trigger price, and the required assets will be occupied after the Conditional order is triggered
Valid for spot only

-----------------------------------------------------------------------------------------------------------

For Perps & Futures, it is the conditional order trigger price. If you expect the price to rise to trigger your conditional order, make sure:
triggerPrice > market price
Else, triggerPrice < market price
For spot, it is the TP/SL and Conditional order trigger price

-----------------------------------------------------------------------------------------------------------

Trigger price type, Conditional order param for Perps & Futures.
LastPrice
IndexPrice
MarkPrice
Valid for linear & inverse

-----------------------------------------------------------------------------------------------------------

Implied volatility. option only. Pass the real value, e.g for 10%, 0.1 should be passed. orderIv has a higher priority when price is passed as well

-----------------------------------------------------------------------------------------------------------

Time in force
Market order will always use IOC
If not passed, GTC is used by default

-----------------------------------------------------------------------------------------------------------

Used to identify positions in different position modes. Under hedge-mode, this param is required
0: one-way mode
1: hedge-mode Buy side
2: hedge-mode Sell side

-----------------------------------------------------------------------------------------------------------

User customised order ID. A max of 36 characters. Combinations of numbers, letters (upper and lower cases), dashes, and underscores are supported.
Futures & Perps: orderLinkId rules:
optional param
always unique
option orderLinkId rules:
required param
always unique

-----------------------------------------------------------------------------------------------------------

Take profit price
UTA: Spot Limit order supports take profit, stop loss or limit take profit, limit stop loss when creating an order

-----------------------------------------------------------------------------------------------------------

Stop loss price
UTA: Spot Limit order supports take profit, stop loss or limit take profit, limit stop loss when creating an order

-----------------------------------------------------------------------------------------------------------

The price type to trigger take profit. MarkPrice, IndexPrice, default: LastPrice. Valid for linear & inverse

-----------------------------------------------------------------------------------------------------------

The price type to trigger stop loss. MarkPrice, IndexPrice, default: LastPrice. Valid for linear & inverse

-----------------------------------------------------------------------------------------------------------

What is a reduce-only order? true means your position can only reduce in size if this order is triggered.
You must specify it as true when you are about to close/reduce the position
When reduceOnly is true, take profit/stop loss cannot be set
Valid for linear, inverse & option

-----------------------------------------------------------------------------------------------------------

What is a close on trigger order? For a closing order. It can only reduce your position, not increase it. If the account has insufficient available balance when the closing order is triggered, then other active orders of similar contracts will be cancelled or reduced. It can be used to ensure your stop loss reduces your position regardless of current available margin.
Valid for linear & inverse

-----------------------------------------------------------------------------------------------------------

Smp execution type. What is SMP?

-----------------------------------------------------------------------------------------------------------

Market maker protection. option only. true means set the order as a market maker protection order. What is mmp?

-----------------------------------------------------------------------------------------------------------

TP/SL mode
Full: entire position for TP/SL. Then, tpOrderType or slOrderType must be Market
Partial: partial position tp/sl (as there is no size option, so it will create tp/sl orders with the qty you actually fill). Limit TP/SL order are supported. Note: When create limit tp/sl, tpslMode is required and it must be Partial
Valid for linear & inverse

-----------------------------------------------------------------------------------------------------------

The limit order price when take profit price is triggered
linear & inverse: only works when tpslMode=Partial and tpOrderType=Limit
Spot(UTA): it is required when the order has takeProfit and "tpOrderType"=Limit

-----------------------------------------------------------------------------------------------------------

The limit order price when stop loss price is triggered
linear & inverse: only works when tpslMode=Partial and slOrderType=Limit
Spot(UTA): it is required when the order has stopLoss and "slOrderType"=Limit

-----------------------------------------------------------------------------------------------------------

The order type when take profit is triggered
linear & inverse: Market(default), Limit. For tpslMode=Full, it only supports tpOrderType=Market
Spot(UTA):
Market: when you set "takeProfit",
Limit: when you set "takeProfit" and "tpLimitPrice"

-----------------------------------------------------------------------------------------------------------

The order type when stop loss is triggered
linear & inverse: Market(default), Limit. For tpslMode=Full, it only supports slOrderType=Market
Spot(UTA):
Market: when you set "stopLoss",
Limit: when you set "stopLoss" and "slLimitPrice"

-----------------------------------------------------------------------------------------------------------

## Изменить ордер

User customised order ID. Either orderId or orderLinkId is required

-----------------------------------------------------------------------------------------------------------

Order ID. Either orderId or orderLinkId is required

-----------------------------------------------------------------------------------------------------------

TP/SL mode
Full: entire position for TP/SL. Then, tpOrderType or slOrderType must be Market
Partial: partial position tp/sl. Limit TP/SL order are supported. Note: When create limit tp/sl, tpslMode is required and it must be Partial
Valid for linear & inverse

-----------------------------------------------------------------------------------------------------------

Take profit price after modification. If pass "0", it means cancel the existing take profit of the order. Do not pass it if you do not want to modify the take profit. valid for spot(UTA), linear, inverse

-----------------------------------------------------------------------------------------------------------

Stop loss price after modification. If pass "0", it means cancel the existing stop loss of the order. Do not pass it if you do not want to modify the stop loss. valid for spot(UTA), linear, inverse

-----------------------------------------------------------------------------------------------------------

The price type to trigger take profit. When set a take profit, this param is required if no initial value for the order 

-----------------------------------------------------------------------------------------------------------

The price type to trigger stop loss. When set a take profit, this param is required if no initial value for the order

-----------------------------------------------------------------------------------------------------------

Trigger price type

-----------------------------------------------------------------------------------------------------------

Limit order price when take profit is triggered. Only working when original order sets partial limit tp/sl. valid for spot(UTA), linear, inverse

-----------------------------------------------------------------------------------------------------------

Limit order price when stop loss is triggered. Only working when original order sets partial limit tp/sl. valid for spot(UTA), linear, inverse

-----------------------------------------------------------------------------------------------------------

## Отменить ордер

Spot trading only
Order
tpslOrder
StopOrder
If not passed, Order by default

-----------------------------------------------------------------------------------------------------------

## Получить открытые и закрытые заказы

Symbol name, like BTCUSDT, uppercase only. For linear, either symbol, baseCoin, settleCoin is required

-----------------------------------------------------------------------------------------------------------

Base coin, uppercase only
Supports linear, inverse & option
option: it returns all option open orders by default

-----------------------------------------------------------------------------------------------------------

Order: active order, StopOrder: conditional order for Futures and Spot, tpslOrder: spot TP/SL order, OcoOrder: Spot oco order, BidirectionalTpslOrder: Spot bidirectional TPSL order
classic account spot: return Order active order by default
Others: all kinds of orders by default

-----------------------------------------------------------------------------------------------------------

Limit for data size per page. [1, 50]. Default: 20

-----------------------------------------------------------------------------------------------------------

Cursor. Use the nextPageCursor token from the response to retrieve the next page of the result set

-----------------------------------------------------------------------------------------------------------



-----------------------------------------------------------------------------------------------------------



-----------------------------------------------------------------------------------------------------------



-----------------------------------------------------------------------------------------------------------



-----------------------------------------------------------------------------------------------------------



-----------------------------------------------------------------------------------------------------------



-----------------------------------------------------------------------------------------------------------
