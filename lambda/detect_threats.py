import json
import sys
import os
import logging
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'alerts')))
from send_alert import send_alert

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

FAILURE_THRESHOLD = 2
LOG_FILE = os.getenv("SECURITY_LOG_FILE", "./cloud-log-monitoring/security_logs.json")

def load_logs(filepath):
    try:
        with open(filepath) as f:
            logs = json.load(f)
        logging.info(f"Loaded {len(logs)} log entries from {filepath}")
        return logs
    except FileNotFoundError:
        logging.error(f"Log file not found: {filepath}")
        sys.exit(1)
    except json.JSONDecodeError:
        logging.error(f"Log file {filepath} is not valid JSON.")
        sys.exit(1)

def detect_failed_logins(logs, failure_threshold=FAILURE_THRESHOLD):
    failure_counts = defaultdict(int)
    failure_users = defaultdict(set)

    for log in logs:
        if not isinstance(log, dict):
            continue
        if log.get("event_type") == "login_failure" and "ip" in log:
            ip = log["ip"]
            failure_counts[ip] += 1
            user = log.get("user")
            if user:
                failure_users[ip].add(user)

    for ip, count in failure_counts.items():
        if count >= failure_threshold:
            users = ", ".join(failure_users[ip]) if failure_users[ip] else "Unknown users"
            alert_msg = (
                f"🚨 *Failed Login Alert*\n"
                f"*Count:* {count}\n"
                f"*IP:* {ip}\n"
                f"*Users:* {users}"
            )
            logging.warning(alert_msg.replace('\n', ' | '))
            send_alert(alert_msg)

def detect_sudo_use(logs):
    for log in logs:
        if not isinstance(log, dict):
            continue
        if log.get("event_type") == "sudo_command" and "user" in log and "ip" in log:
            alert_msg = (
                f"⚠️ *SUDO Alert*\n"
                f"*User:* {log['user']}\n"
                f"*IP:* {log['ip']}\n"
                f"Command: sudo"
            )
            logging.warning(alert_msg.replace('\n', ' | '))
            send_alert(alert_msg)

def run_detections(logs):
    detect_failed_logins(logs)
    detect_sudo_use(logs)

if __name__ == "__main__":
    logs = load_logs(LOG_FILE)
    run_detections(logs)
    logging.info("Detection complete.")
