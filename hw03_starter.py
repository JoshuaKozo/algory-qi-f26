"""Homework 3 starter — Algory QI Education, Fall 2026

Fill in every function marked TODO. Keep the names: the checker looks for them.
Run `python check_hw03.py` as you go.
"""
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


# ---------------------------------------------------------------- Q1
def simulate_dice(trials, seed=0):
    """Pick a 4-sided or 6-sided die at random, roll it, repeat.

    Return the estimated P(picked the 4-sided die | rolled a 1).
    The exact answer is 0.6. Take a seed so your result is reproducible.
    """
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------- Q2
def simulate_coins(trials, seed=0):
    """Flip three fair coins, get paid (heads x tails). Return the mean payout.

    The exact answer is 1.5.
    """
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------- Q5/Q6
def p_down(returns):
    """Fraction of days with a negative return. Count them yourself."""
    # TODO
    raise NotImplementedError


def p_down_given_down(returns):
    """P(tomorrow is down | today was down), counted directly from the series."""
    # TODO
    raise NotImplementedError


def p_down_given_big_drop(returns, threshold=-0.02):
    """P(tomorrow is down | today fell more than the threshold).

    Also report how many days this is based on. Forty observations is a much
    weaker claim than two thousand, and the count is how a reader knows.
    """
    # TODO
    raise NotImplementedError


# ---------------------------------------------------------------- Q7
def expected_present_value(cash_flows, rate, survival_prob):
    """Present value where the company survives EACH year with survival_prob.

    Year 1 is certain. Year 2 arrives with probability survival_prob, year 3
    with survival_prob squared, and so on. This is a yearly hazard rate.

    Note this is deliberately more general than the Session 3 slide, which had a
    single shutdown event after year 1 and came to 16.98. A yearly 50% survival
    is a harsher assumption and gives 15.10. Getting 16.98 here means you applied
    the probability once instead of compounding it.
    """
    # TODO
    raise NotImplementedError


def main():
    print("Q1  P(4-sided | rolled a 1) =", simulate_dice(100_000))
    print("Q2  expected three-coin payout =", simulate_coins(100_000))
    # TODO: Q3 — four trial counts, plot the estimate against trials
    # TODO: Q4 — ten years of SPY, print trading days and mean daily return
    # TODO: Q5, Q6 — the conditional probabilities, each with its count
    print("Q7  EPV =", expected_present_value([10, 10, 10], 0.10, 0.5))


if __name__ == "__main__":
    main()
