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
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cash_flows, start=1))


# ---------------------------------------------------------------- Q2
def bond_price(face, coupon_rate, years, market_rate):
    """Price of a bond paying an annual coupon and repaying face at maturity.

    The final year pays the coupon AND the face value. That is the usual bug.
    bond_price(1000, 0.04, 10, 0.04) -> exactly 1000.0
    """
    coupon = face * coupon_rate
    cash_flows = [coupon] * years
    cash_flows[-1] = cash_flows[-1] + face
    return present_value(cash_flows, market_rate)


# ---------------------------------------------------------------- Q4/Q5
def annualised_return(prices):
    """Annualised return from a price series, using 252 trading days."""
    returns = prices.pct_change().dropna()
    return returns.mean() * 252


def annualised_volatility(prices):
    """Annualised standard deviation of daily returns."""
    returns = prices.pct_change().dropna()
    return returns.std() * np.sqrt(252)


def beta(stock_prices, market_prices):
    """Beta of a stock against the market.

    Covariance of the two RETURN series divided by the variance of the market's.
    Computing this on prices instead of returns is a common and silent error.
    beta(spy, spy) -> 1.0
    """
    stock_returns = stock_prices.pct_change().dropna()
    market_returns = market_prices.pct_change().dropna()
    return stock_returns.cov(market_returns) / market_returns.var()
def annualised_return(prices):
    """Annualised return from a price series, using 252 trading days."""
    returns = prices.pct_change().dropna()
    return returns.mean() * 252


def annualised_volatility(prices):
    """Annualised standard deviation of daily returns."""
    returns = prices.pct_change().dropna()
    return returns.std() * np.sqrt(252)


def beta(stock_prices, market_prices):
    """Beta of a stock against the market.

    Covariance of the two RETURN series divided by the variance of the market's.
    Computing this on prices instead of returns is a common and silent error.
    beta(spy, spy) -> 1.0
    """
    stock_returns = stock_prices.pct_change().dropna()
    market_returns = market_prices.pct_change().dropna()
    return stock_returns.cov(market_returns) / market_returns.var()


# ---------------------------------------------------------------- your answers
def main():
    """Everything the assignment asks you to print goes here."""
    print("Q1  present_value([10, 15, 20], 0.10) =", present_value([10, 15, 20], 0.10))

    print("Q2  bond_price(1000, 0.04, 10, 0.04) =", round(bond_price(1000, 0.04, 10, 0.04), 2))
    print("    bond_price(1000, 0.04, 10, 0.02) =", round(bond_price(1000, 0.04, 10, 0.02), 2))

    market_rate_scenarios = {"2%": 0.02, "4%": 0.04, "10yr Treasury (4.96%)": 0.0496}
    print("\nQ3  10-year, 4% coupon bond prices:")
    for label, r in market_rate_scenarios.items():
        print(f"    market rate {label}: {round(bond_price(1000, 0.04, 10, r), 2)}")

    market_rates = np.linspace(0.0001, 0.10, 200)
    prices = [bond_price(1000, 0.04, 10, r) for r in market_rates]

    plt.figure(figsize=(7, 5))
    plt.plot(market_rates * 100, prices)
    plt.xlabel("Market rate (%)")
    plt.ylabel("Bond price ($)")
    plt.title("10-Year, 4% Coupon Bond: Price vs Market Rate")
    plt.axhline(1000, color="gray", linestyle="--", linewidth=0.8)
    plt.axvline(4, color="gray", linestyle="--", linewidth=0.8)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("bond_price_vs_rate.png", dpi=150)
    plt.show()
    print("\n    Plot saved to bond_price_vs_rate.png")

    tickers = ["GOOG", "JPM", "COST"]   # swap in your three
    benchmark = "SPY"
    all_tickers = tickers + [benchmark]
    data = yf.download(all_tickers, period="5y", auto_adjust=True, progress=False)["Close"]

    print("\nQ4  trading days:")
    for t in all_tickers:
        print(f"    {t}: {data[t].dropna().shape[0]}")

    rows = []
    for t in all_tickers:
        rows.append([
            t,
            round(annualised_return(data[t]), 4),
            round(annualised_volatility(data[t]), 4),
            round(beta(data[t], data[benchmark]), 2),
        ])
    table = pd.DataFrame(rows, columns=["Ticker", "Ann. Return", "Ann. Volatility", "Beta"])
    print("\nQ5  return / volatility / beta table:")
    print(table.to_string(index=False))

    print("\nQ6  ranked by beta:")
    print(table.sort_values("Beta", ascending=False)[["Ticker", "Beta"]].to_string(index=False))
    print("\nQ6  ranked by volatility:")
    print(table.sort_values("Ann. Volatility", ascending=False)[["Ticker", "Ann. Volatility"]].to_string(index=False))


if __name__ == "__main__":
    main()