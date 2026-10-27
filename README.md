# Car Price Predictor 🚗

A machine learning web application that estimates the price of a used car based on its company, model, manufacturing year, kilometers driven, and fuel type.

The application uses Python and Streamlit to provide a simple interactive interface for entering car details and viewing an estimated price.

## Features

- Select a car company and available model.
- Enter the car's manufacturing year and kilometers driven.
- Select the fuel type.
- Generate an estimated used-car price using a trained machine learning model.
- View the prediction through an interactive web interface.

## Technologies Used

- **Python** — application logic
- **Pandas** — data loading and preparation
- **Scikit-learn** — machine learning prediction
- **Streamlit** — interactive web application
- **Pickle** — loading the saved model

## Project Files

- `app.py` — Streamlit application
- `LinearRegressionModel.pkl` — saved machine learning model
- `Cleaned_Car_data.csv` — cleaned dataset used by the application
- `predictor.ipynb` — Jupyter notebook for the prediction project
- `quikr_car.csv` — source dataset
- `requirements.txt` — Python dependencies

## How It Works

1. The application loads the cleaned car dataset and trained model.
2. The user selects the car details using the available input controls.
3. The selected details are passed to the model in the expected feature format.
4. The application displays the estimated car price.

## Run Locally

1. Clone this repository:

   ```bash
   git clone https://github.com/PreethuChandu/car-Price-Predictor.git
   cd car-Price-Predictor
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the Streamlit application:

   ```bash
   streamlit run app.py
   ```

## Limitations

This application provides an estimated price based on the data and model available in the project. It should not be treated as a professional vehicle valuation or a guaranteed market price.

## Project Type

Personal machine learning learning project.

**Note:** This project was developed with AI assistance as part of my machine learning learning journey.
