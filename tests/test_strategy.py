# tests/test_strategy.py
import pandas as pd

def test_signals_length(strategy, prices):
    sig = strategy.signals(prices)
    assert len(sig) == len(prices)

def test_empty_series(strategy):
    s = pd.Series(dtype=float)
    sig = strategy.signals(s)
    assert sig.empty

def test_constant_series(strategy):
    const = pd.Series([100.0] * 50)
    sig = strategy.signals(const)
    assert sig.sum() == 0

def test_nans_at_head(strategy):
    s = pd.Series([float('nan')] + list(range(1, 30)))
    sig = strategy.signals(s)
    assert len(sig) == len(s)
