"""Homework 4 self-check.   python check_hw04.py

The important checks here are the self-consistency ones. A backtester with an
off-by-one error still produces a plausible-looking number, and the only way to
catch it is to run a strategy whose answer you already know.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _check import Checker
import numpy as np

c = Checker("Homework 4 self-check", "hw04_starter.py")
m = c.load(__file__)


def _no_lookahead(m):
    """Detect a backtester that hands the strategy the day it is predicting.

    Feed it a strictly increasing price series, so a price doubles as its own
    index. A probe strategy records the newest price it is ever shown. A correct
    backtester never shows the strategy the final price, because that price only
    ever exists as a "tomorrow". A lookahead backtester shows it.
    """
    ladder = [100.0 + i for i in range(400)]
    highest_seen = [float("-inf")]

    def probe(window):
        highest_seen[0] = max(highest_seen[0], float(max(window)))
        return True

    m.backtest(ladder, probe)
    if highest_seen[0] == float("-inf"):
        return False                      # the strategy was never called at all
    return highest_seen[0] < ladder[-1]


rng = np.random.default_rng(11)
prices = list(100 * np.exp(np.cumsum(rng.normal(0.0003, 0.01, 1200))))
index_total = prices[-1] / prices[60] - 1     # buy and hold from the first tradeable day

c.exists("backtest is defined", "backtest")
c.exists("a strategy function is defined", "always_hold")

c.check("always-hold matches buy-and-hold exactly",
        lambda: m.backtest(prices, m.always_hold)["total_return"], index_total, tol=1e-6,
        note="if this is off, you have an off-by-one: the strategy is seeing the day it predicts")
c.check("always-cash returns exactly zero",
        lambda: m.backtest(prices, m.always_cash)["total_return"], 0.0, tol=1e-12,
        note="holding cash every day cannot make or lose anything")

c.assert_true("a random 70% strategy lands between cash and the index",
              lambda: 0.0 <= m.backtest(prices, m.random_hold)["total_return"] <= index_total * 1.4,
              note="being invested most of the time should land most of the way to the index")

c.assert_true("the strategy never sees the day it is predicting",
              lambda: _no_lookahead(m),
              note="a probe strategy was shown the windows your backtester hands out, and one of them "
                   "contained the price it was supposed to be predicting.")

c.assert_true("fraction of days invested is reported and sensible",
              lambda: 0.0 <= m.backtest(prices, m.always_hold).get("fraction_invested", 1.0) <= 1.0,
              note="backtest should return fraction_invested between 0 and 1")

c.assert_true("max drawdown is negative or zero, never positive",
              lambda: m.backtest(prices, m.always_hold).get("max_drawdown", 0.0) <= 0.0,
              note="a drawdown is a fall from a peak, so it cannot be a positive number")


sys.exit(c.report())
