FROM ghcr.io/rwth-time/scystream-docker-selenium:latest

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "main"]
