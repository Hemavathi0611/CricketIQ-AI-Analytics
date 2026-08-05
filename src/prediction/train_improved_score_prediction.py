import pandas as pd
import joblib

from pathlib import Path

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ==========================================
# START IMPROVED MODEL TRAINING
# ==========================================

print("🤖 Starting improved score prediction model...")


# ==========================================
# LOAD IMPROVED DATASET
# ==========================================

data = pd.read_csv(
    "data/processed/"
    "improved_player_prediction_features.csv"
)

print(
    f"📊 Loaded {len(data)} training records."
)


# ==========================================
# SELECT NUMERICAL FEATURES
# ==========================================

feature_columns = [
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


X = data[
    feature_columns
].copy()


# ==========================================
# TARGET COLUMN
# ==========================================

y = data[
    "next_match_runs"
]


print(
    f"📌 Number of input features: "
    f"{len(feature_columns)}"
)


# ==========================================
# TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42
    )
)


print(
    f"📚 Training records: "
    f"{len(X_train)}"
)

print(
    f"🧪 Testing records: "
    f"{len(X_test)}"
)


# ==========================================
# CREATE IMPROVED RANDOM FOREST MODEL
# ==========================================

model = RandomForestRegressor(
    n_estimators=300,
    max_depth=15,
    min_samples_split=8,
    min_samples_leaf=3,
    max_features="sqrt",
    random_state=42,
    n_jobs=-1
)


# ==========================================
# TRAIN MODEL
# ==========================================

print(
    "⏳ Training improved Random Forest model..."
)

model.fit(
    X_train,
    y_train
)

print(
    "✅ Model training completed."
)


# ==========================================
# MAKE PREDICTIONS
# ==========================================

predictions = model.predict(
    X_test
)


# ==========================================
# CALCULATE METRICS
# ==========================================

mae = mean_absolute_error(
    y_test,
    predictions
)


rmse = (
    mean_squared_error(
        y_test,
        predictions
    )
    ** 0.5
)


r2 = r2_score(
    y_test,
    predictions
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print(
    "\n📊 Improved Model Performance:\n"
)

print(
    f"Mean Absolute Error: "
    f"{mae:.2f} runs"
)

print(
    f"Root Mean Squared Error: "
    f"{rmse:.2f} runs"
)

print(
    f"R² Score: "
    f"{r2:.4f}"
)


# ==========================================
# SAVE MODEL
# ==========================================

Path(
    "models"
).mkdir(
    parents=True,
    exist_ok=True
)


model_file = (
    "models/"
    "improved_next_match_score_model.pkl"
)


joblib.dump(
    model,
    model_file
)


print(
    "\n💾 Improved model saved successfully."
)

print(
    f"📁 Model location: "
    f"{model_file}"
)