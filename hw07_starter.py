"""Homework 7 starter — Algory QI Education, Fall 2026

The check that matters here is that your features never read the future. The
checker builds your features twice, changing only data after row 400, and
confirms the earlier rows did not move.
"""
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor


def build_features(prices, lookbacks=(1, 5, 20, 60)):
    """One row per trading day: features first, label last.

    Every feature must use only prices up to and including that day. The label is
    the NEXT day's return, and it is the only forward-looking value allowed.

    Return a list of rows, each [f1, f2, ..., fn, label].
    """
    # TODO
    raise NotImplementedError


def split_by_time(rows, train=0.6, val=0.2):
    """Split in time order into (training, validation, test). Never shuffle.

    Shuffling lets 2024 train the model that predicts 2016. It produces
    spectacular, meaningless results and it is the most common mistake in the field.
    """
    # TODO
    raise NotImplementedError


def up_day_baseline(prices):
    """Share of days with a positive return: the number any classifier must beat.

    It is nearer 54% than 50%, which is why raw accuracy is a weak measure here.
    """
    # TODO
    raise NotImplementedError


def main():
    # TODO Q1: build the table, print its shape, columns and first three rows
    # TODO Q2: split, print the date range and row count of each set
    # TODO Q3: four models, training and validation R-squared for each
    # TODO Q4: tune one hyperparameter each, plot the tuning curve
    # TODO Q5: best model, once, on the test set
    # TODO Q6: convert to a trading rule and backtest it
    # TODO Q7: rank the features the model leaned on
    pass


if __name__ == "__main__":
    main()
