import pandas as pd
from pathlib import Path


# ==========================================
# LOAD CLEANED DELIVERIES DATA
# ==========================================

print("🏏 Starting batting analysis...")

deliveries = pd.read_csv(
    "data/cleaned/cleaned_deliveries.csv"
)

print(f"📊 Loaded {len(deliveries)} delivery records.")


# ==========================================
# CREATE OUTPUT FOLDER
# ==========================================

Path("outputs/csv").mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================
# BATTER-WISE STATISTICS
# ==========================================

batting_stats = (
    deliveries
    .groupby("batter")
    .agg(
        total_runs=("batsman_runs", "sum"),
        balls_faced=("batter", "count"),
        fours=(
            "batsman_runs",
            lambda x: (x == 4).sum()
        ),
        sixes=(
            "batsman_runs",
            lambda x: (x == 6).sum()
        )
    )
    .reset_index()
)


# ==========================================
# CALCULATE STRIKE RATE
# ==========================================

batting_stats["strike_rate"] = (
    batting_stats["total_runs"]
    * 100
    / batting_stats["balls_faced"]
).round(2)


# ==========================================
# SORT BY TOTAL RUNS
# ==========================================

batting_stats = (
    batting_stats
    .sort_values(
        by="total_runs",
        ascending=False
    )
)


# ==========================================
# SAVE RESULTS
# ==========================================

output_file = (
    "outputs/csv/"
    "batting_statistics.csv"
)

batting_stats.to_csv(
    output_file,
    index=False
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n🏆 Top 10 Run Scorers:\n")

print(
    batting_stats[
        [
            "batter",
            "total_runs",
            "balls_faced",
            "fours",
            "sixes",
            "strike_rate"
        ]
    ]
    .head(10)
    .to_string(index=False)
)


print(
    f"\n✅ Batting analysis completed."
)

print(
    f"📁 Results saved to: {output_file}"
)