from fastapi import FastAPI
from application.service import router

# Create an instance of the FastAPI application
app = FastAPI(version="1.0")

# Include the router from the service module
app.include_router(router)
