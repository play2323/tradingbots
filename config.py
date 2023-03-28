from decimal import Decimal

TRADING_PAIRS = ['BTC/USDT', 'ETH/USDT']

EXCHANGE = 'binance' 'bitfinex' 'houbi' 'kraken'

TRADE_AMOUNT = Decimal('100')
PROFIT_TARGET = Decimal('0.01')
STOP_LOSS = Decimal('0.02')

ARBITRAGE_INTERVAL = 60  # seconds
ORDER_BOOK_DEPTH = 5

SLACK_NOTIFICATIONS = True
