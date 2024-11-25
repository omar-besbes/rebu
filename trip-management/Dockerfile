# Use Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .

# Create and activate virtual environment, install dependencies
RUN python3 -m venv venv
RUN ./venv/bin/pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Command to run the app
CMD ["./venv/bin/uvicorn", "main:app", "--reload"]
