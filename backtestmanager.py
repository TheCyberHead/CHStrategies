import pandas
import yfinance
from backtesting.test import SMA, GOOG


def run_backtest(strategy):
    exec(f'''
from cyberhead.strategies.{strategy} import {strategy}
from backtesting import Backtest, Strategy


class backtest_{strategy}(Strategy):
    def init(self):
        self.prices = {strategy}.broker.prices

    def next(self):
        {strategy}.iterate(self, {strategy}.data)


bt = Backtest({strategy}.broker.prices,
            backtest_{strategy},
            cash={strategy}.broker.cash,
            commission={strategy}.broker.commission)


bt.run()
bt.plot()

print('{strategy} backtest performed!')
''', globals())

