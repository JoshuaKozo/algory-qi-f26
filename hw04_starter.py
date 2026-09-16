"""Homework 4 starter — Algory QI Education, Fall 2026

The backtester is the piece worth getting right. Everything after it in the
semester assumes it works.
"""
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

LOOKBACK = 60


# ---------------------------------------------------------------- Q1
def load_and_split(split_date="2011-09-10"):
    """Download ^SP500TR since 1990 and split into training and test.

    The split date belongs to both sets. Return (training, test) and print the
    length and mean price of each, so you can see the split landed where you think.
    """
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------- Q2, Q4, Q5
def always_hold(window):
    """Always invest. The control case, and the one that proves the backtester."""
    return True


def always_cash(window):
    """Never invest. Must produce exactly 0% return."""
    return False


def random_hold(window, p=0.7, rng=np.random.default_rng(0)):
    """Invest with probability p each day."""
    return bool(rng.random() < p)


def five_day_reversal(window):
    """The rule from class: hold unless the last 5 days were positive."""
    # TODO
    raise NotImplementedError


def my_strategy(window):
    """Your own rule. It sees only `window`, the previous LOOKBACK closes.

    It must never look at anything after that. That is the whole assignment.
    """
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------- Q3
def backtest(prices, strategy, lookback=LOOKBACK):
    """Walk forward one day at a time and apply the strategy's decision.

    On each day, hand the strategy the previous `lookback` closes and nothing
    else. If it says hold, you earn the NEXT day's return; if cash, you earn zero.

    Return a dict with at least:
        total_return, annualised_return, max_drawdown, fraction_invested

    Sanity checks before you trust it:
        always_hold  must match buy-and-hold exactly
        always_cash  must return exactly 0.0
    If either fails you have an off-by-one, and every number after it is fiction.
    """
    # TODO
    raise NotImplementedError


def main():
    train, test = load_and_split()
    for name, strat in [("always hold", always_hold),
                        ("always cash", always_cash),
                        ("random 70%", random_hold),
                        ("5-day reversal", five_day_reversal)]:
        r = backtest(train, strat)
        print(f"{name:<16} total {r['total_return']:+.1%}   annual {r['annualised_return']:+.2%}")
    # TODO: Q6 — print EVERY variant you try, not just the one you keep
    # TODO: Q8 — run my_strategy on the test set. Once.
    # TODO: Q9 — what does your rule say to do today?


if __name__ == "__main__":
    main()
