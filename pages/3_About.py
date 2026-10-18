"""Project scope and runtime methodology."""

import streamlit as st

from src.inference.ui import page_intro


st.set_page_config(page_title="About", page_icon="ℹ️", layout="wide")
page_intro("About / Methodology", "Summary of the datasets, models and limitations of the project.")

st.markdown(
    """
### Data and models

TThe estimates are based on HDB resale transactions, URA residential property transactions, the HDB Resale Price Index (RPI) and MRT-related location information. 

At runtime, models, RPI values, form options, address matches and MRT distances are all loaded locally. The app makes no live OneMap request and needs no API token.

### Scope choices

- A general private-condominium predictor is omitted because the supplied private dataset contained only 117 rows across five projects and four districts.
- Rental prediction is omitted because no rental transaction data was supplied.
- EC does not use MRT as a model feature because it worsened validation performance.
- Landed predictions cover one individual property, exclude portfolio transactions, and do not use MRT due to imprecise source locations.

### Important limitation

Predictions and historical error ranges are estimates from past transaction behavior. They are not professional valuations, guaranteed sale prices, offers, or financial advice. Property condition, renovations, views, exact plot characteristics and sudden market changes may not be represented.
"""
)
