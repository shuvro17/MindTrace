"""MindTrace: educational digital wellbeing analytics prototype.
All demo data are synthetic; the app is not a clinical or therapeutic tool.
"""
import sqlite3
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from scipy.stats import spearmanr
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import balanced_accuracy_score, classification_report
from sklearn.model_selection import train_test_split

DB = Path(__file__).with_name("mindtrace.db")
FIELDS = ["screen_hours", "social_hours", "late_night_minutes", "sleep_hours", "mood", "stress"]

st.set_page_config(page_title="MindTrace", page_icon="🧠", layout="wide")


def connect():
    return sqlite3.connect(DB)


def initialize():
    with connect() as con:
        con.execute("""CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entry_date TEXT NOT NULL UNIQUE,
            screen_hours REAL NOT NULL,
            social_hours REAL NOT NULL,
            late_night_minutes INTEGER NOT NULL,
            sleep_hours REAL NOT NULL,
            mood INTEGER NOT NULL,
            stress INTEGER NOT NULL,
            source TEXT NOT NULL DEFAULT 'personal'
        )""")


def load_entries():
    with connect() as con:
        df = pd.read_sql_query("SELECT * FROM entries ORDER BY entry_date", con)
    if not df.empty:
        df["entry_date"] = pd.to_datetime(df["entry_date"])
    return df


def add_entry(entry_date, screen, social, late, sleep, mood, stress):
    if social > screen:
        raise ValueError("Social media time cannot exceed total screen time.")
    with connect() as con:
        con.execute("""INSERT INTO entries
            (entry_date, screen_hours, social_hours, late_night_minutes, sleep_hours, mood, stress, source)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'personal')
            ON CONFLICT(entry_date) DO UPDATE SET
            screen_hours=excluded.screen_hours, social_hours=excluded.social_hours,
            late_night_minutes=excluded.late_night_minutes, sleep_hours=excluded.sleep_hours,
            mood=excluded.mood, stress=excluded.stress, source='personal'""",
            (entry_date.isoformat(), screen, social, late, sleep, mood, stress))


def make_demo(n=180):
    """Synthetic observations for demonstrating software, not real research."""
    rng = np.random.default_rng(42)
    screen = rng.uniform(1.5, 10, n)
    social = np.array([rng.uniform(0.2, max(0.21, x * 0.75)) for x in screen])
    late = rng.integers(0, 181, n)
    sleep = np.clip(8.4 - 0.012 * late - 0.08 * screen + rng.normal(0, 0.9, n), 3, 11)
    stress = np.clip(np.rint(2.2 + 0.35 * screen + 0.015 * late - 0.34 * sleep + rng.normal(0, 1.6, n)), 1, 10).astype(int)
    mood = np.clip(np.rint(8 - 0.48 * stress + rng.normal(0, 1.2, n)), 1, 10).astype(int)
    dates = [date.today() - timedelta(days=n-i-1) for i in range(n)]
    return pd.DataFrame({"entry_date": pd.to_datetime(dates), "screen_hours": screen.round(1),
                         "social_hours": social.round(1), "late_night_minutes": late,
                         "sleep_hours": sleep.round(1), "mood": mood, "stress": stress,
                         "source": "synthetic"})


initialize()
st.title("🧠 MindTrace")
st.caption("Privacy-aware digital wellbeing and behavioural analytics | Educational prototype")
st.warning("Not a medical device or therapy service. No diagnosis or treatment advice. Synthetic data are for demonstration only.")

page = st.sidebar.radio("Navigate", ["Overview", "Daily Check-in", "Behavioural Analytics", "ML Demonstration", "Data & Privacy", "About"])
records = load_entries()

if page == "Overview":
    st.header("Wellbeing Overview")
    st.write("Explore voluntary daily check-ins or use synthetic demonstration data to preview the dashboard.")
    use_demo = st.toggle("Use synthetic demonstration data", value=records.empty)
    df = make_demo() if use_demo else records
    if df.empty:
        st.info("No entries yet. Add a daily check-in or turn on demonstration data.")
    else:
        if use_demo:
            st.info("Showing synthetic data. These are not observations from real people.")
        a, b, c, d = st.columns(4)
        a.metric("Entries", len(df))
        b.metric("Avg. screen time", f"{df.screen_hours.mean():.1f} h")
        c.metric("Avg. sleep", f"{df.sleep_hours.mean():.1f} h")
        d.metric("Avg. stress", f"{df.stress.mean():.1f}/10")
        st.plotly_chart(px.line(df, x="entry_date", y=["stress", "mood"], title="Self-reported stress and mood over time"), use_container_width=True)
        st.plotly_chart(px.scatter(df, x="screen_hours", y="stress", color="sleep_hours", title="Screen time and self-reported stress"), use_container_width=True)

elif page == "Daily Check-in":
    st.header("Daily Check-in")
    st.write("Optional local-only tracking. One record per day; saving the same date replaces it.")
    with st.form("checkin"):
        day = st.date_input("Date", value=date.today(), max_value=date.today())
        screen = st.number_input("Total screen time (hours)", 0.0, 24.0, 4.0, 0.5)
        social = st.number_input("Social media time (hours)", 0.0, 24.0, 2.0, 0.5)
        late = st.number_input("Late-night device use (minutes)", 0, 600, 30, 5)
        sleep = st.number_input("Sleep duration (hours)", 0.0, 24.0, 7.0, 0.5)
        mood = st.slider("Mood (1 = very low, 10 = very positive)", 1, 10, 6)
        stress = st.slider("Perceived stress (1 = very low, 10 = very high)", 1, 10, 5)
        consent = st.checkbox("I understand these records are stored locally on this computer and are not used for medical decisions.")
        submitted = st.form_submit_button("Save check-in")
    if submitted:
        if not consent:
            st.error("Please acknowledge the local data storage notice.")
        else:
            try:
                add_entry(day, screen, social, late, sleep, mood, stress)
                st.success("Check-in saved locally.")
            except ValueError as err:
                st.error(str(err))

elif page == "Behavioural Analytics":
    st.header("Behavioural Analytics")
    source = st.radio("Dataset", ["Synthetic demo", "My local check-ins"], horizontal=True)
    df = make_demo() if source == "Synthetic demo" else records
    if df.empty or len(df) < 3:
        st.info("At least three records are needed for exploratory analysis.")
    else:
        if source == "Synthetic demo":
            st.info("The patterns in this synthetic dataset were deliberately generated and do not establish scientific findings.")
        st.plotly_chart(px.scatter(df, x="late_night_minutes", y="stress", color="sleep_hours", title="Late-night use vs. perceived stress"), use_container_width=True)
        st.plotly_chart(px.box(df, x="stress", y="sleep_hours", title="Sleep duration by stress rating"), use_container_width=True)
        st.subheader("Exploratory Spearman correlations")
        rows = []
        for col in ["screen_hours", "social_hours", "late_night_minutes", "sleep_hours", "mood"]:
            if df[col].nunique() > 1 and df["stress"].nunique() > 1:
                coefficient, pvalue = spearmanr(df[col], df["stress"])
                rows.append({"Feature": col, "Spearman rho": round(float(coefficient), 3), "p-value": round(float(pvalue), 4)})
        st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
        st.caption("Exploratory associations only. Correlation does not imply causation; p-values are not corrected for multiple testing.")

elif page == "ML Demonstration":
    st.header("Explainable ML Demonstration")
    st.info("Trains only on generated synthetic data. This is a technical demonstration, not a validated stress predictor.")
    df = make_demo(500)
    X = df[["screen_hours", "social_hours", "late_night_minutes", "sleep_hours"]]
    y = (df["stress"] >= 6).astype(int)
    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    baseline = DummyClassifier(strategy="most_frequent").fit(Xtrain, ytrain)
    model = RandomForestClassifier(n_estimators=120, max_depth=5, min_samples_leaf=5, random_state=42).fit(Xtrain, ytrain)
    a, b = st.columns(2)
    a.metric("Baseline balanced accuracy", f"{balanced_accuracy_score(ytest, baseline.predict(Xtest)):.2f}")
    b.metric("Model balanced accuracy", f"{balanced_accuracy_score(ytest, model.predict(Xtest)):.2f}")
    st.text(classification_report(ytest, model.predict(Xtest), zero_division=0))
    importance = pd.DataFrame({"Feature": X.columns, "Importance": model.feature_importances_}).sort_values("Importance")
    st.plotly_chart(px.bar(importance, x="Importance", y="Feature", orientation="h", title="Model feature importance (not causal effect)"), use_container_width=True)
    st.caption("Random train/test split is acceptable for this independent synthetic demo; repeated observations from real participants would require participant-grouped validation.")

elif page == "Data & Privacy":
    st.header("Data & Privacy")
    st.write("Personal entries are saved in a local SQLite database beside app.py. No cloud account, tracking service, or external API is used by this application.")
    if records.empty:
        st.info("No personal records stored.")
    else:
        st.dataframe(records.drop(columns=["id"]), use_container_width=True, hide_index=True)
        st.download_button("Export my data as CSV", records.drop(columns=["id"]).to_csv(index=False), "mindtrace_export.csv", "text/csv")
        st.subheader("Delete local records")
        confirm = st.checkbox("I understand deletion of my local check-ins cannot be undone.")
        if st.button("Delete all personal records", disabled=not confirm):
            with connect() as con:
                con.execute("DELETE FROM entries")
            st.success("Local check-ins deleted.")
            st.rerun()
    st.caption("For research involving other people, separate ethical review, participant information, and appropriate data protection measures are required.")

else:
    st.header("About MindTrace")
    st.markdown("""**MindTrace** is an educational prototype exploring the intersection of cyberspace behaviour, human-computer interaction, data science, and digital wellbeing.

**Research question:** How might self-reported digital habits and sleep relate to perceived stress?

**Limitations:** Self-report bias, no clinical validation, no causal inference, and synthetic-only ML evaluation. It is not a therapeutic intervention.

**Stack:** Python, Streamlit, SQLite, Pandas, SciPy, Plotly, scikit-learn.

**Next steps:** Ethics-reviewed pilot, validated survey instruments, usability evaluation, and participant-grouped validation if longitudinal data are collected.
""")
