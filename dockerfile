FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Run setup file to create prometheus.yml
RUN python setup.py

# Expose port for debugging
EXPOSE 5678
