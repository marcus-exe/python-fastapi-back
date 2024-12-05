FROM docker.io/python:3.11-slim

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install\
    libgl1\
    libgl1-mesa-glx \ 
    libglib2.0-0 -y && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./main.py /app/main.py
COPY ./utils/my_module.py /app/utils/my_module.py
COPY ./utils/__init__.py /app/utils/__init__.py
COPY ./utils/best.pt /app/utils/best.pt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]