from pathlib import Path
import pandas as pd

from shiny import App, ui, render

# Paths (data folders live inside quarto_dashboard for deployment)
APP_DIR = Path(__file__).resolve().parent
DATA_CLEAN_DIR = APP_DIR / "data_clean"
DATA_FINAL_DIR = APP_DIR / "data_final"

evictions_clean = pd.read_csv(DATA_CLEAN_DIR / "evictions_clean.csv", parse_dates=["executed_date"])
evictions_by_month = pd.read_csv(DATA_FINAL_DIR / "evictions_by_month.csv")
evictions_by_borough = pd.read_csv(DATA_FINAL_DIR / "evictions_by_borough.csv")

app_ui = ui.page_fluid(
    ui.h2("NYC Evictions Dashboard (Shiny for Python)"),
    ui.p(f"Loaded evictions_clean: {len(evictions_clean):,} rows"),
    ui.p(f"Loaded evictions_by_month: {len(evictions_by_month):,} rows"),
    ui.p(f"Loaded evictions_by_borough: {len(evictions_by_borough):,} rows"),
)

def server(input, output, session):
    pass

app = App(app_ui, server)
