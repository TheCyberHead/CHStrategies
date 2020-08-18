from strat1 import strat1
import pandas
import yfinance
from backtesting.test import SMA, GOOG


def run_backtest(strategy):
    exec(f'''
from {strategy} import {strategy}
from backtesting import Backtest, Strategy


class backtest_{strategy}(Strategy):
    def init(self):
        self.prices = {strategy}.broker.prices

    def next(self):
        {strategy}.iterate(self, {strategy}.data)

print({strategy}.broker.prices)
bt = Backtest({strategy}.broker.prices,
            backtest_{strategy},
            cash={strategy}.broker.cash,
            commission={strategy}.broker.commission)


bt.run()
bt.plot()

print('{strategy} backtest performed!')
''', globals())

run_backtest('strat1')
