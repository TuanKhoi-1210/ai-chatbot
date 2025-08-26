from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

# Endpoint GET / (truy cập địa chỉ gốc của server)
# Khi gõ http://127.0.0.1:8000/ thì sẽ trả về JSON như dưới
@app.get("/")
def home():
    return {"message": "Hello, AI chatbot is running!"}


# Endpoint POST /chat (dùng để chat với bot)
# Client sẽ gửi JSON dạng {"text": "Hello"} lên server
@app.post("/chat")
def chat(msg: Message):
    
    user_text = msg.text.lower()

    # Chatbot rule-based (trả lời cứng theo điều kiện)
    if "hello" in user_text or "hi" in user_text:
        reply = "Xin chào! Tôi là chatbot của bạn 🤖"
    elif "bye" in user_text:
        reply = "Tạm biệt, hẹn gặp lại!"
    else:
        reply = "Tôi chưa thông minh lắm, nhưng tôi sẽ học dần 😅"
        # Trả về JSON gồm: nội dung user gửi + câu trả lời của bot
    return {"user": msg.text, "bot": reply}