"""Homework 5 starter — Algory QI Education, Fall 2026

Keep these function names: check_hw05.py looks for them.
"""
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


def intrinsic(kind, strike, spot):
    """What the option is worth if exercised right now. Never negative.

    kind is "call" or "put".
    intrinsic("call", 45, 48) -> 3.0        intrinsic("call", 55, 48) -> 0.0
    """
    # TODO
    raise NotImplementedError


def extrinsic(kind, strike, spot, premium):
    """What you are paying for time and uncertainty: premium minus intrinsic."""
    # TODO
    raise NotImplementedError


def payoff(kind, strike, premium, spot):
    """Profit per share at expiry.

    kind is one of: long_call, long_put, short_call, short_put.
    Check the signs before going further:
        payoff("long_call", 100, 6, 80)   -> -6.0
        payoff("short_call", 100, 6, 120) -> -14.0
    """
    # TODO
    raise NotImplementedError


def main():
    # TODO Q1: print all four payoffs at spot 80, 100, 120
    # TODO Q2: the 2x2 grid of payoff diagrams
    # TODO Q3: pull a live chain, print ticker, expiry, spot, counts
    # TODO Q4: mid price, intrinsic and extrinsic for the ten strikes nearest spot
    # TODO Q5: extrinsic against strike, with spot marked
    # TODO Q6: the same for a six-month expiry, both curves on one axis
    pass


if __name__ == "__main__":
    main()
