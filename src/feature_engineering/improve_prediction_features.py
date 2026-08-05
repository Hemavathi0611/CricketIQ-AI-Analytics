import pandas as pd
from pathlib import Path


print("🚀 Creating improved prediction features...")


# ==========================================
# LOAD DATA
# ==========================================

data = pd.read_csv(
    "data/processed/match_player_features.csv"
)

matches = pd.read_csv(
    "data/cleaned/cleaned_matches.csv"
)

print(
    f"📊 Loaded {len(data)} match-player records."
)


# ==========================================
# ADD MATCH INFORMATION
# ==========================================

matches = matches[
    [
        "id",
        "season",
        "venue",
        "team1",
        "team2"
    ]
].copy()

matches = matches.rename(
    columns={
        "id": "match_id"
    }
)

data = data.merge(
    matches,
    on="match_id",
    how="left"
)


# ==========================================
# SORT PLAYER HISTORY
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
# RECENT-FORM FEATURES
# ==========================================

grouped_runs = (
    data
    .groupby("batter")["runs_scored"]
)


data["previous_match_runs"] = (
    grouped_runs.shift(1)
)


data["last_3_match_average"] = (
    grouped_runs.transform(
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
    grouped_runs.transform(
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


data["last_10_match_average"] = (
    grouped_runs.transform(
        lambda x: (
            x.shift(1)
            .rolling(
                window=10,
                min_periods=1
            )
            .mean()
        )
    )
)


data["last_5_match_std"] = (
    grouped_runs.transform(
        lambda x: (
            x.shift(1)
            .rolling(
                window=5,
                min_periods=2
            )
            .std()
        )
    )
)


# ==========================================
# CAREER FEATURES
# ==========================================

data["career_average_before_match"] = (
    grouped_runs.transform(
        lambda x: (
            x.shift(1)
            .expanding()
            .mean()
        )
    )
)


data["matches_played_before"] = (
    data
    .groupby("batter")
    .cumcount()
)


# ==========================================
# NEXT-MATCH TARGET
# ==========================================

data["next_match_runs"] = (
    grouped_runs.shift(-1)
)


# ==========================================
# REMOVE INCOMPLETE RECORDS
# ==========================================

prediction_data = data.dropna(
    subset=[
        "previous_match_runs",
        "next_match_runs"
    ]
).copy()


# Fill standard deviation for players
# with limited match history

prediction_data[
    "last_5_match_std"
] = (
    prediction_data[
        "last_5_match_std"
    ]
    .fillna(0)
)


# ==========================================
# ROUND NUMERIC VALUES
# ==========================================

numeric_columns = [
    "last_3_match_average",
    "last_5_match_average",
    "last_10_match_average",
    "last_5_match_std",
    "career_average_before_match"
]

prediction_data[
    numeric_columns
] = (
    prediction_data[
        numeric_columns
    ]
    .round(2)
)


# ==========================================
# SAVE DATASET
# ==========================================

Path(
    "data/processed"
).mkdir(
    parents=True,
    exist_ok=True
)


output_file = (
    "data/processed/"
    "improved_player_prediction_features.csv"
)


prediction_data.to_csv(
    output_file,
    index=False
)


print(
    f"📊 Final training records: "
    f"{len(prediction_data)}"
)


print(
    "✅ Improved prediction features created."
)


print(
    f"📁 Saved to: {output_file}"
)