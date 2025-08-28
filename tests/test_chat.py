from chatbot.core import respond

def test_greeting():
    reply = respond("hello")
    assert "Xin chào" in reply

def test_bye():
    reply = respond("bye")
    assert "Tạm biệt" in reply

def test_unknown():
    reply = respond("something random")
    assert "chưa thông minh" in reply