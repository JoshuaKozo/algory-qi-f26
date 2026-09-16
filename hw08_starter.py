"""Homework 8 starter — Algory QI Education, Fall 2026"""
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


def n_day_returns(prices, n):
    """Every overlapping n-day return in the series.

    A series of length L gives about L - n windows.
    With n = 1 this is just the daily return series.
    """
    # TODO
    raise NotImplementedError


def price_from_history(prices, spot, strike, days, kind):
    """Price an option from what the underlying has actually done.

    Apply every historical `days`-day return to `spot` to build a distribution of
    final prices, compute the payoff under each, and return the mean. No
    distributional assumption anywhere.

    Sanity checks: a strike far below spot prices near intrinsic; a strike far
    above prices near zero; nothing is ever negative.
    """
    # TODO
    raise NotImplementedError


def main():
    # TODO Q1: the 21-day return distribution, with its percentiles
    # TODO Q2: histogram against a fitted normal, plus skew and excess kurtosis
    # TODO Q3: price a 21-day call struck 3% above spot, and the matching put
    # TODO Q4: the distribution of final prices, with the paying region shaded
    # TODO Q5/Q6: Black-Scholes on the same contracts, and the difference by strike
    pass


if __name__ == "__main__":
    main()
