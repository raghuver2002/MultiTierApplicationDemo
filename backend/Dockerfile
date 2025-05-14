FROM python:3.10-slim

# Install curl and clean up to reduce image size
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Continue with your existing setup
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
