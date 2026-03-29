# Airline Passenger Demand Forecasting System

An end-to-end Machine Learning solution for long-term passenger traffic prediction. Developed with a focus on airline industry standards, specifically targeting high-precision forecasting for carriers like **Lufthansa**.

## Key Achievements
* **High Accuracy:** Achieved a **3.46% MAPE** on a 24-month recursive backtest (blind forecast).
* **Production-Ready:** Containerized architecture using Docker & Docker Compose.
* **Scalable Backend:** REST API built with FastAPI, ready for integration with frontend dashboards.

---

## System Architecture
The project follows a modern MLOps approach, separating data storage, model logic, and the serving layer.

1.  **Database:** PostgreSQL (running in Docker) stores historical SFO passenger traffic.
2.  **ML Engine:** XGBoost regressor with custom recursive forecasting logic.
3.  **API Layer:** FastAPI service providing high-performance inference endpoints.



---

## Tech Stack
* **Languages:** Python 3.10
* **ML Libraries:** XGBoost, Scikit-learn, Pandas, Statsmodels (SARIMA for baseline)
* **Database:** PostgreSQL + SQLAlchemy
* **API:** FastAPI + Pydantic + Uvicorn
* **DevOps:** Docker, Docker Compose

---

## Feature Engineering
To overcome the limitations of decision trees in time-series forecasting, the system generates:
* **Temporal Features:** Month, Quarter, Year (to capture seasonality).
* **Lags:** 1-month, 3-month, and **12-month** (critical for airline summer/winter cycles).
* **Moving Averages:** 3-month and 6-month rolling windows to capture trends.

---

## Model Evaluation (Backtesting)
The model was evaluated using a **Recursive Backtest** starting from Jan 2023 to prove long-term stability:
* **MAE:** ~151,976 passengers
* **RMSE:** ~193,394 passengers
* **MAPE:** **3.46%** (Average error over 2 years)

---

## Installation & Running
Ensure you have **Docker** and **Docker Compose** installed.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mapi-developer/Passenger-Demand-Forecasting.git](https://github.com/mapi-developer/Passenger-Demand-Forecasting.git)
   cd passenger-demand-forecast

2. **Launch the entire stack:**
    ```bash
    docker-compose up --build -d

3. **Test the API:**
    The API will be available at http://localhost:8000. 
    You can access the interactive Swagger documentation at http://localhost:8000/docs.

## API Example (Inference)
Send a POST request to /predict with the following JSON:
    ```json
    {
        "month": 7,
        "quarter": 3,
        "year": 2026,
        "lag_1M": 4500000,
        "lag_12M": 4450000,
        "rolling_mean_3M": 4300000,
        "pct_change_1M": 0.05
    }