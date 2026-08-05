import pandas as pd
from pathlib import Path


# ==========================================
# START PREDICTION FEATURE CREATION
# ==========================================

print("🤖 Creating next-match prediction features...")


# ==========================================
# LOAD MATCH-WISE PLAYER DATA
# ==========================================

data = pd.read_csv(
    "data/processed/match_player_features.csv"
)

print(
    f"📊 Loaded {len(data)} match-player records."
)


# ==========================================
# SORT PLAYER MATCH HISTORY
# ==========================================

data = data.sort_values(
    by=[
        "batter",
        "match_id"
    ]
).reset_index(
    drop=True
)


# ==========================================
# CREATE PREVIOUS-MATCH FEATURES
# ==========================================

data["previous_match_runs"] = (
    data
    .groupby("batter")["runs_scored"]
    .shift(1)
)


data["last_3_match_average"] = (
    data
    .groupby("batter")["runs_scored"]
    .transform(
        lambda x: (
            x.shift(1)
            .rolling(
                window=3,
                min_periods=1
            )
            .mean()
        )
    )
)


data["last_5_match_average"] = (
    data
    .groupby("batter")["runs_scored"]
    .transform(
        lambda x: (
            x.shift(1)
            .rolling(
                window=5,
                min_periods=1
            )
            .mean()
        )
    )
)


# ==========================================
# CREATE NEXT-MATCH TARGET
# ==========================================

data["next_match_runs"] = (
    data
    .groupby("batter")["runs_scored"]
    .shift(-1)
)


# ==========================================
# REMOVE RECORDS WITHOUT HISTORY/TARGET
# ==========================================

prediction_data = data.dropna(
    subset=[
        "previous_match_runs",
        "next_match_runs"
    ]
).copy()


# ==========================================
# ROUND NUMERIC FEATURES
# ==========================================

prediction_data[
    "last_3_match_average"
] = (
    prediction_data[
        "last_3_match_average"
    ]
    .round(2)
)


prediction_data[
    "last_5_match_average"
] = (
    prediction_data[
        "last_5_match_average"
    ]
    .round(2)
)


# ==========================================
# CREATE OUTPUT FOLDER
# ==========================================

Path(
    "data/processed"
).mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================
# SAVE TRAINING DATASET
# ==========================================

output_file = (
    "data/processed/"
    "player_prediction_features.csv"
)

prediction_data.to_csv(
    output_file,
    index=False
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print(
    "\n🏏 Sample Prediction Features:\n"
)

print(
    prediction_data[
        [
            "batter",
            "runs_scored",
            "previous_match_runs",
            "last_3_match_average",
            "last_5_match_average",
            "next_match_runs"
        ]
    ]
    .head(10)
    .to_string(index=False)
)


print(
    f"\n📊 Final training records: "
    f"{len(prediction_data)}"
)


print(
    "\n✅ Prediction features created successfully."
)

print(
    f"📁 Saved to: {output_file}"
)