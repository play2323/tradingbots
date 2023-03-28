import kucoin.client as kucoin_client

class KuCoinAPI:
    def __init__(self, api_key, api_secret, api_passphrase):
        self.client = kucoin_client.TradeAPI(api_key, api_secret, api_passphrase)
        self.name = 'KuCoin'

    def get_ticker(self, symbol):
        ticker = self.client.get_ticker(symbol)
        return {'bid': float(ticker['buy']), 'ask': float(ticker['sell'])}

    def get_balance(self, currency):
        balances = self.client.get_accounts()
        for balance in balances:
            if balance['currency'] == currency:
                return float(balance['available'])
        return 0.0

    def create_order(self, symbol, side, quantity, price):
        response = self.client.create_limit_order(symbol, side, price, quantity)
        return response['orderId']

    def cancel_order(self, symbol, order_id):
        response = self.client.cancel_order(order_id, symbol=symbol)
        return response['cancelledOrderIds']

    def get_order_status(self, symbol, order_id):
        order_info = self.client.get_order(order_id, symbol=symbol)
        if order_info is None:
            return 'NOT FOUND'
        status = order_info['status']
        if status == 'NEW':
            return 'OPEN'
        elif status == 'PARTIALLY_FILLED':
            return 'PARTIAL'
        elif status == 'FILLED':
            return 'FILLED'
        elif status == 'CANCELED':
            return 'CANCELLED'
        else:
            return 'UNKNOWN'

This class defines the necessary methods for interacting with the KuCoin exchange's API using the python-kucoin library. The __init__ method initializes the KuCoin client with the API key, secret, and passphrase provided by the user.

The get_ticker method retrieves the bid and ask prices for the specified trading pair. The get_balance method retrieves the available balance for the specified currency.

The create_order method creates a limit order with the specified parameters. The cancel_order method cancels an existing order with the specified ID. The get_order_status method retrieves the status of an existing order with the specified ID.

Note that this is just an example and you should refer to the KuCoin API documentation and use the library that you prefer.