import pandas as pd
from pathlib import Path

# -------------------------------
# Create output folders if needed
# -------------------------------
Path("data/cleaned").mkdir(parents=True, exist_ok=True)
Path("outputs/reports").mkdir(parents=True, exist_ok=True)

# -------------------------------
# Load deliveries dataset
# -------------------------------
deliveries = pd.read_csv("data/raw/deliveries.csv")

# -------------------------------
# Store original information
# -------------------------------
original_rows = len(deliveries)
duplicate_rows = deliveries.duplicated().sum()

# -------------------------------
# Remove duplicate rows
# -------------------------------
deliveries = deliveries.drop_duplicates()

# -------------------------------
# Validate over numbers
# -------------------------------
invalid_overs = deliveries[
    (deliveries["over"] < 1) | (deliveries["over"] > 20)
]

# -------------------------------
# Validate ball numbers
# -------------------------------
invalid_balls = deliveries[
    (deliveries["ball"] < 1) | (deliveries["ball"] > 10)
]

# -------------------------------
# Missing values
# -------------------------------
missing_values = deliveries.isnull().sum()

# -------------------------------
# Save cleaned dataset
# -------------------------------
deliveries.to_csv(
    "data/cleaned/cleaned_deliveries.csv",
    index=False
)

# -------------------------------
# Append Cleaning Report
# -------------------------------
with open("outputs/reports/cleaning_report.txt", "a", encoding="utf-8") as report:

    report.write("\n\n")
    report.write("=" * 60 + "\n")
    report.write("DELIVERIES DATA CLEANING REPORT\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Original Rows : {original_rows}\n")
    report.write(f"Duplicate Rows Found : {duplicate_rows}\n")
    report.write(f"Rows After Cleaning : {len(deliveries)}\n\n")

    report.write(f"Invalid Overs : {len(invalid_overs)}\n")
    report.write(f"Invalid Balls : {len(invalid_balls)}\n\n")

    report.write("Missing Values\n")
    report.write("-" * 60 + "\n")
    report.write(missing_values.to_string())

print("✅ Deliveries dataset cleaned successfully.")
print("✅ Clean dataset saved.")
print("✅ Cleaning report updated.")