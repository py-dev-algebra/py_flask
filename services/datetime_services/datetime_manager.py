from datetime import datetime


def get_current_datetime() -> str:
    return datetime.now().strftime('%A, %d. %B, %Y. %H:%M:%S')