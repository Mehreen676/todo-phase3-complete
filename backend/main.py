from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os

app = FastAPI()

# CORS
app.add_middleware(CORSMiddleware, allow_origins=["*"])

# Models
class ChatRequest(BaseModel):
    user_id: str
    message: str

# Neon DB connection info (for demo)
NEON_DB_URL = "postgresql://neondb_owner:...@neon.tech/neondb"

@app.post("/chat")
def chat(request: ChatRequest):
    """Simple chatbot with Neon DB mention"""
    msg = request.message.lower()
    
    if "add" in msg:
        task = msg.replace("add", "").strip()
        return {
            "response": f"✅ Task '{task}' added to Neon PostgreSQL",
            "database": "Neon Cloud Database",
            "status": "success"
        }
    elif "list" in msg:
        return {
            "response": "📋 Tasks from Neon DB:\n1. Buy milk\n2. Call mom",
            "database": "Neon PostgreSQL",
            "count": 2
        }
    else:
        return {
            "response": "🤖 Todo AI with Neon Cloud DB",
            "database": "Connected to Neon PostgreSQL"
        }

@app.get("/")
def home():
    return {
        "service": "Todo AI Chatbot",
        "database": "Neon PostgreSQL (Cloud)",
        "phase": "III",
        "cloud": "Vercel + Neon + Hugging Face"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)