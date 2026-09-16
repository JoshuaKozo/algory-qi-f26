"""Homework 2 starter — Algory QI Education, Fall 2026

Fill in every function marked TODO. Do not rename them: the checker looks for
these exact names. Run `python check_hw02.py` before you submit.
"""
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------------- Q1
def present_value(cash_flows, rate):
    """Present value of a list of cash flows, the first arriving in one year.

    present_value([10, 15, 20], 0.10) -> 36.51
    """
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------- Q2
def bond_price(face, coupon_rate, years, market_rate):
    """Price of a bond paying an annual coupon and repaying face at maturity.

    The final year pays the coupon AND the face value. That is the usual bug.
    bond_price(1000, 0.04, 10, 0.04) -> exactly 1000.0
    """
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------- Q4/Q5
def annualised_return(prices):
    """Annualised return from a price series, using 252 trading days."""
    # TODO
    raise NotImplementedError


def annualised_volatility(prices):
    """Annualised standard deviation of daily returns."""
    # TODO
    raise NotImplementedError


def beta(stock_prices, market_prices):
    """Beta of a stock against the market.

    Covariance of the two RETURN series divided by the variance of the market's.
    Computing this on prices instead of returns is a common and silent error.
    beta(spy, spy) -> 1.0
    """
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------- your answers
def main():
    """Everything the assignment asks you to print goes here."""
    print("Q1  present_value([10, 15, 20], 0.10) =", present_value([10, 15, 20], 0.10))
    # TODO: Q3 — three bond prices, then the price-vs-rate plot
    # TODO: Q4 — download your three tickers and SPY, print trading days for each
    # TODO: Q5 — the table of return, volatility and beta
    # TODO: Q6 — both rankings


if __name__ == "__main__":
    main()
