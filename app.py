from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from chatbot.schemas import Message, ChatResponse
from chatbot.core import respond

app = FastAPI(title="AI Chatbot", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

@app.get("/", tags=["root"])
def home():
    return {"message": "Hello, AI chatbot is running!"}

@app.get("/healthz", tags=["ops"])
def healthz():
    return {"status": "ok"}

@app.get("/version", tags=["ops"])
def version():
    return {"version": app.version}


@app.post("/chat", response_model=ChatResponse, status_code=status.HTTP_200_OK, tags=["chat"])
def chat(msg: Message):
    logger.info("User said: {}", msg.text)
    reply = respond(msg.text)
    return ChatResponse(user=msg.text, bot=reply)