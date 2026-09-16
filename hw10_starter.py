"""Homework 10 starter — Algory QI Education, Fall 2026"""
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


def kelly_fraction(p, b):
    """Fraction of wealth to stake on a bet paying b-to-1 with probability p.

    kelly_fraction(0.5, 2.0) -> 0.25
    A negative answer means the bet has negative expectation. Do not take it.
    """
    # TODO
    raise NotImplementedError


def correlation_matrix(return_series):
    """Correlation matrix from a list of return series.

    Ones down the diagonal, symmetric. On RETURNS, never on prices.
    """
    # TODO
    raise NotImplementedError


def portfolio_volatility(return_series, weights):
    """Volatility of the weighted combination.

    Must come out BELOW the weighted average of the individual volatilities
    whenever the assets are less than perfectly correlated. That gap is
    diversification, and it is the only free thing in finance.
    """
    # TODO
    raise NotImplementedError


def portfolio_beta(return_series, weights, market_returns):
    """Beta of the weighted portfolio against the market. Cash has beta zero."""
    # TODO
    raise NotImplementedError


def main():
    # TODO Q1/Q2: six assets, their stats, the correlation heatmap
    # TODO Q3/Q4: 10,000 random portfolios, the frontier, the allocation line
    # TODO Q5/Q6: Kelly, then 40 years at four bet sizes with the 5th percentile
    # TODO Q7: the allocation maximising expected log wealth
    # TODO Q8/Q9: beta-hedge the portfolio and backtest hedged against unhedged
    pass


if __name__ == "__main__":
    main()
