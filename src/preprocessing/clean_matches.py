import pandas as pd
from pathlib import Path

# -------------------------------
# Create output folders if needed
# -------------------------------
Path("data/cleaned").mkdir(parents=True, exist_ok=True)
Path("outputs/reports").mkdir(parents=True, exist_ok=True)

# -------------------------------
# Load dataset
# -------------------------------
matches = pd.read_csv("data/raw/matches.csv")

# -------------------------------
# Store original information
# -------------------------------
original_rows = len(matches)
duplicate_rows = matches.duplicated().sum()

# -------------------------------
# Remove duplicate rows
# -------------------------------
matches = matches.drop_duplicates()

# -------------------------------
# Convert date column to datetime
# -------------------------------
matches["date"] = pd.to_datetime(matches["date"])

# -------------------------------
# Check missing values
# -------------------------------
missing_values = matches.isnull().sum()

# -------------------------------
# Save cleaned dataset
# -------------------------------
matches.to_csv(
    "data/cleaned/cleaned_matches.csv",
    index=False
)

# -------------------------------
# Create Cleaning Report
# -------------------------------
with open("outputs/reports/cleaning_report.txt", "w", encoding="utf-8") as report:

    report.write("=" * 60 + "\n")
    report.write("MATCHES DATA CLEANING REPORT\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Original Rows : {original_rows}\n")
    report.write(f"Duplicate Rows Found : {duplicate_rows}\n")
    report.write(f"Rows After Cleaning : {len(matches)}\n\n")

    report.write("Missing Values\n")
    report.write("-" * 60 + "\n")
    report.write(missing_values.to_string())

print("✅ Matches dataset cleaned successfully.")
print("✅ Clean dataset saved to data/cleaned/")
print("✅ Cleaning report saved to outputs/reports/")