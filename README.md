# ✈️ Airline Passenger Demand Forecasting

An end-to-end machine learning pipeline and REST API for predicting airline passenger traffic. This project leverages multivariate time-series data to forecast regional and airline-specific demand, aiding in network planning and route optimization.

## 🎯 Business Objective
Accurate passenger demand forecasting is critical for airlines to optimize fleet allocation, manage crew schedules, and maximize route profitability. This project demonstrates a production-ready approach to predicting monthly passenger volumes using historical traffic data, temporal features, and machine learning.

## 📊 Dataset
This project uses the **San Francisco International Airport (SFO) Monthly Passenger Traffic** dataset. 
* **Granularity:** Monthly
* **Features:** Operating Airline, GEO Region (Domestic/International), Activity Type (Enplaned/Deplaned), and Price Category.
* **Complexity:** The dataset requires careful ETL handling as passenger counts are additive across multiple categorical dimensions.

## 🛠️ Tech Stack
* **Data Engineering:** `pandas`, `SQLAlchemy`, `PostgreSQL` (Data ingestion & transformation)
* **Machine Learning:** `scikit-learn`, `XGBoost`, `statsmodels` (SARIMA baseline)
* **Backend API:** `FastAPI`, `Uvicorn`, `Pydantic`
* **Deployment:** `Docker`, Google Cloud Platform (GCP)

## 📁 Project Structure

```text
passenger-demand-forecast/
├── data/                      # Local data storage (raw and processed)
├── notebooks/                 # Jupyter notebooks for EDA and model prototyping
├── src/                       
│   ├── api/                   # FastAPI application (main.py, routes, schemas)
│   ├── db/                    # PostgreSQL configuration and SQLAlchemy models
│   ├── etl/                   # Data extraction and transformation pipelines
│   └── ml/                    # Machine learning training and inference scripts
├── models/                    # Saved model artifacts (.joblib)
├── tests/                     # Pytest unit tests
├── Dockerfile                 # Containerization setup
└── requirements.txt           # Python dependencies