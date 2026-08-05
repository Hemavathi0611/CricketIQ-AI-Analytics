print("🚀 Script started...")

import pandas as pd
from src.utils.db_connection import get_connection


# -----------------------------------
# Load cleaned matches dataset
# -----------------------------------

print("📂 Reading cleaned_matches.csv...")

matches = pd.read_csv(
    "data/cleaned/cleaned_matches.csv"
)

print(f"📊 Loaded {len(matches)} match records from CSV.")


# -----------------------------------
# Convert date column
# -----------------------------------

matches["date"] = pd.to_datetime(
    matches["date"],
    errors="coerce"
).dt.date

print("✅ Date column converted.")


# -----------------------------------
# Connect to MySQL
# -----------------------------------

print("🔄 Connecting to MySQL...")

connection = get_connection()

print("📌 get_connection() finished.")

if connection is None:
    print("❌ Could not connect to MySQL.")
    raise SystemExit

print("✅ MySQL connection received.")

cursor = connection.cursor()

print("✅ MySQL cursor created.")


# -----------------------------------
# Insert query
# -----------------------------------

insert_query = """
INSERT INTO matches (
    match_id,
    season,
    city,
    match_date,
    match_type,
    player_of_match,
    venue,
    team1,
    team2,
    toss_winner,
    toss_decision,
    winner,
    result,
    result_margin,
    target_runs,
    target_overs,
    super_over,
    method,
    umpire1,
    umpire2
)
VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s
)
"""


# -----------------------------------
# Insert data
# -----------------------------------

print("📤 Starting data insertion...")

inserted_count = 0

for _, row in matches.iterrows():

    values = (
        int(row["id"]),
        str(row["season"]),
        None if pd.isna(row["city"]) else str(row["city"]),
        row["date"],
        str(row["match_type"]),
        None if pd.isna(row["player_of_match"])
        else str(row["player_of_match"]),
        str(row["venue"]),
        str(row["team1"]),
        str(row["team2"]),
        str(row["toss_winner"]),
        str(row["toss_decision"]),
        None if pd.isna(row["winner"])
        else str(row["winner"]),
        str(row["result"]),
        None if pd.isna(row["result_margin"])
        else float(row["result_margin"]),
        None if pd.isna(row["target_runs"])
        else float(row["target_runs"]),
        None if pd.isna(row["target_overs"])
        else float(row["target_overs"]),
        str(row["super_over"]),
        None if pd.isna(row["method"])
        else str(row["method"]),
        str(row["umpire1"]),
        str(row["umpire2"])
    )

    cursor.execute(insert_query, values)

    inserted_count += 1

    if inserted_count % 100 == 0:
        print(f"⏳ Inserted {inserted_count} records...")


# -----------------------------------
# Save and close
# -----------------------------------

connection.commit()

print("💾 Changes committed successfully.")

cursor.close()
connection.close()

print("🔒 MySQL connection closed.")

print(
    f"🎉 {inserted_count} match records "
    "loaded into MySQL successfully!"
)