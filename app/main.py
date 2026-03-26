from fastapi import FastAPI
from pydantic import BaseModel
from .kafka_producer import send_message
from .kafka_admin import create_topic

app = FastAPI(
    title="Broker Service",
    description="Kafka broker wrapper for IoT streaming platform",
    version="0.1.0"
)


class Message(BaseModel):
    sensor_id: int
    temperature: float
    humidity: float
    timestamp: float


@app.on_event("startup")
def startup_event():
    create_topic()


@app.get("/health")
def health():
    return {"status": "ok", "message": "Broker service running"}


@app.post("/publish")
def publish_message(msg: Message):
    send_message(msg.dict())
    return {"status": "sent", "message": msg}
