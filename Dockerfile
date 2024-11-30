# Use an official Python runtime as the base image
FROM python:3.11-slim

# Install dependencies for OpenCV (including libGL.so.1)
RUN apt-get update && apt-get install -y \
    libglib2.0-0 libgthread-2.0-0
    
# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code to the container
COPY . .

# Expose the port your application runs on (if needed)
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
