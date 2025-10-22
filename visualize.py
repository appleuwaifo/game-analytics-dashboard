# --- visualize.py ---
import pandas as pd
import matplotlib.pyplot as plt

metrics = pd.read_csv("outputs/daily_metrics.csv", parse_dates=["date"])

# --- DAU trend ---
plt.figure(figsize=(10,5))
plt.plot(metrics["date"], metrics["DAU"], color="royalblue", linewidth=2)
plt.title("Daily Active Users (DAU)")
plt.xlabel("Date"); plt.ylabel("Players")
plt.tight_layout()
plt.savefig("outputs/dau_trend.png", dpi=150)
plt.show()

# --- Revenue trend ---
plt.figure(figsize=(10,5))
plt.plot(metrics["date"], metrics["Revenue"], color="green", linewidth=2)
plt.title("Daily Revenue ($)")
plt.xlabel("Date"); plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("outputs/revenue_trend.png", dpi=150)
plt.show()
