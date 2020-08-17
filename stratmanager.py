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


def get_df_name(df):
    '''get the name of a DataFrame object'''
    name =[x for x in globals() if globals()[x] is df][0]
    return name


def run_live(strategy):
    exec(f'''
from cyberhead.strategies.{strategy} import {strategy}
from cyberhead.brokers.broker import Broker


iterate = {strategy}.iterate
broker = {strategy}.broker
data = {strategy}.data

symbol = get_df_name(broker.prices)
broker.symbol = symbol


new_data = yfinance.download('GOOG', interval = '1d')
past_data = pandas.read_csv('GOOG.csv')
stored_record = past_data.iloc[-1][0]
new_record = str(new_data.index.values[-1])[:10]

if stored_record != new_record:
    new_data.to_csv('GOOG.csv')
    print('New record!')
    iterate(broker, data)
else:
    print('There is no new record!')

print('There is no new record!')


''')




if {strategy}.broker.prices.has_new_data():
    iterate(broker, data)
        #run_backtest(strategy)
        run_live(strategy)
