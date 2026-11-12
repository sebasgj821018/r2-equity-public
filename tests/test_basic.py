import numpy as np
from equity_football_risk import gini, theil_t, tvar, solidarity_transfers

def test_gini_equal():
    assert abs(gini(np.ones(10))) < 1e-12

def test_theil_equal():
    assert abs(theil_t(np.ones(10))) < 1e-12

def test_tvar_ge_mean():
    L = np.random.RandomState(0).exponential(10, 500)
    assert tvar(L, 0.95) >= L.mean()

def test_transfers_sum_zero():
    P = np.array([10.0, 20.0, 30.0])
    assert abs(solidarity_transfers(P).sum()) < 1e-12
