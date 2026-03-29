from sqlalchemy import Column, Integer, String, Date
from .database import Base

class PassengerTraffic(Base):
    __tablename__ = 'passenger_traffic'

    id = Column(Integer, primary_key=True, index=True)

    activity_period = Column(Integer, index=True)
    activity_period_start_date = Column(Date, index=True)

    operating_airline = Column(String, index=True)
    geo_summary = Column(String)
    geo_region = Column(String, index=True)
    activity_type_code = Column(String)
    price_category_code = Column(String)

    passenger_count = Column(Integer)