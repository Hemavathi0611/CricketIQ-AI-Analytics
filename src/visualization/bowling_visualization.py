import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ==========================================
# LOAD BOWLING STATISTICS
# ==========================================

print("🎯 Starting bowling visualization...")

bowling = pd.read_csv(
    "outputs/csv/bowling_statistics.csv"
)

print(
    f"✅ Loaded {len(bowling)} bowling records."
)


# ==========================================
# CREATE OUTPUT FOLDER
# ==========================================

Path("outputs/graphs").mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================
# SELECT TOP 10 WICKET TAKERS
# ==========================================

top_bowlers = (
    bowling
    .sort_values(
        by="total_wickets",
        ascending=False
    )
    .head(10)
)


# ==========================================
# CREATE BAR GRAPH
# ==========================================

plt.figure(
    figsize=(12, 7)
)

plt.bar(
    top_bowlers["bowler"],
    top_bowlers["total_wickets"]
)

plt.title(
    "Top 10 IPL Wicket Takers"
)

plt.xlabel(
    "Bowler"
)

plt.ylabel(
    "Total Wickets"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()


# ==========================================
# SAVE GRAPH
# ==========================================

output_file = (
    "outputs/graphs/"
    "top_10_wicket_takers.png"
)

plt.savefig(
    output_file,
    dpi=300
)

plt.close()


print(
    "✅ Bowling visualization completed."
)

print(
    f"📁 Graph saved to: {output_file}"
)