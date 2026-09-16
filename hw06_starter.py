"""Homework 6 starter — Algory QI Education, Fall 2026"""
from math import log, sqrt, exp, erf
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


def black_scholes(kind, spot, strike, years, rate, vol):
    """European option price.

    Time in YEARS. Rate and vol as decimals, not percentages. That is the usual bug.
    black_scholes("call", 100, 100, 1, 0.04, 0.25) -> 11.84
    black_scholes("put",  100, 100, 1, 0.04, 0.25) ->  7.92
    """
    # TODO
    raise NotImplementedError


def implied_volatility(price, spot, strike, years, rate, kind):
    """Solve for the volatility that makes black_scholes match `price`.

    Bisection between about 0.0001 and 5.0 is plenty and is easier to debug than
    Newton's method. Price rises with volatility, which is what makes it work.
    Feeding your own price back in must return the volatility you started with.
    """
    # TODO
    raise NotImplementedError


def covered_call(entry, strike, premium, spot):
    """Long 100 shares bought at `entry`, short one call struck at `strike`.

    Returns profit per share at expiry. Above the strike this must stop rising.
    """
    # TODO
    raise NotImplementedError


def main():
    # TODO Q1: the four combinations, with max profit, max loss and break-evens
    # TODO Q2: why a calendar spread has no single expiry diagram
    # TODO Q5: implied vol across a live chain, plotted against strike
    # TODO Q6: 30-day realised volatility, next to at-the-money implied
    pass


if __name__ == "__main__":
    main()
