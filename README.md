# NYC Evictions Shiny Dashboard

An interactive data dashboard analyzing **NYC eviction executions carried out by NYC Marshals (2017–2025)**.  
Built with **Python, Quarto, and Shiny**, and deployed as a **server-backed application** on Posit Connect Cloud.

---

## 🔗 Live Dashboard

👉 **View the interactive dashboard:**  
https://019b23c2-e6a2-a8d2-5863-12c506b45aad.share.connect.posit.cloud/

*(This is a live Shiny application — not a static report.)*

---

## 📊 Project Overview

This dashboard explores patterns and trends in NYC eviction executions, with an emphasis on clarity and public-sector relevance.

Key questions explored include:
- How eviction activity has changed over time
- Differences in eviction volume across boroughs
- Residential vs. commercial eviction composition
- Ejectment vs. non-ejectment cases
- Seasonal patterns in eviction activity
- Marshal activity patterns (names anonymized for privacy)

The goal is to make complex housing data **accessible, interpretable, and policy-relevant** for a non-technical audience.

---

## 🗂️ Data Source

- **NYC Open Data – Evictions Dataset**  
  https://data.cityofnewyork.us/City-Government/Evictions/6z8x-wfk4

> Note: The dashboard reflects the dataset as of the time of publication and does **not** live-update.

---

## 🛠️ Tech Stack & Libraries

**Languages & Frameworks**
- Python
- Shiny for Python
- Quarto Dashboards

**Data & Analysis**
- pandas
- NumPy

**Visualization**
- matplotlib
- Plotly

**Deployment**
- Posit Connect Cloud
- Git & GitHub for version control

---

## 🚀 Deployment Notes

- The dashboard is rendered locally with Quarto and compiled into a Shiny application (`app.py`)
- The Shiny app is deployed to **Posit Connect Cloud**, enabling full interactivity and server-side execution
- Marshal names are anonymized to protect privacy while preserving analytical value
