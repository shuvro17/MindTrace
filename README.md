# MindTrace
### A Privacy-Aware Digital Wellbeing & Behavioural Analytics Platform

**Interdisciplinary Academic Research and Software Development Project**

**Developed by:** Tanvir Rahman Shuvro  
**Department:** Computer Science and Engineering  
**Institution:** Daffodil International University, Bangladesh  
**Proposed Academic Supervisor:** Mr. Saiful Islam, Assistant Professor  
**Initial Development:** Spring 2025  
**GitHub Publication:** 13 October 2026

---

## 1. Project Overview

**MindTrace** is a privacy-aware digital wellbeing analytics platform developed using Python and Streamlit. It explores computational approaches to understanding relationships between digital media usage, sleep patterns, emotional wellbeing, and self-reported psychological stress.

The project integrates **Computer Science, Behavioural Data Science, Human–Computer Interaction (HCI), Machine Learning, and Digital Health** into a single interactive research-oriented application.

MindTrace demonstrates how digital technologies can support behavioural data collection, statistical exploration, interactive visualization, and interpretable machine learning while emphasizing responsible data management and research ethics.

> **Disclaimer:** MindTrace is an educational and research-oriented software prototype. It is not a medical device, diagnostic system, or therapeutic application. Demonstration data are synthetically generated and do not constitute empirical research findings.

---

## 2. Project Information

| Information | Details |
|---|---|
| **Project Title** | MindTrace: A Privacy-Aware Digital Wellbeing Analytics Platform |
| **Project Type** | Academic Research and Software Development |
| **Researcher & Developer** | Tanvir Rahman Shuvro |
| **Department** | Computer Science and Engineering |
| **University** | Daffodil International University |
| **Academic Supervisor (Proposed)** | Mr. Saiful Islam |
| **Supervisor's Designation** | Assistant Professor |
| **Faculty** | Faculty of Science and Information Technology |
| **Initial Development Period** | Spring 2025 |
| **GitHub Publication Date** | 13 October 2026 |
| **Programming Language** | Python |
| **Project Status** | Educational Research Prototype |

---

## 3. Abstract

The increasing integration of digital technologies into everyday life has created opportunities to investigate relationships between technology usage and psychological wellbeing. Digital behaviours, including screen time, social media engagement, and late-night device usage, may be associated with sleep patterns, emotional states, and perceived stress.

MindTrace was developed as an interdisciplinary software prototype to demonstrate how behavioural information can be collected, processed, visualized, and analysed using computational methods.

The system integrates daily self-report tracking, interactive behavioural dashboards, Spearman rank correlation analysis, and interpretable machine learning demonstrations. A local SQLite database supports data storage, CSV export, and deletion.

The current implementation uses synthetic demonstration data to illustrate analytical workflows. Therefore, the project does not establish causal relationships, validate psychological hypotheses, or provide clinical assessments.

---

## 4. Research Objectives

The primary objective of MindTrace is to demonstrate a computational framework for exploring digital behaviour and self-reported psychological wellbeing.

Specific objectives include:

1. Develop an interactive platform for recording digital media usage, sleep duration, mood, and perceived stress.
2. Implement a structured data-processing workflow for behavioural information.
3. Explore statistical associations between digital habits and wellbeing indicators.
4. Demonstrate interpretable machine learning for behavioural data classification.
5. Integrate privacy-aware local storage and user-controlled data management.
6. Examine the ethical and methodological limitations of computational approaches to digital mental health research.

---

## 5. Research Questions

The project is organized around three exploratory research questions:

**RQ1:** What associations can be examined between self-reported digital media usage, sleep patterns, and perceived stress?

**RQ2:** How can statistical analysis and interpretable machine learning support the exploration of behavioural patterns in digital wellbeing data?

**RQ3:** How can privacy-aware software design support responsible collection, processing, and management of sensitive behavioural information?

These questions establish the project's research direction. The current synthetic-data implementation is designed to demonstrate analytical methods rather than provide empirical answers.

---

## 6. Key Features

### 6.1 Daily Behavioural Tracking

- Record daily screen time and digital media habits.
- Document sleep duration and self-reported mood.
- Track perceived stress through daily check-in questions.
- Store entries in a local SQLite database.

### 6.2 Interactive Analytics Dashboard

- Visualize behavioural indicators and trends.
- Explore relationships between digital habits and wellbeing.
- Review descriptive statistics and interactive charts.

### 6.3 Statistical Analysis

- Calculate Spearman rank correlations.
- Examine associations between numerical behavioural variables.
- Present results with appropriate methodological limitations.

### 6.4 Machine Learning Demonstration

- Train a Random Forest classification model using synthetic demonstration data.
- Compare model performance against a majority-class baseline.
- Visualize feature importance.
- Demonstrate predictive modelling and evaluation principles.

### 6.5 Privacy-Aware Data Management

- Store personal entries locally.
- Export available records in CSV format.
- Delete locally stored entries.
- Avoid requiring external cloud storage for basic operation.

---

## 7. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming and data processing |
| Streamlit | Interactive web application |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computation |
| Plotly | Interactive data visualization |
| SciPy | Statistical analysis |
| scikit-learn | Machine learning and model evaluation |
| SQLite | Local database storage |
| Git and GitHub | Version control and source code hosting |

---

## 8. System Architecture

MindTrace follows a simplified behavioural data-processing workflow:

```text
                 USER
                   |
                   v
          STREAMLIT INTERFACE
                   |
                   v
        DATA INPUT & VALIDATION
                   |
                   v
          LOCAL SQLITE DATABASE
                   |
                   v
           DATA PROCESSING
                   |
          +--------+--------+
          |                 |
          v                 v
   STATISTICAL         MACHINE LEARNING
     ANALYSIS            DEMONSTRATION
          |                 |
          +--------+--------+
                   |
                   v
       INTERACTIVE VISUALIZATION
                   |
                   v
       BEHAVIOURAL DATA INSIGHTS
```

The application contains five major components:

1. **User Interface:** Streamlit-based dashboard and daily check-in forms.
2. **Data Management:** SQLite storage and CSV export functionality.
3. **Analytics:** Descriptive statistics and Spearman correlation analysis.
4. **Machine Learning:** Random Forest demonstration and baseline comparison.
5. **Visualization:** Interactive behavioural charts and model explanations.

---

## 9. Installation and Setup

### 9.1 Prerequisites

- Windows 10 or Windows 11
- Python 3.11 or Python 3.12
- pip package manager
- Visual Studio Code or another Python-compatible editor

### 9.2 Clone the Repository

Open PowerShell or the VS Code terminal:

```powershell
git clone https://github.com/YOUR_USERNAME/MindTrace-Digital-Wellbeing.git
cd MindTrace-Digital-Wellbeing
```

Replace `YOUR_USERNAME` with your GitHub username.

Alternatively, download the repository as a ZIP file and extract it.

### 9.3 Create a Virtual Environment

```powershell
py -3.11 -m venv .venv
```

### 9.4 Install Dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 9.5 Run the Application

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

### 9.6 Access the Dashboard

After launching the application, open:

http://localhost:8501

The MindTrace dashboard should appear in your browser.

---

## 10. Project Directory Structure

```text
MindTrace/
|
|-- app.py                 # Main Streamlit application
|-- requirements.txt       # Python dependencies
|-- README.md              # Project documentation
|-- .gitignore             # Git exclusion rules
|-- .venv/                 # Local virtual environment (not committed)
|-- mindtrace.db           # Generated SQLite database (not committed)
```

The local virtual environment and generated database should not be committed to GitHub.

---

## 11. Research Methodology

MindTrace currently follows a demonstration-oriented computational methodology.

### Phase 1: Data Generation and Collection

Synthetic behavioural records are generated for software demonstration. Users can also enter daily check-in information into the local application.

### Phase 2: Data Processing

Behavioural variables are structured and processed, including screen time, sleep duration, mood, and perceived stress.

### Phase 3: Statistical Analysis

Spearman rank correlation analysis is used to examine monotonic associations between selected numerical behavioural variables.

### Phase 4: Machine Learning

A Random Forest classifier demonstrates behavioural feature modelling. Its performance is compared against a majority-class baseline.

### Phase 5: Visualization and Interpretation

Interactive charts communicate behavioural patterns and model outputs, accompanied by explanations of the limitations of synthetic data.

---

## 12. Research Ethics and Limitations

MindTrace emphasizes responsible computing and research integrity.

- **Synthetic Data:** Demonstration records are artificially generated and cannot validate real-world psychological hypotheses.
- **Non-Clinical Measurements:** Mood and stress are recorded through simple self-report indicators rather than validated diagnostic instruments.
- **Correlation vs. Causation:** Statistical associations do not establish causal relationships.
- **Model Generalizability:** Performance on synthetic data does not demonstrate effectiveness with real-world users.
- **Privacy:** Local storage reduces reliance on external services but does not guarantee data security.
- **Human-Participant Research:** Appropriate informed consent, ethical review, and additional safeguards would be required before conducting formal research involving human participants.
- **Repeated Observations:** Future datasets containing multiple records from the same participant would require participant-grouped model validation to reduce data leakage.

MindTrace must not be used for clinical diagnosis, psychological treatment, or medical decision-making.

---

## 13. Academic Supervision

**Proposed Academic Supervisor:**

**Mr. Saiful Islam**  
Assistant Professor  
Department of Computer Science and Engineering  
Faculty of Science and Information Technology  
Daffodil International University, Bangladesh

**Email:** [saiful.cse@diu.edu.bd](mailto:saiful.cse@diu.edu.bd)  
**Faculty Profile:** [Official DIU Faculty Profile](https://faculty.daffodilvarsity.edu.bd/profile/cse/saiful-islam.html)

**Supervision Status:** Pending confirmation

The proposed academic supervision would focus on research methodology, computational implementation, behavioural data analysis, and ethical considerations related to digital wellbeing technologies.

---

## 14. Academic Relevance

MindTrace connects several interdisciplinary research areas:

- **Computer Science:** Software engineering, databases, and data processing.
- **Artificial Intelligence:** Interpretable machine learning and model evaluation.
- **Behavioural Science:** Digital habits, emotional wellbeing, and perceived stress.
- **Human–Computer Interaction:** User-centred digital wellbeing interfaces.
- **Digital Health:** Responsible collection and analysis of wellbeing-related information.
- **Research Ethics:** Privacy, informed consent, and methodological transparency.

The project is particularly relevant to postgraduate study involving cyberspace behaviour, e-health, behavioural measurement, and computational approaches to human wellbeing.

---

## 15. Future Development

Planned improvements include:

1. Integrating validated psychological assessment instruments where appropriate.
2. Conducting an ethically approved usability study.
3. Developing participant-level longitudinal data analysis.
4. Expanding interpretable machine learning and model evaluation.
5. Improving accessibility and user-centred interface design.
6. Exploring privacy-preserving behavioural data-processing methods.
7. Preparing a scientific research poster or academic manuscript based on appropriately collected evidence.

---

## 16. Project Timeline

| Milestone | Date |
|---|---|
| Initial project development | Spring 2025 |
| GitHub repository publication | 13 October 2026 |
| Future research and improvements | Planned |

---

## 17. Author and Developer

**Tanvir Rahman Shuvro**  
BSc in Computer Science and Engineering  
Department of Computer Science and Engineering  
Daffodil International University, Bangladesh

**Project Role:** Student Researcher, Software Developer and Data Analyst

**Research Interests:**
- Artificial Intelligence and Machine Learning
- Human–Computer Interaction
- Behavioural Data Science
- Digital Health and E-Health Technologies
- Privacy-Aware Software Development

---

### MindTrace — Exploring Digital Behaviour Through Responsible Computing

*Developed by Tanvir Rahman Shuvro as an interdisciplinary educational and research-oriented software project.*