"""Capa actuarial: prima pura, riesgo de cola y transferencias solidarias."""
import numpy as np

def pure_premium(L):
    """Prima pura = perdida esperada E[L]."""
    return float(np.mean(L))

def tvar(L, q=0.95):
    """Tail Value at Risk (Expected Shortfall) al nivel q."""
    L = np.asarray(L, dtype=float)
    return float(L[L >= np.quantile(L, q)].mean())

def solidarity_transfers(P):
    """Transferencia neta recibida bajo prima comunitaria: T_i = P_i - mean(P).
    Positivo = receptor neto (club sobrecargado logisticamente)."""
    P = np.asarray(P, dtype=float)
    return P - P.mean()
