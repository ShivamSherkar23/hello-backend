from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Demo API")


class MessageResponse(BaseModel):
    message: str
    timestamp: str
    server: str


@app.get("/api/hello", response_model=MessageResponse)
def hello():
    """A simple endpoint that returns a greeting."""
    return MessageResponse(
        message="Hello from FastAPI!",
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        server="FastAPI on port 8000",
    )
