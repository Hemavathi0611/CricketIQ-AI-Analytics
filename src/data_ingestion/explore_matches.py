import pandas as pd

# Read dataset
matches = pd.read_csv("data/raw/matches.csv")

with open("outputs/reports/matches_report.txt", "w", encoding="utf-8") as f:

    f.write("=" * 60 + "\n")
    f.write("MATCHES DATASET REPORT\n")
    f.write("=" * 60 + "\n\n")

    # Shape
    f.write(f"Shape:\n{matches.shape}\n\n")

    # Columns
    f.write("Columns:\n")
    f.write(str(matches.columns.tolist()))
    f.write("\n\n")

    # Info
    f.write("Info:\n")
    matches.info(buf=f)

    # Missing Values
    f.write("\n\nMissing Values:\n")
    f.write(matches.isnull().sum().to_string())

    # First Five Rows
    f.write("\n\nFirst Five Rows:\n")
    f.write(matches.head().to_string())

    # Last Five Rows
    f.write("\n\nLast Five Rows:\n")
    f.write(matches.tail().to_string())

    # Statistical Summary
    f.write("\n\nStatistical Summary:\n")
    f.write(matches.describe(include="all").to_string())

print("Matches report saved successfully!")