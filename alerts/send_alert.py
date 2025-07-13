import os
import requests
from dotenv import load_dotenv

load_dotenv()
print("Slack webhook URL:", os.getenv("SLACK_WEBHOOK_URL"))
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_alert(message):
    if not SLACK_WEBHOOK_URL:
        print("❌ Slack webhook URL not found.")
        return

    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)

    if response.status_code == 200:
        print("✅ Alert sent successfully.")
    else:
        print(f"❌ Failed to send alert: {response.status_code} {response.text}")

if __name__ == "__main__":
    print("send_alert.py is running!")
    send_alert("🚨 Test alert from send_alert.py")
