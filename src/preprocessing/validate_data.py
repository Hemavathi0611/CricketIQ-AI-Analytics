import pandas as pd
from pathlib import Path

# -----------------------------------
# Create report folder if not exists
# -----------------------------------
Path("outputs/reports").mkdir(parents=True, exist_ok=True)

# -----------------------------------
# Load cleaned datasets
# -----------------------------------
matches = pd.read_csv("data/cleaned/cleaned_matches.csv")
deliveries = pd.read_csv("data/cleaned/cleaned_deliveries.csv")

# -----------------------------------
# Validation
# -----------------------------------

duplicate_matches = matches.duplicated().sum()
duplicate_deliveries = deliveries.duplicated().sum()

invalid_overs = deliveries[
    (deliveries["over"] < 0) | (deliveries["over"] > 19)
]

invalid_balls = deliveries[
    deliveries["ball"] < 1
]

negative_runs = deliveries[
    deliveries["total_runs"] < 0
]

invalid_wickets = deliveries[
    ~deliveries["is_wicket"].isin([0, 1])
]

# -----------------------------------
# Statistics
# -----------------------------------

unique_players = deliveries["batter"].nunique()

unique_bowlers = deliveries["bowler"].nunique()

unique_teams = pd.concat([
    matches["team1"],
    matches["team2"]
]).nunique()

unique_venues = matches["venue"].nunique()

season_start = matches["season"].min()
season_end = matches["season"].max()

# -----------------------------------
# Generate Validation Report
# -----------------------------------

with open("outputs/reports/validation_report.txt", "w", encoding="utf-8") as report:

    report.write("="*60 + "\n")
    report.write("DATA VALIDATION REPORT\n")
    report.write("="*60 + "\n\n")

    report.write(f"Duplicate Matches : {duplicate_matches}\n")
    report.write(f"Duplicate Deliveries : {duplicate_deliveries}\n\n")

    report.write(f"Invalid Overs : {len(invalid_overs)}\n")
    report.write(f"Invalid Balls : {len(invalid_balls)}\n")
    report.write(f"Negative Runs : {len(negative_runs)}\n")
    report.write(f"Invalid Wickets : {len(invalid_wickets)}\n\n")

    report.write(f"Unique Batters : {unique_players}\n")
    report.write(f"Unique Bowlers : {unique_bowlers}\n")
    report.write(f"Unique Teams : {unique_teams}\n")
    report.write(f"Unique Venues : {unique_venues}\n\n")

    report.write(f"Season Range : {season_start} to {season_end}\n")

print("✅ Validation completed successfully.")
print("✅ validation_report.txt generated.")