from typing import Dict

RULES: Dict[str, str] = {
    "hello": "Xin chào! Tôi là chatbot của bạn",
    "hi": "Xin chào! Tôi là chatbot của bạn",
    "bye": "Tạm biệt, hẹn gặp lại!",
}
def respond(user_text: str) -> str:
    text = user_text.lower()
    for key, val in RULES.items():
        if key in text:
            return val