import pandas as pd
from pathlib import Path


# ==========================================
# LOAD CLEANED DELIVERIES DATA
# ==========================================

print("🎯 Starting bowling analysis...")

deliveries = pd.read_csv(
    "data/cleaned/cleaned_deliveries.csv"
)

print(
    f"📊 Loaded {len(deliveries)} delivery records."
)


# ==========================================
# CREATE OUTPUT FOLDER
# ==========================================

Path("outputs/csv").mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================
# IDENTIFY BOWLER WICKETS
# ==========================================

bowler_wickets = deliveries[
    (deliveries["is_wicket"] == 1)
    &
    (~deliveries["dismissal_kind"].isin([
        "run out",
        "retired hurt",
        "obstructing the field"
    ]))
]


# ==========================================
# CALCULATE BOWLER STATISTICS
# ==========================================

bowling_stats = (
    deliveries
    .groupby("bowler")
    .agg(
        balls_bowled=("bowler", "count"),
        runs_conceded=("total_runs", "sum"),
        dot_balls=(
            "total_runs",
            lambda x: (x == 0).sum()
        )
    )
    .reset_index()
)


# ==========================================
# ADD WICKETS
# ==========================================

wicket_counts = (
    bowler_wickets
    .groupby("bowler")
    .size()
    .reset_index(
        name="total_wickets"
    )
)


bowling_stats = bowling_stats.merge(
    wicket_counts,
    on="bowler",
    how="left"
)


# ==========================================
# HANDLE BOWLERS WITH ZERO WICKETS
# ==========================================

bowling_stats["total_wickets"] = (
    bowling_stats["total_wickets"]
    .fillna(0)
    .astype(int)
)


# ==========================================
# CALCULATE ECONOMY RATE
# ==========================================

bowling_stats["economy_rate"] = (
    bowling_stats["runs_conceded"]
    * 6
    / bowling_stats["balls_bowled"]
).round(2)


# ==========================================
# CALCULATE BOWLING STRIKE RATE
# ==========================================

bowling_stats["bowling_strike_rate"] = (
    bowling_stats["balls_bowled"]
    / bowling_stats["total_wickets"]
)

bowling_stats["bowling_strike_rate"] = (
    bowling_stats["bowling_strike_rate"]
    .replace(
        [float("inf")],
        0
    )
    .round(2)
)


# ==========================================
# SORT BY WICKETS
# ==========================================

bowling_stats = (
    bowling_stats
    .sort_values(
        by="total_wickets",
        ascending=False
    )
)


# ==========================================
# SAVE RESULTS
# ==========================================

output_file = (
    "outputs/csv/"
    "bowling_statistics.csv"
)

bowling_stats.to_csv(
    output_file,
    index=False
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n🏆 Top 10 Wicket Takers:\n")

print(
    bowling_stats[
        [
            "bowler",
            "total_wickets",
            "runs_conceded",
            "dot_balls",
            "economy_rate",
            "bowling_strike_rate"
        ]
    ]
    .head(10)
    .to_string(index=False)
)


print(
    "\n✅ Bowling analysis completed."
)

print(
    f"📁 Results saved to: {output_file}"
)