from typing import List
from fastapi import HTTPException, APIRouter
from application.schema import House, Reservation, Rental

router = APIRouter()

# Database models (simulated with lists for simplicity)
houses_db = []
reservations_db = []
rentals_db = []


# House Endpoints
@router.post("/houses/")
def create_house(house: House):
    houses_db.append(house)
    return house


@router.get("/houses/", response_model=List[House])
def get_houses():
    return houses_db


@router.get("/houses/{id}")
def get_house(id: int):
    house = next((h for h in houses_db if h.id == id), None)
    if house is None:
        raise HTTPException(status_code=404, detail="House not found")
    return house


# Reservation Endpoints
@router.post("/reservations/")
def create_reservation(reservation: Reservation):
    reservations_db.append(reservation)
    return reservation


@router.get("/reservations/", response_model=List[Reservation])
def get_reservations():
    return reservations_db


@router.get("/reservations/{id}")
def get_reservation(id: int):
    reservation = next((r for r in reservations_db if r.id == id), None)
    if reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation


# Motorbike Rental Endpoints
@router.post("/rentals/")
def create_rental(rental: Rental):
    rentals_db.append(rental)
    return rental


@router.get("/rentals/", response_model=List[Rental])
def get_rentals():
    return rentals_db


@router.get("/rentals/{id}")
def get_rental(id: int):
    rental = next((r for r in rentals_db if r.id == id), None)
    if rental is None:
        raise HTTPException(status_code=404, detail="Rental not found")
    return rental
