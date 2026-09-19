# importing data, dropping empty rows, then printing desired columns
import yfinance as yf
import matplotlib.pyplot as plt
ticker = "GOOG"
goog_df = yf.download(ticker, start = "2025-09-15" , end = "2026-09-15")
spy_df = yf.download("SPY", start = "2025-09-15" , end = "2026-09-15")

goog_df = goog_df.dropna()
spy_df = spy_df.dropna()

print(ticker)
print("Number of trading days:", len(goog_df))
print("First day:", goog_df.index[0])
print("Last day:", goog_df.index[-1])

print("SPY")
print("Number of trading days:", len(spy_df))
print("First day:", spy_df.index[0])
print("Last day:", spy_df.index[-1])

# step 7 print last close, the return over the year, and the annualised volatility

goog_last_close = goog_df["Close"]["GOOG"].iloc[-1]
goog_first_close = goog_df["Close"]["GOOG"].iloc[0]
goog_year_return = (goog_last_close/goog_first_close) - 1
goog_dailyreturn = goog_df["Close"]["GOOG"].pct_change().dropna()
goog_av = goog_dailyreturn.std() * (252 ** 0.5)

print("GOOG Last Close:", round(goog_last_close, 2))
print("GOOG Year Return:", round(goog_year_return, 2))
print("GOOG Annualized Volatility:", round(goog_av, 2))

spy_last_close = spy_df["Close"]["SPY"].iloc[-1]
spy_first_close = spy_df["Close"]["SPY"].iloc[0]
spy_year_return = (spy_last_close/spy_first_close) - 1
spy_dailyreturn = spy_df["Close"]["SPY"].pct_change().dropna()
spy_av = spy_dailyreturn.std() * (252 ** 0.5)

print("SPY Last Close:", round(spy_last_close, 2))
print("SPY Year Return:", round(spy_year_return, 2))
print("SPY Annualized Volatility:", round(spy_av, 2))

#step 8 rebase and plot

goog_rebased = ((goog_df["Close"]["GOOG"] / goog_first_close) *100)
spy_rebased = ((spy_df["Close"]["SPY"] / spy_first_close) *100)

plt.plot(goog_rebased, label = "GOOG")
plt.plot(spy_rebased, label = "SPY")
plt.xlabel("Date")
plt.ylabel("Rebased Price (100)")
plt.title("GOOG vs. SPY - Rebased Performance")
plt.legend()
plt.show()

# step 9 find biggest daily move
biggest_move_date = goog_dailyreturn.abs().idxmax()
biggest_move_size = goog_dailyreturn[biggest_move_date]

print("Biggest single-day move date:", biggest_move_date)
print("Size of move:", round(biggest_move_size, 4))