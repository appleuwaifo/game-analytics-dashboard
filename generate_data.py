# --- generate_data.py ---
import numpy as np
import pandas as pd

# fix randomness so results stay the same each time
rng = np.random.default_rng(42)

# 1. basic configuration
N_USERS = 3000                              # number of fake players
DAYS = pd.date_range("2025-01-01", periods=60, freq="D")  # 60 days of data
countries = ["CA","US","UK","DE","NG","IN","BR"]
devices   = ["iOS","Android","PC"]

# 2. create fake players ("users")
users = pd.DataFrame({
    "user_id": np.arange(1, N_USERS+1),
    "country": rng.choice(countries, N_USERS),
    "device": rng.choice(devices, N_USERS),
    "install_date": rng.choice(DAYS[:10], N_USERS)   # everyone installs in first 10 days
})

# 3. save it to disk  →  this becomes users.csv
users.to_csv("data/users.csv", index=False)
print("✅  Saved data/users.csv")

# 4. create gameplay "events"
rows = []
for day in DAYS:
    # pick 25 % of players active each day
    active_today = users[users.install_date <= day].sample(frac=0.25)
    for uid in active_today.user_id:
        sessions = rng.integers(1, 3)  # 1–2 sessions
        for s in range(sessions):
            sid = f"{uid}-{day.strftime('%Y%m%d')}-{s}"
            events = rng.choice(
                ["launch","match_start","match_end","purchase"],
                p=[0.3,0.4,0.25,0.05],
                size=rng.integers(2,6)
            )
            for e in events:
                spend = float(
                    rng.choice([0,0,0,1.99,4.99],
                               p=[0.9,0.03,0.03,0.03,0.01])
                )
                rows.append([uid, e, day, sid, spend])

events = pd.DataFrame(rows,
    columns=["user_id","event_type","date","session_id","spend"])

events.to_csv("data/events.csv", index=False)
print("✅  Saved data/events.csv")
