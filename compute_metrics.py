# --- compute_metrics.py ---
import pandas as pd

# read our data back in
events = pd.read_csv("data/events.csv", parse_dates=["date"])

# 1️⃣  Daily Active Users (DAU)
dau = events.groupby("date")["user_id"].nunique().rename("DAU")

# 2️⃣  Revenue per day
revenue = events.groupby("date")["spend"].sum().rename("Revenue")

# 3️⃣  ARPDAU (Average Revenue Per Daily Active User)
arpdau = (revenue / dau).rename("ARPDAU")

# combine into one table
metrics = pd.concat([dau, revenue, arpdau], axis=1).fillna(0)
metrics.to_csv("outputs/daily_metrics.csv")
print(metrics.head())
print("✅  Saved outputs/daily_metrics.csv")
