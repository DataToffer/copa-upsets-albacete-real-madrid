import pandas as pd
import numpy as np

# ==============================
# CONFIG
# ==============================
FIRST_SEASON = "1940-41"
LAST_SEASON = "2024-25"
TOTAL_SEASONS = 85  # 1940-41 ... 2024-25 (inclusive)

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv("../data/processed/rm_copa_eliminations_low_tier.csv")

# ==============================
# KPI CALCULATION
# ==============================
numerator = df.shape[0]
denominator = TOTAL_SEASONS

p_upset = numerator / denominator
one_in_n = (1 / p_upset) if p_upset > 0 else np.inf

tier_counts = df["opponent_tier"].value_counts().sort_index()

print("=====================================")
print("ANÁLISIS: Upsets vs Real Madrid (Copa)")
print("=====================================")
print(f"Ventana temporal: {FIRST_SEASON} a {LAST_SEASON}")
print(f"Temporadas consideradas (denominador): {denominator}")
print(f"Upsets (numerador): {numerator}")
print("-------------------------------------")
print(f"p(upset) = {p_upset:.4f} ({p_upset*100:.2f}%)")
print(f"Equivalencia: 1 de cada {one_in_n:.1f} ediciones")
print("-------------------------------------")
print("Distribución por tier:")
for tier, cnt in tier_counts.items():
    tier_label = "Segunda" if tier == 2 else "Inferior (tier 3+)"
    print(f"  Tier {tier} ({tier_label}): {cnt} casos")
print("-------------------------------------")
print("Casos incluidos:")
print(df.sort_values("season").to_string(index=False))
