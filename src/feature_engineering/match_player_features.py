import pandas as pd
from pathlib import Path


# ==========================================
# START MATCH-WISE FEATURE ENGINEERING
# ==========================================

print("🤖 Starting match-wise player feature engineering...")


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
# CREATE MATCH-WISE BATTER FEATURES
# ==========================================

match_player_features = (
    deliveries
    .groupby(
        [
            "match_id",
            "batter"
        ]
    )
    .agg(
        runs_scored=(
            "batsman_runs",
            "sum"
        ),
        balls_faced=(
            "batter",
            "count"
        ),
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

match_player_features["strike_rate"] = (
    match_player_features["runs_scored"]
    * 100
    / match_player_features["balls_faced"]
).round(2)


# ==========================================
# SORT DATA
# ==========================================

match_player_features = (
    match_player_features
    .sort_values(
        by=[
            "batter",
            "match_id"
        ]
    )
)


# ==========================================
# SAVE FEATURES
# ==========================================

output_file = (
    "data/processed/"
    "match_player_features.csv"
)

match_player_features.to_csv(
    output_file,
    index=False
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print(
    "\n🏏 Sample Match-Wise Player Features:\n"
)

print(
    match_player_features
    .head(10)
    .to_string(index=False)
)


print(
    "\n📊 Total match-player records: "
    f"{len(match_player_features)}"
)

print(
    "\n✅ Match-wise feature engineering completed."
)

print(
    f"📁 Features saved to: {output_file}"
)