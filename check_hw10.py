"""Homework 10 self-check.   python check_hw10.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _check import Checker
import numpy as np

c = Checker("Homework 10 self-check", "hw10_starter.py")
m = c.load(__file__)


def _rets():
    a = rng.normal(0.0004, 0.012, 800)
    b = rng.normal(0.0003, 0.010, 800)
    d = rng.normal(0.0002, 0.008, 800)
    return [list(a), list(b), list(d)]

def _corr_diag(m):
    C = np.asarray(m.correlation_matrix(_rets()))
    return bool(np.allclose(np.diag(C), 1.0, atol=1e-9))

def _corr_sym(m):
    C = np.asarray(m.correlation_matrix(_rets()))
    return bool(np.allclose(C, C.T, atol=1e-9))

def _diversifies(m):
    rs = _rets()
    w = [1 / 3, 1 / 3, 1 / 3]
    port = m.portfolio_volatility(rs, w)
    weighted_avg = sum(wi * float(np.std(r, ddof=1)) for wi, r in zip(w, rs))
    return port < weighted_avg


rng = np.random.default_rng(10)

c.check("Kelly for the coin from class",
        lambda: m.kelly_fraction(0.5, 2.0), 0.25, tol=1e-6,
        note="50% chance of tripling the stake")
c.check("Kelly for a two-thirds chance at even money",
        lambda: m.kelly_fraction(2 / 3, 1.0), 1 / 3, tol=1e-6, note="(p*b - q)/b")
c.assert_true("Kelly is zero or negative on a losing bet",
              lambda: m.kelly_fraction(0.25, 1.0) <= 0,
              note="a negative-expectation bet should not be taken at any size")
c.assert_true("Kelly never tells you to bet more than everything",
              lambda: all(m.kelly_fraction(p, b) <= 1.0 + 1e-9
                          for p in (0.5, 0.7, 0.9) for b in (1.0, 2.0, 5.0)),
              note="a fraction above 1 would mean borrowing, which Kelly does not assume")

mkt = rng.normal(0.0004, 0.010, 900)
stock = 1.6 * mkt + rng.normal(0, 0.004, 900)

c.check("portfolio beta of a 1.6-beta holding",
        lambda: m.portfolio_beta([list(stock)], [1.0], list(mkt)), 1.6, tol=0.06,
        note="one holding, so the portfolio beta is that holding's beta")
c.check("half in a 1.6-beta stock and half in cash",
        lambda: m.portfolio_beta([list(stock), [0.0] * 900], [0.5, 0.5], list(mkt)), 0.8, tol=0.06,
        note="cash has a beta of zero, so it scales the whole thing down")

c.assert_true("a correlation matrix has ones down the diagonal",
              lambda: _corr_diag(m), note="every asset is perfectly correlated with itself")
c.assert_true("a correlation matrix is symmetric",
              lambda: _corr_sym(m), note="correlation of A with B equals B with A")
c.assert_true("diversification lowers volatility below the weighted average",
              lambda: _diversifies(m),
              note="this is the whole point of holding more than one thing")


sys.exit(c.report())
