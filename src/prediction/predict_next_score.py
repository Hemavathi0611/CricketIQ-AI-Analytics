import pandas as pd
import joblib


print("🏏 CricketIQ Next-Match Score Predictor")


# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load(
    "models/improved_next_match_score_model.pkl"
)

print("✅ Improved ML model loaded.")


# ==========================================
# PLAYER INPUT
# ==========================================

player_name = input(
    "\nEnter player name: "
)


previous_match_runs = float(
    input(
        "Previous-match runs: "
    )
)


last_3_match_average = float(
    input(
        "Last 3-match average: "
    )
)


last_5_match_average = float(
    input(
        "Last 5-match average: "
    )
)


last_10_match_average = float(
    input(
        "Last 10-match average: "
    )
)


last_5_match_std = float(
    input(
        "Last 5-match score standard deviation: "
    )
)


career_average_before_match = float(
    input(
        "Career batting average: "
    )
)


matches_played_before = int(
    input(
        "Matches played: "
    )
)


balls_faced = float(
    input(
        "Previous-match balls faced: "
    )
)


fours = float(
    input(
        "Previous-match fours: "
    )
)


sixes = float(
    input(
        "Previous-match sixes: "
    )
)


strike_rate = float(
    input(
        "Previous-match strike rate: "
    )
)


# ==========================================
# CREATE INPUT DATA
# ==========================================

input_data = pd.DataFrame(
    [[
        previous_match_runs,
        last_3_match_average,
        last_5_match_average,
        last_10_match_average,
        last_5_match_std,
        career_average_before_match,
        matches_played_before,
        balls_faced,
        fours,
        sixes,
        strike_rate
    ]],
    columns=[
        "previous_match_runs",
        "last_3_match_average",
        "last_5_match_average",
        "last_10_match_average",
        "last_5_match_std",
        "career_average_before_match",
        "matches_played_before",
        "balls_faced",
        "fours",
        "sixes",
        "strike_rate"
    ]
)


# ==========================================
# PREDICT SCORE
# ==========================================

predicted_score = model.predict(
    input_data
)[0]


# ==========================================
# DISPLAY RESULT
# ==========================================

print(
    "\n================================"
)

print(
    f"🏏 Player: {player_name}"
)

print(
    f"🤖 Predicted next-match score: "
    f"{predicted_score:.0f} runs"
)

print(
    "================================"
)