def get_message(message):
    lower_message = message.lower()
    if(("join" in lower_message or "enter" in lower_message or "get" in lower_message) and ("queue" in lower_message or "raid" in lower_message)):
        return "read the pins <a:venopins:1057410756762673263>"
    return