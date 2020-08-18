from pandas import DataFrame

from backtesting.lib import crossover
from backtesting.test import GOOG


data = DataFrame

class Broker:
    def __init__(self):
        self.commission = .002
        self.cash = 10000
        self.prices = GOOG

broker = Broker()

def iterate(broker, data):
    '''please note that broker, data and iterate are not related here,
    this objects are called by the stratmanager'''

    data.sma_10 = list(broker.prices.Close.rolling(10).mean())
    data.sma_20 = list(broker.prices.Close.rolling(20).mean())

    if crossover(data.sma_10, data.sma_20):
        broker.buy()
    elif crossover(data.sma_20, data.sma_10):
        broker.sell()
