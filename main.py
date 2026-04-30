from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Demo API")

# Allow requests from the React frontend (running on port 5173 or 3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class MessageResponse(BaseModel):
    message: str
    timestamp: str
    server: str


@app.get("/api/hello", response_model=MessageResponse)
def hello():
    """A simple endpoint that returns a greeting."""
    return MessageResponse(
        message="Hello from FastAPI! 🚀",
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        server="FastAPI on port 8000",
    )
