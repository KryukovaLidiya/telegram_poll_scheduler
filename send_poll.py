import os
import json
import sys
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

TOKEN   = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_poll():
    url = f"https://api.telegram.org/bot{TOKEN}/sendPoll"
    data = {
        "chat_id": CHAT_ID,
        "question": os.getenv("POLL_QUESTION", "Test"),
        "options": json.dumps(
            json.loads(
                os.getenv("POLL_OPTIONS", '["A","B","C"]')
            )
        ),
        "is_anonymous": os.getenv("POLL_ANONYMOUS", "False").lower() in ("true", "1"),
        "allows_multiple_answers": os.getenv("POLL_MULTIPLE", "False").lower() in ("true", "1")
    }
    resp = requests.post(url, data=data)
    print("Status:", resp.status_code, resp.text)

if __name__ == "__main__":
    send_poll()
    sys.exit(0)
