from pandas import DataFrame


class Broker:
    def __init__(self):
        self.name = 'alpaca'
        self.commission = .002
        self.cash = 10000
        self.prices = DataFrame
