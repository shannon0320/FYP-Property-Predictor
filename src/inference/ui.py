"""Small Streamlit helpers shared by the local application pages."""

from __future__ import annotations

from datetime import date
from typing import Any

import streamlit as st

from .predictor import PredictionResult, get_predictor
from .reference_data import load_market_summary, load_ui_reference


@st.cache_resource(show_spinner="Loading local prediction models…")
def app_predictor():
    return get_predictor()


@st.cache_data(show_spinner=False)
def app_references() -> dict[str, Any]:
    return load_ui_reference()


@st.cache_data(show_spinner=False)
def app_market_summary() -> dict[str, Any]:
    return load_market_summary()


def valuation_month_input(key: str) -> str:
    selected = st.date_input(
        "Valuation month",
        value=date.today().replace(day=1),
        help="The model uses the month and year; the day is ignored.",
        key=key,
    )
    return selected.strftime("%Y-%m")


def money(value: float) -> str:
    return f"S${value:,.0f}"


def show_prediction(result: PredictionResult) -> None:
    st.success("Estimate ready — calculated locally")
    st.caption("Estimated property value")
    st.markdown(f"## {money(result.predicted_price)}")
    st.markdown(
        f"**Estimated historical error range:**  "
        f"{money(result.range_lower)} – {money(result.range_upper)}"
    )
    st.caption(
        "The estimated range is based on the model's historical prediction performance "
        "and should be used as a reference only."
    )

    first, second = st.columns(2)
    first.metric("Model historical test MAE", money(result.model_test_mae))
    second.metric("Valuation month", result.valuation_month)

    if result.category == "hdb":
        mrt = result.references.get("nearest_mrt_station")
        distance = result.references.get("nearest_mrt_distance_m")
        if mrt and distance is not None:
            used = "used by model" if result.references.get("mrt_used_by_model") else "reference only"
            st.write(f"**Nearest MRT:** {mrt.title()} MRT — {distance:,.0f} m ({used})")
        else:
            st.write("**Nearest MRT:** unavailable locally; the model used its missing-MRT pathway")
        st.write(f"**Market index used:** HDB RPI {result.references['rpi_source_quarter']}")
    elif result.category == "ec":
        mrt = result.references.get("nearest_mrt_station")
        distance = result.references.get("nearest_mrt_distance_m")
        if mrt and distance is not None:
            st.write(f"**Nearest MRT (information only):** {str(mrt).title()} MRT — {distance:,.0f} m")
            st.caption("MRT distance is not an input to the frozen EC model.")

    for warning in result.warnings:
        st.warning(warning)
    if result.category == "landed":
        st.info(
            "Landed property estimates may have larger errors because individual homes differ in "
            "land size, condition and other property characteristics that are not included in the model."
        )

    with st.expander("Model details"):
        st.write(f"Model: {result.model_name}")
        st.write(f"Calibration band: {result.calibration_band}")
        st.write(f"P80 historical absolute error: {money(result.historical_error_amount)}")
        st.write("Derived inputs:", result.derived)
        for limitation in result.limitations:
            st.write(f"• {limitation}")


def page_intro(title: str, description: str) -> None:
    st.title(title)
    st.write(description)
    st.caption("Predictions are generated using trained models and supporting reference data.")
