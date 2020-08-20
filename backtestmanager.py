from backtesting import Backtest, Strategy


def run_backtest(strategy):
    strategy = __import__(strategy, globals(), locals())

    class BacktestStrategy(Strategy):
        def __init__(self):
            self.prices = strategy.broker.prices

        def next(self):
            strategy.iterate(self, strategy.data)


    bt = Backtest(strategy.broker.prices,
            BacktestStrategy,
            cash=strategy.broker.cash,
            commission=strategy.broker.commission)

    bt.run()
    bt.plot()
    print(f'{strategy} backtest performed!')

from smaCross import smaCross
run_backtest('smaCross')

