print("🚀 Deliveries loading script started...")

import pandas as pd
from src.utils.db_connection import get_connection


# -----------------------------------
# Load cleaned deliveries dataset
# -----------------------------------

print("📂 Reading cleaned_deliveries.csv...")

deliveries = pd.read_csv(
    "data/cleaned/cleaned_deliveries.csv"
)

print(f"📊 Loaded {len(deliveries)} delivery records from CSV.")


# -----------------------------------
# Connect to MySQL
# -----------------------------------

print("🔄 Connecting to MySQL...")

connection = get_connection()

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
INSERT INTO deliveries (
    match_id,
    inning,
    batting_team,
    bowling_team,
    over_number,
    ball_number,
    batter,
    bowler,
    non_striker,
    batsman_runs,
    extra_runs,
    total_runs,
    extras_type,
    is_wicket,
    player_dismissed,
    dismissal_kind,
    fielder
)
VALUES (
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s,
    %s, %s
)
"""


# -----------------------------------
# Prepare data
# -----------------------------------

print("🔄 Preparing delivery records...")

records = []

for _, row in deliveries.iterrows():

    values = (
        int(row["match_id"]),
        int(row["inning"]),
        str(row["batting_team"]),
        str(row["bowling_team"]),
        int(row["over"]),
        int(row["ball"]),
        str(row["batter"]),
        str(row["bowler"]),
        str(row["non_striker"]),
        int(row["batsman_runs"]),
        int(row["extra_runs"]),
        int(row["total_runs"]),
        None if pd.isna(row["extras_type"])
        else str(row["extras_type"]),
        int(row["is_wicket"]),
        None if pd.isna(row["player_dismissed"])
        else str(row["player_dismissed"]),
        None if pd.isna(row["dismissal_kind"])
        else str(row["dismissal_kind"]),
        None if pd.isna(row["fielder"])
        else str(row["fielder"])
    )

    records.append(values)

print(f"✅ Prepared {len(records)} delivery records.")


# -----------------------------------
# Batch insertion
# -----------------------------------

print("📤 Starting batch insertion...")

batch_size = 5000

inserted_count = 0

for start in range(0, len(records), batch_size):

    batch = records[start:start + batch_size]

    cursor.executemany(
        insert_query,
        batch
    )

    connection.commit()

    inserted_count += len(batch)

    print(
        f"⏳ Inserted {inserted_count} "
        f"of {len(records)} records..."
    )


# -----------------------------------
# Close connection
# -----------------------------------

cursor.close()
connection.close()

print("🔒 MySQL connection closed.")

print(
    f"🎉 {inserted_count} delivery records "
    "loaded into MySQL successfully!"
)