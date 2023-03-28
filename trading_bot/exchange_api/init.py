import requests


class ExchangeAPI:
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def get_price(self, symbol):
        url = f"https://api.example.com/price?symbol={symbol}"
        headers = {"X-MBX-APIKEY": self.api_key}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return float(data["price"])



import ccxt


class Exchange:
    def __init__(self, exchange_id, api_key, secret_key):
        self.exchange_id = exchange_id
        self.api_key = api_key
        self.secret_key = secret_key
        self.exchange = self.get_exchange()

    def get_exchange(self):
        exchange_class = getattr(ccxt, self.exchange_id)
        exchange = exchange_class({
            'apiKey': self.api_key,
            'secret': self.secret_key,
        })
        return exchange

    def get_balance(self, symbol):
        balance = self.exchange.fetch_balance()[symbol]
        return balance

    def create_order(self, symbol, order_type, side, amount, price=None):
        order = None
        try:
            if order_type == 'market':
                order = self.exchange.create_order(symbol=symbol, type=order_type, side=side, amount=amount)
            elif order_type == 'limit':
                order = self.exchange.create_order(symbol=symbol, type=order_type, side=side, amount=amount, price=price)
        except Exception as e:
            print(f'Error creating order: {e}')
        return order

    def cancel_order(self, order_id):
        result = None
        try:
            result = self.exchange.cancel_order(order_id)
        except Exception as e:
            print(f'Error cancelling order: {e}')
        return result

    def get_order(self, order_id):
        order = None
        try:
            order = self.exchange.fetch_order(order_id)
        except Exception as e:
            print(f'Error getting order: {e}')
        return order

    def get_open_orders(self, symbol=None):
        orders = []
        try:
            orders = self.exchange.fetch_open_orders(symbol=symbol)
        except Exception as e:
            print(f'Error getting open orders: {e}')
        return orders
