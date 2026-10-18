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

The models were evaluated using newer transaction records that were not included during training. Different input variables were used for each property category. For example, the HDB model incorporated market indicators and MRT accessibility information, while the EC and landed models used feature sets that were found to be more suitable for their respective datasets.
"""
)
