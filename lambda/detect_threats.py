import json
from collections import defaultdict
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alerts')))

from send_alert import send_alert

# Configurable threshold
FAILURE_THRESHOLD = 3

def detect_failed_logins(logs):
    failure_counts = defaultdict(int)

    for log in logs:
        if log.get("event_type") == "login_failure":
            ip = log.get("ip")
            failure_counts[ip] += 1

    for ip, count in failure_counts.items():
        if count >= FAILURE_THRESHOLD:
            alert_msg = f"🚨 ALERT: {count} failed logins from {ip}"
            print(alert_msg)
            send_alert(alert_msg)

def detect_sudo_use(logs):
    for log in logs:
        if log.get("event_type") == "sudo_command":
            alert_msg = f"⚠️ SUDO alert: {log['user']} ran a sudo command from {log['ip']}"
            print(alert_msg)
            send_alert(alert_msg)

if __name__ == "__main__":
    LOG_FILE = "./cloud-log-monitoring/log_ingestion/security_logs.json"

    print(f"Opening log file: {LOG_FILE}")
    with open(LOG_FILE) as f:
        logs = json.load(f)

    print(f"Loaded {len(logs)} log entries")
    detect_failed_logins(logs)
    detect_sudo_use(logs)
    print("Detection complete.")
