"""Homework 3 starter — Algory QI Education, Fall 2026

Fill in every function marked TODO. Keep the names: the checker looks for them.
Run `python check_hw03.py` as you go.
"""
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


# ---------------------------------------------------------------- Q1
def simulate_dice(trials, seed=1292008):
    """Pick a 4-sided or 6-sided die at random, roll it, repeat.

    Return the estimated P(picked the 4-sided die | rolled a 1).
    The exact answer is 0.6. Take a seed so your result is reproducible.
    """
    import random

    random.seed(seed)

    ones = 0
    ones_4 = 0

    for i in range(100000):
        die = random.choice([4,6])
        roll = random.randint(1, die)
        if roll == 1:
            ones += 1
            if die == 4:
                ones_4 += 1

    simulated_prob = ones_4 / ones
    exact_prob = 0.6

    difference = simulated_prob - exact_prob

    print(f'Simulated Probability: {simulated_prob}')
    print(f'Exact Probability: {exact_prob}')
    print(f'Difference between sim and expected: {difference}')
    return(simulated_prob)

# ---------------------------------------------------------------- Q2
def simulate_coins(trials, seed=1292008):
    """Flip three fair coins, get paid (heads x tails). Return the mean payout.

    The exact answer is 1.5.
    """


    total_payout = 0
    import random
    random.seed(seed)
    for flips in range (100000):
        heads = 0
        for j in range(3):
            if random.choice(['Heads', 'Tails']) == 'Heads':
                heads += 1
        tails = 3 - heads
        total_payout += heads * tails

    payout_avg = total_payout / 100000
    expected = 1.5
    difference = expected - payout_avg

    print(f'Simulated Probability:, {payout_avg}')
    print(f'Exact Probability: {expected}')
    print(f'Difference between sim and expected: {difference}')

    #code needed for Q3
    import random
    import matplotlib.pyplot as plt

    random.seed(1292008)
    trials_numbers = [100, 1000, 10000, 100000]
    resulting_estimates = []
    for n in trials_numbers:
        total_payout = 0
        for flips in range (n):
                heads = 0
                for j in range(3):
                    if random.choice(['Heads', 'Tails']) == 'Heads':
                        heads += 1
                tails = 3 - heads
                total_payout += heads * tails
        resulting_estimates.append(total_payout / n)
    
    for n, est in zip(trials_numbers, resulting_estimates):
        print(f'{n} trials: {est}')

    plt.plot(trials_numbers, resulting_estimates, marker='o')
    plt.axhline(expected, linestyle='--')
    plt.xscale('log')
    plt.xlabel('Number of trials')
    plt.ylabel('Estimated expected payout')
    plt.show()


    return(payout_avg)


# ---------------------------------------------------------------- Q5/Q6
def p_down(returns):
    """Fraction of days with a negative return. Count them yourself."""

    import yfinance
    
    spy = yfinance.download("SPY", period = "10y")
    closes = spy["Close"]["SPY"]
    returns = closes.pct_change().dropna()
    print("Number of trading days:", len(returns))
    print("Mean daily return:", returns.mean())
    
    down_days = returns[returns < 0 ]

    print(f'Number of down days = {len(down_days)}')
    print(f'Total number of days = {len(returns)}')

    return(len(down_days) / len(returns))



def p_down_given_down(returns):
    """P(tomorrow is down | today was down), counted directly from the series."""
    returns = list(returns)
    today_down = 0
    both_down = 0
    for i in range(len(returns) - 1):
        if returns[i] < 0:
            today_down += 1
            if returns[i + 1] < 0:
                both_down += 1
    print(f'down given down is when a single down day {today_down}, is followed by another {both_down}')
    return(both_down / today_down)
    


def p_down_given_big_drop(returns, threshold=-0.02):
    """P(tomorrow is down | today fell more than the threshold).

    Also report how many days this is based on. Forty observations is a much
    weaker claim than two thousand, and the count is how a reader knows.
    """
    returns = list(returns)
    big_drops = 0
    next_day_down = 0
    for i in range(len(returns) - 1):
        if returns[i] < threshold:
            big_drops += 1
            if returns[i + 1] < 0:
                next_day_down += 1
    print(f'P(tomorrow is down | today fell more than the threshold) is the number of down days {next_day_down} that fllowed a big drop {big_drops}')
    return(next_day_down / big_drops)


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
    epv = 0
    for i in range(len(cash_flows)):
        year = i + 1
        alive_chance = survival_prob ** (year - 1)
        present_value = cash_flows[i] / (1 + rate) ** year
        epv += alive_chance * present_value
    print(epv)
    return epv


def main():
    print("Q1  P(4-sided | rolled a 1) =", simulate_dice(100_000))
    print("Q2  expected three-coin payout =", simulate_coins(100_000))
    # TODO: Q3 — four trial counts, plot the estimate against trials
    # Q4
    spy = yf.download("SPY", period="10y", auto_adjust=True)
    closes = spy["Close"]["SPY"]
    returns = closes.pct_change().dropna()
    print("Q4  Number of trading days:", len(returns))
    print("Q4  Mean daily return:", returns.mean())
    # Q5, Q6
    print("Q5  P(down) =", p_down(returns))
    print("Q5  P(down | down) =", p_down_given_down(returns))
    print("Q6  P(down | drop > 2%) =", p_down_given_big_drop(returns))
    print("Q7  EPV =", expected_present_value([10, 10, 10], 0.10, 0.5))


if __name__ == "__main__":
    main()
