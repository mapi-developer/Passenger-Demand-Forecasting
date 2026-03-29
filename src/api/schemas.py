from pydantic import BaseModel, Field


class PassengerForecastRequest(BaseModel):
    month: int = Field(..., ge=1, le=12, description='Month of the year')
    quarter: int = Field(..., ge=1, le=4, description='Quarter of the Year')
    year: int = Field(..., ge=2000, description='Year of prediction')

    lag_1M: float = Field(..., description='Passengers 1 month ago')
    lag_3M: float = Field(..., description='Passengers 3 month ago')
    lag_12M: float = Field(..., description='Passengers 12 month ago')
    rolling_mean_3M: float = Field(..., description='Average passengers over last 3 months')
    rolling_mean_6M: float = Field(..., description='Average passengers over last 6 months')
    pct_change_1M: float = Field(..., description="Percentage change from previous month")


class PassengerForecastResponse(BaseModel):
    predicted_passengers: int