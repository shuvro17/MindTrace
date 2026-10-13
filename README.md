# MindTrace — Digital Wellbeing & Behavioural Analytics

A privacy-aware educational prototype investigating relationships between self-reported digital habits, sleep, mood, and stress. Designed as an interdisciplinary Computer Science / digital health portfolio project.

**Important:** This application is not a medical device, therapy tool, or diagnostic service. Demonstration data are synthetic and must not be described as real research findings.

## Features
- Daily check-ins saved in local SQLite
- Interactive behavioural dashboards
- Spearman correlation analysis
- Random forest demonstration with majority-class baseline and feature importance
- CSV export and deletion of local entries
- Research and ethics limitations explained in the interface

## Requirements
Python 3.11 or 3.12 is recommended.

## Windows setup (PowerShell in VS Code)
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```
If Python 3.12 is unavailable, use `py -3.11` for the first command.

## Run again
```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```
Then open the localhost URL displayed in the terminal (usually http://localhost:8501).

## Files
- `app.py` — Streamlit app, data processing and analytics
- `requirements.txt` — Python dependencies
- `mindtrace.db` — generated local database, never commit real personal entries

## Ethics and methodological notes
- Synthetic records are deliberately generated with relationships and cannot validate real-world hypotheses.
- Stress and mood are single-item self-reports, not validated clinical scales.
- Correlations are descriptive, not causal.
- ML demonstration uses independent synthetic rows; future repeated real-person observations need participant-grouped validation.
- Obtain appropriate consent and ethical review before collecting research data from others.

## Suggested CV description (only after personally testing and understanding the implementation)
Developed and evaluated an educational Python/Streamlit prototype for digital wellbeing tracking, behavioural analytics, and interpretable machine learning, with local SQLite storage, export/deletion controls, and explicit research-ethics limitations.
