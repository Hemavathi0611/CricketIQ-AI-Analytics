import pandas as pd
from pathlib import Path


# ==========================================
# LOAD CLEANED MATCHES DATA
# ==========================================

print("🏏 Starting team analysis...")

matches = pd.read_csv(
    "data/cleaned/cleaned_matches.csv"
)

print(
    f"📊 Loaded {len(matches)} match records."
)


# ==========================================
# CREATE OUTPUT FOLDER
# ==========================================

Path("outputs/csv").mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================
# CALCULATE MATCHES PLAYED
# ==========================================

team1_matches = matches["team1"]

team2_matches = matches["team2"]

all_teams = pd.concat(
    [
        team1_matches,
        team2_matches
    ],
    ignore_index=True
)

matches_played = (
    all_teams
    .value_counts()
    .reset_index()
)

matches_played.columns = [
    "team",
    "matches_played"
]


# ==========================================
# CALCULATE MATCHES WON
# ==========================================

matches_won = (
    matches["winner"]
    .dropna()
    .value_counts()
    .reset_index()
)

matches_won.columns = [
    "team",
    "matches_won"
]


# ==========================================
# MERGE TEAM STATISTICS
# ==========================================

team_stats = matches_played.merge(
    matches_won,
    on="team",
    how="left"
)


# ==========================================
# HANDLE TEAMS WITH ZERO WINS
# ==========================================

team_stats["matches_won"] = (
    team_stats["matches_won"]
    .fillna(0)
    .astype(int)
)


# ==========================================
# CALCULATE LOSSES
# ==========================================

team_stats["matches_lost"] = (
    team_stats["matches_played"]
    -
    team_stats["matches_won"]
)


# ==========================================
# CALCULATE WIN PERCENTAGE
# ==========================================

team_stats["win_percentage"] = (
    team_stats["matches_won"]
    * 100
    / team_stats["matches_played"]
).round(2)


# ==========================================
# SORT BY TOTAL WINS
# ==========================================

team_stats = (
    team_stats
    .sort_values(
        by="matches_won",
        ascending=False
    )
)


# ==========================================
# SAVE RESULTS
# ==========================================

output_file = (
    "outputs/csv/"
    "team_statistics.csv"
)

team_stats.to_csv(
    output_file,
    index=False
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print(
    "\n🏆 Team Performance:\n"
)

print(
    team_stats[
        [
            "team",
            "matches_played",
            "matches_won",
            "matches_lost",
            "win_percentage"
        ]
    ]
    .head(10)
    .to_string(index=False)
)


print(
    "\n✅ Team analysis completed."
)

print(
    f"📁 Results saved to: {output_file}"
)