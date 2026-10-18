"""Project scope and runtime methodology."""

import streamlit as st

from src.inference.ui import page_intro


st.set_page_config(page_title="About", page_icon="ℹ️", layout="wide")
page_intro("About / Methodology", "Summary of the datasets, models and limitations of the project.")

st.markdown(
    """
### Data and models

TThe estimates are based on HDB resale transactions, URA residential property transactions, the HDB Resale Price Index (RPI) and MRT-related location information. 

The application uses locally stored models and reference data to generate predictions and display supporting information.

### Scope choices

- A general private condominium prediction model was not included due to the limited amount of available transaction data.
- Rental prediction was not included as rental transaction data was not available.
- EC does not use MRT as a model feature because it worsened validation performance.
- Landed predictions cover one individual property, exclude portfolio transactions, and do not use MRT due to imprecise source locations.

### Important limitation

Predictions and historical error ranges are estimates from past transaction behavior. They are not professional valuations, guaranteed sale prices, offers, or financial advice. Property condition, renovations, views, exact plot characteristics and sudden market changes may not be represented.
"""
)
