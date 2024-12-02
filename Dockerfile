# Use an official Python runtime as the base image
FROM docker.io/python:3.11-slim

# Install dependencies for OpenCV (including libGL.so.1)
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install\
    libgl1\
    libgl1-mesa-glx \ 
    libglib2.0-0 -y && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code to the container
COPY ./main.py /app/main.py
COPY ./utils/my_module.py /app/utils/my_module.py
COPY ./utils/__init__.py /app/utils/__init__.py
COPY ./utils/best.pt /app/utils/best.pt


# Expose the port your application runs on (if needed)
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]