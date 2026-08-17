"""Generate simple synthetic user profiles using statistical distributions.

This is intentionally simple: it demonstrates marginal distributions first.
It does not attempt to reproduce a real population.
"""
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 42
N = 1000
rng = np.random.default_rng(SEED)

# Statistical generation: different variables are sampled from simple distributions.
age = np.clip(np.rint(rng.normal(loc=42, scale=13, size=N)), 18, 75).astype(int)
income = np.round(rng.lognormal(mean=np.log(55000), sigma=0.45, size=N), 2)
credit_score = np.clip(np.rint(rng.normal(690, 55, N)), 300, 850).astype(int)
country = rng.choice(["USA", "Canada"], size=N, p=[0.75, 0.25])

# These values are intentionally generated independently so students can discuss
# the limitation: marginal distributions can look reasonable while relationships
# between variables may be unrealistic.
df = pd.DataFrame({
    "Age": age,
    "Income": income,
    "Credit_Score": credit_score,
    "Country": country,
})

out = Path(__file__).resolve().parent / "statistical_profiles.csv"
df.to_csv(out, index=False)
print(f"Generated {len(df)} profiles: {out}")
print("\nSummary statistics:")
print(df.describe(include="all"))
print("\nFirst 5 rows:")
print(df.head().to_string(index=False))
