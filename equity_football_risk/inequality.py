"""Metricas de desigualdad de carga logistica."""
import numpy as np

def gini(x):
    """Coeficiente de Gini de un array x >= 0. 0 = igualdad perfecta."""
    x = np.sort(np.asarray(x, dtype=float))
    if np.any(x < 0):
        raise ValueError("gini requiere valores no negativos")
    n = len(x)
    idx = np.arange(1, n + 1)
    return float((2 * np.sum(idx * x) - (n + 1) * np.sum(x)) / (n * np.sum(x)))

def theil_t(x):
    """Indice de Theil T de un array x > 0."""
    x = np.asarray(x, dtype=float)
    if np.any(x <= 0):
        raise ValueError("theil_t requiere valores positivos")
    mu = x.mean()
    return float(np.mean((x / mu) * np.log(x / mu)))
