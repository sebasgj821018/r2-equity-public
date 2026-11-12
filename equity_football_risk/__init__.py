"""equity-football-risk: inequidad logistica como riesgo cuantificable y transferible.

Toolkit open-source con datos sinteticos. Contraparte publica de una investigacion
en curso (WCSF 2027); aqui no se distribuyen datos reales ni resultados.
"""
from .inequality import gini, theil_t
from .actuarial import pure_premium, tvar, solidarity_transfers
from .covar_log import delta_covar_empirico

__version__ = "0.1.0"
