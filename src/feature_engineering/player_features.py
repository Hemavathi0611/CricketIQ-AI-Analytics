import pandas as pd
from pathlib import Path


# ==========================================
# START FEATURE ENGINEERING
# ==========================================

print("🤖 Starting player feature engineering...")


# ==========================================
# LOAD CLEANED DELIVERY DATA
# ==========================================

deliveries = pd.read_csv(
    "data/cleaned/cleaned_deliveries.csv"
)

print(
    f"📊 Loaded {len(deliveries)} delivery records."
)


# ==========================================
# CREATE OUTPUT FOLDER
# ==========================================

Path("data/processed").mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================
# CREATE BATTER FEATURES
# ==========================================

player_features = (
    deliveries
    .groupby("batter")
    .agg(
        total_runs=(
            "batsman_runs",
            "sum"
        ),
        balls_faced=(
            "batter",
            "count"
        ),
        total_fours=(
            "batsman_runs",
            lambda x: (x == 4).sum()
        ),
        total_sixes=(
            "batsman_runs",
            lambda x: (x == 6).sum()
        ),
        total_matches=(
            "match_id",
            "nunique"
        )
    )
    .reset_index()
)


# ==========================================
# CALCULATE DERIVED FEATURES
# ==========================================

player_features["batting_average"] = (
    player_features["total_runs"]
    / player_features["total_matches"]
).round(2)


player_features["strike_rate"] = (
    player_features["total_runs"]
    * 100
    / player_features["balls_faced"]
).round(2)


player_features["boundary_runs"] = (
    player_features["total_fours"]
    * 4
    +
    player_features["total_sixes"]
    * 6
)


# ==========================================
# SORT BY TOTAL RUNS
# ==========================================

player_features = (
    player_features
    .sort_values(
        by="total_runs",
        ascending=False
    )
)


# ==========================================
# SAVE FEATURES
# ==========================================

output_file = (
    "data/processed/"
    "player_features.csv"
)

player_features.to_csv(
    output_file,
    index=False
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print(
    "\n🏏 Top 10 Player Features:\n"
)

print(
    player_features
    .head(10)
    .to_string(index=False)
)


print(
    "\n✅ Player feature engineering completed."
)

print(
    f"📁 Features saved to: {output_file}"
)