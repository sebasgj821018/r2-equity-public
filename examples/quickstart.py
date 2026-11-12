"""Quickstart: equity-football-risk sobre datos sinteticos."""
from pathlib import Path
import pandas as pd
from equity_football_risk import gini, pure_premium, tvar, solidarity_transfers

csv = Path(__file__).resolve().parents[1] / "data_synthetic" / "club_season_load_synthetic.csv"
df = pd.read_csv(csv)
load = df.groupby("club")["load_E"].mean().sort_values(ascending=False)
print("Gini de carga media:", round(gini(load.values), 3))
P = 0.05 * load  # coeficiente de perdida sintetico
print("Top-5 primas puras:"); print(P.head(5).round(2))
print("TVaR 95%:", round(tvar(P.values), 2))
T = solidarity_transfers(P.values)
print("Top-5 receptores netos:", dict(zip(load.index[:5], T[:5].round(2))))
