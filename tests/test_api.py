from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json()["message"] == "Hello, AI chatbot is running!"

def test_chat_greeting():
    res = client.post("/chat", json={"text": "hello"})
    assert res.status_code == 200
    data = res.json()
    assert data["user"] == "hello"
    assert "Xin chào" in data["bot"]

def test_chat_fallback():
    res = client.post("/chat", json={"text": "something random"})
    assert res.status_code == 200
    data = res.json()
    assert "chưa thông minh" in data["bot"]
