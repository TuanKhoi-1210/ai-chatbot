import re
from typing import Dict, Pattern

RULES: Dict[str, str] = {
    "hello": "Xin chào! Tôi là chatbot của bạn",
    "hi": "Xin chào! Tôi là chatbot của bạn",
    "bye": "Tạm biệt, hẹn gặp lại!",
}

_PATTERNS: Dict[str, Pattern] = {
    k: re.compile(rf"\b{k}\b", flags=re.IGNORECASE) for k in RULES
}


def respond(user_text: str) -> str:
    text = user_text.strip()
    for key, pat in _PATTERNS.items():
        if pat.search(text):
            return RULES[key]
    return "Tôi chưa thông minh lắm, nhưng tôi sẽ học dần 😅"