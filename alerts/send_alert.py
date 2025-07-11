import requests

def send_alert(message):
    webhook_url = 'https://hooks.slack.com/services/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'
    payload = {"text": message}

    response = requests.post(webhook_url, json=payload)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
    else:
        print("✅ Alert sent successfully!")

if __name__ == "__main__":
    send_alert("🚨 Test alert from my mini SIEM!")