import pandas as pd

from pathlib import Path

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import joblib


# ==========================================
# START MODEL TRAINING
# ==========================================

print("🤖 Starting next-match score prediction model...")


# ==========================================
# LOAD PREDICTION DATA
# ==========================================

data = pd.read_csv(
    "data/processed/player_prediction_features.csv"
)

print(
    f"📊 Loaded {len(data)} training records."
)


# ==========================================
# SELECT INPUT FEATURES
# ==========================================

feature_columns = [
    "previous_match_runs",
    "last_3_match_average",
    "last_5_match_average",
    "balls_faced",
    "fours",
    "sixes",
    "strike_rate"
]


X = data[
    feature_columns
]


# ==========================================
# SELECT TARGET
# ==========================================

y = data[
    "next_match_runs"
]


print(
    f"📌 Number of input features: "
    f"{len(feature_columns)}"
)


# ==========================================
# SPLIT TRAINING AND TEST DATA
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
# CREATE MODEL
# ==========================================

model = RandomForestRegressor(
    n_estimators=200,
    max_depth=12,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1
)


# ==========================================
# TRAIN MODEL
# ==========================================

print(
    "⏳ Training Random Forest model..."
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
# CALCULATE MODEL METRICS
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


print(
    "\n📊 Model Performance:\n"
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
# CREATE MODELS FOLDER
# ==========================================

Path(
    "models"
).mkdir(
    parents=True,
    exist_ok=True
)


# ==========================================
# SAVE MODEL
# ==========================================

model_file = (
    "models/"
    "next_match_score_model.pkl"
)


joblib.dump(
    model,
    model_file
)


print(
    "\n💾 Model saved successfully."
)

print(
    f"📁 Model location: "
    f"{model_file}"
)