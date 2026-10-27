from pathlib import Path
import pickle
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "LinearRegressionModel.pkl"
DATA_PATH = BASE_DIR / "Cleaned_Car_data.csv"

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="centered")
st.title("🚗 Car Price Predictor")
st.caption("Estimate a used car's price from its details. Predictions are approximate, not professional valuations.")

@st.cache_resource
def load_model(path: str):
    with open(path, "rb") as model_file:
        return pickle.load(model_file)

@st.cache_data
def load_data(path: str):
    return pd.read_csv(path)

try:
    if not MODEL_PATH.is_file():
        st.error("Model file not found. Ensure LinearRegressionModel.pkl is uploaded in the same GitHub folder as app.py.")
        st.stop()
    if not DATA_PATH.is_file():
        st.error("Dataset not found. Ensure Cleaned_Car_data.csv is uploaded in the same GitHub folder as app.py.")
        st.stop()

    model = load_model(str(MODEL_PATH))
    car_data = load_data(str(DATA_PATH))
except ModuleNotFoundError as exc:
    st.error(f"A Python module needed to load the saved model is missing: {exc.name}. Check requirements.txt and redeploy.")
    st.stop()
except Exception as exc:
    st.error("The model or dataset could not be loaded. Check the Streamlit app logs for details.")
    st.caption(f"Diagnostic: {type(exc).__name__}: {exc}")
    st.stop()

required_columns = {"name", "company", "year", "kms_driven", "fuel_type"}
if not required_columns.issubset(car_data.columns):
    st.error("The dataset is missing one or more required columns: name, company, year, kms_driven, fuel_type.")
    st.stop()

companies = sorted(car_data["company"].dropna().unique().tolist())
if not companies:
    st.error("No car companies were found in the dataset.")
    st.stop()

company = st.selectbox("Select company", companies)
company_rows = car_data[car_data["company"] == company]
models = sorted(company_rows["name"].dropna().unique().tolist())
if not models:
    st.warning("No models were found for this company.")
    st.stop()
name = st.selectbox("Select car model", models)

year_min = int(pd.to_numeric(car_data["year"], errors="coerce").dropna().min())
year_max = max(2025, int(pd.to_numeric(car_data["year"], errors="coerce").dropna().max()))
year = st.number_input("Manufacturing year", min_value=year_min, max_value=year_max, step=1, value=min(2015, year_max))
kms_driven = st.number_input("Kilometers driven", min_value=0, max_value=1_000_000, step=1000, value=30_000)
fuel_types = sorted(car_data["fuel_type"].dropna().unique().tolist())
fuel_type = st.radio("Fuel type", fuel_types, horizontal=True)

if st.button("Predict price", type="primary", use_container_width=True):
    sample = pd.DataFrame(
        [[name, company, int(year), int(kms_driven), fuel_type]],
        columns=["name", "company", "year", "kms_driven", "fuel_type"],
    )
    try:
        prediction = float(model.predict(sample)[0])
        if not pd.notna(prediction):
            st.error("The model returned an invalid prediction. Please try different car details.")
        else:
            st.success(f"Estimated price: ₹ {max(0, round(prediction)):,}")
            st.caption("This estimate depends on the training data and may differ from actual market prices.")
    except Exception as exc:
        st.error("Prediction failed for these inputs. Check the app logs for details.")
        st.caption(f"Diagnostic: {type(exc).__name__}: {exc}")
