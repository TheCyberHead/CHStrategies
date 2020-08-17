from os import system
from cyberhead.strategies.stratmanager import run_strategies
from cyberhead.logger import Logger

log = Logger('strategies').log

def start():
    log('starting...')
    strategies = ['strat1', 'strat2']
    run_strategies(strategies)
    return 'Strategies initilized!', 15
