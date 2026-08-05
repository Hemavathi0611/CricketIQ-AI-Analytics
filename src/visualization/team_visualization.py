import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ==========================================
# LOAD TEAM STATISTICS
# ==========================================

print("🏆 Starting team visualization...")

team_stats = pd.read_csv(
    "outputs/csv/team_statistics.csv"
)

print(
    f"✅ Loaded {len(team_stats)} team records."
)


# ==========================================
# CREATE OUTPUT FOLDER
# ==========================================

Path("outputs/graphs").mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================
# SELECT TOP 10 TEAMS
# ==========================================

top_teams = (
    team_stats
    .sort_values(
        by="matches_won",
        ascending=False
    )
    .head(10)
)


# ==========================================
# CREATE BAR GRAPH
# ==========================================

plt.figure(
    figsize=(13, 7)
)

plt.bar(
    top_teams["team"],
    top_teams["matches_won"]
)

plt.title(
    "Top IPL Teams by Total Wins"
)

plt.xlabel(
    "Team"
)

plt.ylabel(
    "Matches Won"
)

plt.xticks(
    rotation=45,
    ha="right"
)

plt.tight_layout()


# ==========================================
# SAVE GRAPH
# ==========================================

output_file = (
    "outputs/graphs/"
    "top_teams_by_wins.png"
)

plt.savefig(
    output_file,
    dpi=300
)

plt.close()


print(
    "✅ Team visualization completed."
)

print(
    f"📁 Graph saved to: {output_file}"
)