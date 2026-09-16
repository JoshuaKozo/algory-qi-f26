"""Homework 3 self-check.   python check_hw03.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _check import Checker

c = Checker("Homework 3 self-check", "hw03_starter.py")
m = c.load(__file__)

_EPV_HALF = sum((0.5 ** i) * 10 / 1.1 ** (i + 1) for i in range(3))

c.check("expected_present_value with 50% survival each year",
        lambda: m.expected_present_value([10, 10, 10], 0.10, 0.5), _EPV_HALF, tol=0.02,
        note="year 1 certain, year 2 at 0.5, year 3 at 0.25. This is NOT the 16.98 from "
             "the Session 3 slide, which modelled a single shutdown event rather than a "
             "yearly one. Read the docstring.")
c.check("expected_present_value with certain survival",
        lambda: m.expected_present_value([10, 15, 20], 0.10, 1.0), 36.51, tol=0.02,
        note="survival of 1.0 must reduce to plain present value")
c.check("expected_present_value with no survival past year 1",
        lambda: m.expected_present_value([10, 10, 10], 0.10, 0.0), 10 / 1.1, tol=0.02,
        note="only the first year is ever collected")

c.check("simulated P(4-sided | rolled a 1)",
        lambda: m.simulate_dice(200_000), 0.6, tol=0.02,
        note="exact answer is 3/5. If you are far off, check which die you recorded.")
c.check("simulated three-coin expected payout",
        lambda: m.simulate_coins(200_000), 1.5, tol=0.02,
        note="pays heads x tails, so 0, 2, 2, 0 across the four cases")

c.assert_true("simulate_dice is reproducible with a fixed seed",
              lambda: abs(m.simulate_dice(50_000, seed=1) - m.simulate_dice(50_000, seed=1)) < 1e-12,
              note="the same seed must give the same answer twice, or your results are not reproducible")
c.assert_true("more trials gives a closer estimate",
              lambda: abs(m.simulate_coins(400_000, seed=3) - 1.5)
                      <= abs(m.simulate_coins(400, seed=3) - 1.5) + 0.05,
              note="this is the law of large numbers, and it is the point of question 3")

sys.exit(c.report())
