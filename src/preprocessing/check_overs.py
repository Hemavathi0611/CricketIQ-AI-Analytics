import pandas as pd

deliveries = pd.read_csv("data/cleaned/cleaned_deliveries.csv")

print("Maximum Over:")
print(deliveries["over"].max())

print("\nUnique Overs:")
print(sorted(deliveries["over"].unique()))

print("\nInvalid Ball Records:")

invalid_balls = deliveries[
    (deliveries["ball"] < 1) |
    (deliveries["ball"] > 10)
]

print(
    invalid_balls[
        [
            "match_id",
            "inning",
            "over",
            "ball",
            "batter",
            "bowler",
            "total_runs"
        ]
    ]
)