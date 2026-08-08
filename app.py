import streamlit as st
import pandas as pd
import joblib


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="CricketIQ AI Analytics",
    page_icon="🏏",
    layout="wide"
)


# ==========================================
# LOAD MODEL
# ==========================================

@st.cache_resource
def load_model():

    return joblib.load(
        "models/"
        "improved_next_match_score_model.pkl"
    )


model = load_model()


# ==========================================
# TITLE
# ==========================================

st.title(
    "🏏 CricketIQ AI Analytics"
)

st.subheader(
    "AI-Powered Next-Match Score Prediction"
)

st.write(
    "Enter a player's recent performance "
    "details to estimate the expected "
    "score in the next match."
)


# ==========================================
# PLAYER DETAILS
# ==========================================

st.divider()

st.subheader(
    "👤 Player Details"
)


player_name = st.text_input(
    "Player Name",
    value="V Kohli"
)


# ==========================================
# INPUT COLUMNS
# ==========================================

col1, col2 = st.columns(2)


with col1:

    previous_match_runs = st.number_input(
        "Previous-Match Runs",
        min_value=0,
        value=50,
        step=1
    )

    last_3_match_average = st.number_input(
        "Last 3-Match Average",
        min_value=0.0,
        value=45.0,
        step=0.1
    )

    last_5_match_average = st.number_input(
        "Last 5-Match Average",
        min_value=0.0,
        value=42.0,
        step=0.1
    )

    last_10_match_average = st.number_input(
        "Last 10-Match Average",
        min_value=0.0,
        value=40.0,
        step=0.1
    )

    last_5_match_std = st.number_input(
        "Last 5-Match Score Consistency",
        min_value=0.0,
        value=15.0,
        step=0.1
    )

    career_average = st.number_input(
        "Career Batting Average",
        min_value=0.0,
        value=33.0,
        step=0.1
    )


with col2:

    matches_played = st.number_input(
        "Matches Played",
        min_value=0,
        value=244,
        step=1
    )

    balls_faced = st.number_input(
        "Previous-Match Balls Faced",
        min_value=0,
        value=40,
        step=1
    )

    fours = st.number_input(
        "Previous-Match Fours",
        min_value=0,
        value=5,
        step=1
    )

    sixes = st.number_input(
        "Previous-Match Sixes",
        min_value=0,
        value=2,
        step=1
    )

    strike_rate = st.number_input(
        "Previous-Match Strike Rate",
        min_value=0.0,
        value=125.0,
        step=0.1
    )


# ==========================================
# PREDICTION BUTTON
# ==========================================

st.divider()


if st.button(
    "🏏 Predict Next-Match Score",
    use_container_width=True
):

    input_data = pd.DataFrame(
        [[
            previous_match_runs,
            last_3_match_average,
            last_5_match_average,
            last_10_match_average,
            last_5_match_std,
            career_average,
            matches_played,
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


    predicted_score = (
        model.predict(
            input_data
        )[0]
    )


    st.success(
        f"🏏 Predicted score for "
        f"{player_name}: "
        f"{predicted_score:.0f} runs"
    )


    st.metric(
        label="Predicted Next-Match Score",
        value=f"{predicted_score:.0f} runs"
    )


# ==========================================
# PROJECT INFORMATION
# ==========================================

st.divider()

st.caption(
    "CricketIQ AI Analytics | "
    "Machine Learning-based cricket "
    "performance analysis"
)