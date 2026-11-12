"""Riesgo sistemico (CoVaR empirico): version demo con datos sinteticos.
La implementacion completa por quantile regression vive en el repo privado."""
import numpy as np

def delta_covar_empirico(X, E, q=0.95):
    """delta-CoVaR empirico: cuantil q de X bajo distress de E (E >= VaR_q(E))
    menos cuantil q de X en estado mediano de E."""
    X = np.asarray(X, float); E = np.asarray(E, float)
    distress = E >= np.quantile(E, q)
    mediano = (E >= np.quantile(E, 0.45)) & (E <= np.quantile(E, 0.55))
    return float(np.quantile(X[distress], q) - np.quantile(X[mediano], q))
