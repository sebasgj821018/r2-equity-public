"""Quickstart: equity-football-risk sobre datos sinteticos.

Funciona sin instalar el paquete (bootstrap de sys.path) o tras `pip install -e .`.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pandas as pd
from equity_football_risk import gini, pure_premium, tvar, solidarity_transfers

csv = ROOT / "data_synthetic" / "club_season_load_synthetic.csv"
df = pd.read_csv(csv)
load = df.groupby("club")["load_E"].mean().sort_values(ascending=False)
print("Gini de carga media:", round(gini(load.values), 3))
P = 0.05 * load  # coeficiente de perdida sintetico
print("Top-5 primas puras:"); print(P.head(5).round(2))
print("TVaR 95%:", round(tvar(P.values), 2))
T = solidarity_transfers(P.values)
print("Top-5 receptores netos:", dict(zip(load.index[:5], T[:5].round(2))))
