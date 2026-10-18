"""Plain-language frozen model performance."""

import streamlit as st

from src.inference.ui import page_intro


st.set_page_config(page_title="Model Performance", page_icon="🧪", layout="wide")
page_intro("Model Performance", "Newer transaction records were used to evaluate how well the models performed on unseen data.")

rows = [
    ("HDB", "S$32,723", "S$46,304", "0.949"),
    ("Executive Condominium", "S$101,868", "S$138,187", "0.828"),
    ("Landed", "S$943,058", "S$2,659,602", "0.762"),
]
for name, mae, rmse, r2 in rows:
    st.subheader(name)
    a, b, c = st.columns(3)
    a.metric("MAE", mae)
    b.metric("RMSE", rmse)
    c.metric("R²", r2)

st.markdown(
    """
- **MAE** measures the average difference between predicted and actual property prices.
- **RMSE** is similar to MAE but gives more importance to larger errors.
- **R²** indicates how much of the variation in property prices is explained by the model.

All testing was chronological: models fitted older transactions and the test sets contained newer transactions. HDB uses a strictly lagged official HDB Resale Price Index and validated MRT distance. EC excludes MRT because it worsened validation performance. Landed excludes MRT because source locations were too imprecise, and its estimates are less precise because landed homes are highly heterogeneous.
"""
)
