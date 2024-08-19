# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

USER 10016

# Make port 8000 available to the world outside this container
EXPOSE 8080

# Define environment variable for Uvicorn
ENV HOST 0.0.0.0
ENV PORT 8080

# Run app.py when the container launches
CMD ["uvicorn", "application.main:app", "--host", "0.0.0.0", "--port", "8080"]
