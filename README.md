# broker-service

A lightweight Kafka wrapper service for the Spark IoT Platform.

## Features

- Creates Kafka topic on startup
- Provides a REST endpoint to publish test messages
- Used as the ingestion layer for sensor-service and spark-streaming

## Endpoints

### Health check

```bash
GET /health
```

### Publish a message

```bash
POST /publish
{
"sensor_id": 1,
"temperature": 22.5,
"humidity": 55.0,
"timestamp": 1710000000.0
}
```


## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 9000
```

## Docker

```bash
docker build -t broker-service .
docker run -p 9000:9000 broker-service
```
