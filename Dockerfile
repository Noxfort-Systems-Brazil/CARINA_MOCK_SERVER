# CARINA Mock Server - Production Container Image
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    MOCK_SERVER_HOST=0.0.0.0 \
    MOCK_SERVER_PORT=50051 \
    MOCK_SERVER_NO_GUI=1

WORKDIR /app

# Install minimal system dependencies for curl (healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install production Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy server source code and map networks
COPY proto/ ./proto/
COPY src/ ./src/
COPY ui/ ./ui/
COPY data/ ./data/
COPY main.py .

# Create directory for persisting received maps
RUN mkdir -p /app/data/maps

EXPOSE 50051

HEALTHCHECK --interval=15s --timeout=5s --start-period=5s --retries=3 \
  CMD python -c "import socket; s = socket.socket(); s.connect(('127.0.0.1', 50051)); s.close()" || exit 1

ENTRYPOINT ["python", "main.py", "--no-gui"]
