"""Homework 9 starter — Algory QI Education, Fall 2026"""
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


def recovery_needed(loss_fraction):
    """Gain required to get back to even after a loss.

    recovery_needed(0.50) -> 1.00     lose half, need to double
    recovery_needed(0.75) -> 3.00     lose three quarters, need +300%
    """
    # TODO
    raise NotImplementedError


def annualise_vol(daily_vol, days=252):
    """Scale a daily standard deviation to annual. Assumes days are independent."""
    # TODO
    raise NotImplementedError


def var(returns, confidence=0.95):
    """Value at risk, as a return. A left-tail quantile, so it comes out negative."""
    # TODO
    raise NotImplementedError


def cvar(returns, confidence=0.95):
    """Mean of everything at or beyond the VaR threshold.

    Must always be worse than var() on the same inputs. If it is not, you have
    averaged the wrong side of the distribution.
    """
    # TODO
    raise NotImplementedError


def simulate_paths(start, drift, vol, days=252, paths=1000, seed=0):
    """Geometric Brownian motion. Return the FINAL value of each path."""
    # TODO
    raise NotImplementedError


def main():
    # TODO Q1/Q2: scaled vs directly measured annual volatility, and the gap
    # TODO Q3: rolling 60-day volatility, with the two largest spikes named
    # TODO Q4/Q5: the return histogram, and four-sigma days expected vs actual
    # TODO Q6: the loss-and-recovery table
    # TODO Q7/Q8/Q9: Monte Carlo, then VaR and CVaR both ways
    pass


if __name__ == "__main__":
    main()
