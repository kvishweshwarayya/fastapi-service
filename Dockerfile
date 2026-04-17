# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code (main + api package)
COPY favicon.ico .
COPY main.py .
COPY routers ./routers

# Expose FastAPI port
EXPOSE 8080


# Run the app via main.py
# CMD ["python", "main.py"] <= it is always better to run app with uvicorn

# Run FastAPI app with Uvicorn directly
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
