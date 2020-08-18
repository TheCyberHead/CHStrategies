from cyberhead.brokers.broker import Broker
from pandas import DataFrame

from backtesting.lib import crossover
from backtesting.test import GOOG


broker = Broker('alpaca')
data = DataFrame

broker.commission = .002
broker.cash = 10000
broker.prices = GOOG

def iterate(broker, data):
    '''please note that broker, data and iterate are not related here,
    this objects are called by the stratmanager'''

    data.sma_10 = list(broker.prices.Close.rolling(10).mean())
    data.sma_20 = list(broker.prices.Close.rolling(20).mean())
?!?jedi=0, ?!?         (*_**values: object*_*, sep: Optional[Text]=..., end: Optional[Text]=..., file: Optional[_Writer]=..., flush: bool=...) ?!?jedi?!?
    if crossover(data.sma_10, data.sma_20):
        broker.buy()
    elif crossover(data.sma_20, data.sma_10):
        broker.sell()
