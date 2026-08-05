import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# ==========================================
# LOAD BATTING STATISTICS
# ==========================================

print("📊 Starting batting visualization...")

batting = pd.read_csv(
    "outputs/csv/batting_statistics.csv"
)

print(
    f"✅ Loaded {len(batting)} batting records."
)


# ==========================================
# CREATE OUTPUT FOLDER
# ==========================================

Path("outputs/graphs").mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================
# SELECT TOP 10 BATTERS
# ==========================================

top_batters = (
    batting
    .sort_values(
        by="total_runs",
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
    top_batters["batter"],
    top_batters["total_runs"]
)

plt.title(
    "Top 10 IPL Run Scorers"
)

plt.xlabel(
    "Batter"
)

plt.ylabel(
    "Total Runs"
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
    "top_10_run_scorers.png"
)

plt.savefig(
    output_file,
    dpi=300
)

plt.close()


print(
    "✅ Batting visualization completed."
)

print(
    f"📁 Graph saved to: {output_file}"
)