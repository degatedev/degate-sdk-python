# DeGate Public SDK Connector Python
[![PyPI version](https://img.shields.io/pypi/v/degate-connector)](https://pypi.python.org/pypi/degate-connector)
[![Python 3.6](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a lightweight library that works as a connector to [DeGate public SDK](https://api-docs.degate.com/cn/spot)

- Supported APIs:
    - Spot
    - Spot Websocket Market Stream
    - Spot User Data Stream
- Inclusion of examples
- Customizable base URL
- Response metadata can be displayed

## Installation

```bash
pip install degate-connector
```

## SDK
Usage examples:
```python
from degate.spot import Spot as Client

ETH = {
    "id": 0,
    "symbol": "ETH",
}
USDC = {
    "id": 8,
    "symbol": "USDC",
}
client = Client(tokens=[ETH,USDC])


# Get server timestamp
print(client.time())

# Get klines of ETHUSDC at 1m interval
print(client.klines("ETHUSDC", "1m"))
# Get last 10 klines of ETHUSDC at 1h interval
print(client.klines("ETHUSDC", "1h", limit=10))

# accountAddress、assetPrivateKey、accountId are required for user data endpoints
client = Client(accountAddress='<account_address>',assetPrivateKey='<DeGate AssetPrivateKey>',accountId='<account_id>',tokens=[ETH,USDC])
# Get account and balance information
print(client.account())

# Post a new order
params = {
    'symbol': 'ETHUSDC',
    'side': 'SELL',
    'type': 'LIMIT',
    'quantity': 0.1,
    'price': 9500
}

response = client.newOrder(**params)
print(response)
```
Please find `examples` folder to check for more endpoints.

### Testnet
[Spot Testnet](https://testnet.degate.com/) is available, it can be used to test.

To use testnet:
```python
from degate.spot import Spot as Client

client = Client(baseUrl='https://testnet-backend.degate.com')
print(client.time())
```

### Response Metadata
The DeGate API server provides weight usages in the headers of each response.
You can display them by initializing the client with `show_header=True`:

```python
from degate.spot import Spot as Client
client = Client(show_header=True)
print(client.time())
```

returns:

```python
{'data': {'serverTime': 1587990847650}, 'header': {'Context-Type': 'application/json;charset=utf-8', ...}}
```

If `ClientError` is received, it'll display full response meta information.

### Display logs

Setting the log level to `DEBUG` will log the request URL, payload and response text.

### Error

There are 2 types of error returned from the library:
- `degate.error.ClientError`
    - This is thrown when server returns `4XX`, it's an issue from client side.
    - It has 4 properties:
        - `status_code` - HTTP status code
        - `error_code` - Server's error code, e.g. `-1102`
        - `error_message` - Server's error message, e.g. `Unknown order sent.`
        - `header` - Full response header. 
- `degate.error.ServerError`
    - This is thrown when server returns `5XX`, it's an issue from server side.

## Websocket
```python
import time
from degate.websocket.spot.websocket_client import SpotWebsocketClient as WsClient

def message_handler(message):
    print(message)

ETH = {
    "id": 0,
    "symbol": "ETH",
}
USDC = {
    "id": 8,
    "symbol": "USDC",
}
wsClient = WsClient(tokens=[ETH,USDC])
wsClient.start()

wsClient.subscribeTicker(
    symbol="ETHUSDC",
    id=1,
    callback=message_handler,
)
time.sleep(300)
wsClient.stop()
```
More websocket examples are available in the `examples` folder

### Testnet
```python
from degate.websocket.spot.websocket_client import SpotWebsocketClient as WsClient

wsClient = WsClient(websocketBaseUrl='wss://testnet-goerli-ws.degate.com')
```