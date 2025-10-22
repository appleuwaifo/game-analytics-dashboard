import pandas as pd
from datetime import timedelta

# Load our data
events = pd.read_csv("data/events.csv", parse_dates=["date"])
users  = pd.read_csv("data/users.csv", parse_dates=["install_date"])

# First day each user ever played
first_play = events.groupby("user_id")["date"].min().rename("first_day")
events = events.merge(first_play, on="user_id")

# Retention calculator
def retention(events, days):
    rows = []
    for fd in first_play.unique():
        cohort = first_play[first_play == fd].index
        check_day = fd + timedelta(days=days)
        active = events[
            (events["user_id"].isin(cohort)) &
            (events["date"] == check_day)
        ]["user_id"].nunique()
        total = len(cohort)
        rate = active / total if total else 0
        rows.append({"install_date": fd, f"D{days}_retention": rate})
    return pd.DataFrame(rows)

# Compute D1 & D7
ret1 = retention(events, 1)
ret7 = retention(events, 7)
retention_df = ret1.merge(ret7, on="install_date", how="outer")

retention_df.to_csv("outputs/retention.csv", index=False)
print("✅  Saved outputs/retention.csv")
print(retention_df.head())

