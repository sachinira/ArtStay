from typing import List
from pydantic import BaseModel


class House(BaseModel):
    id: int
    name: str
    location: str
    contact_details: str
    facilities: List[str]
    price_per_night: float
    availability: bool


class Reservation(BaseModel):
    id: int
    house_id: int
    customer_name: str
    customer_contact: str
    check_in_date: str
    check_out_date: str
    total_price: float
    status: str


class Rental(BaseModel):
    id: int
    reservation_id: int
    bike_id: int
    rental_price: float
    status: str
