# 🔐 Cloud Log Monitoring & Alerting System (Mini SIEM)

A cloud-native, lightweight security monitoring system that detects suspicious activity (e.g., brute force login attempts, unauthorized file access) using AWS services and Python. Alerts are triggered via Slack or email for investigation—mimicking a basic SIEM pipeline.

---

## 📌 Project Overview

| Category      | Info                                      |
|---------------|-------------------------------------------|
| **Type**      | Cybersecurity / Cloud Security Project    |
| **Built With**| Python, AWS (S3, CloudWatch, Lambda, SNS) |
| **Skills**    | Log Analysis, Threat Detection, Alerting  |
| **Level**     | Entry to Intermediate                     |

---

## 🎯 Key Features

- ✅ Simulates security logs (e.g., failed logins, file access events)
- ✅ Pushes logs to **AWS S3** or **CloudWatch**
- ✅ AWS Lambda function scans logs for suspicious patterns
- ✅ Alerts sent to **Slack** or **Email (via SNS)**
- ✅ (Optional) Visualizations using **CloudWatch Dashboards** or **Splunk**

---

## 📁 Folder Structure

cloud-log-monitoring/
├── README.md
├── generate_logs.py # Log simulator
├── log_ingestion/
│ ├── push_to_s3.py
│ └── push_to_cloudwatch.py
├── lambda/
│ └── detect_threats.py
├── alerts/
│ └── send_alert.py
├── screenshots/ # Output + UI examples
└── architecture.png # Optional diagram

---

## 🧪 How It Works

1. **Simulate Logs**  
   `generate_logs.py` creates fake security event logs including login attempts, file access, and sudo commands.

2. **Ingest Logs**  
   Logs are pushed to either **AWS S3** or **CloudWatch Logs** using the ingestion scripts.

3. **Detect Threats**  
   A Lambda function scans the logs to detect:
   - Multiple failed logins from the same IP
   - Access to sensitive files or suspicious commands

4. **Trigger Alerts**  
   Alerts are sent to Slack or via SNS email when thresholds are met.

5. **Visualize Logs**
   Visualize logs with dashboards using Splunk or CloudWatch to mimic a SOC environment.

---

## 📊 Example Alert Output

ALERT: Suspicious Activity Detected 🚨

IP: 192.168.1.245

Event: 7 failed login attempts in 1 minute

User: eve

Time: 2025-07-08T18:15:21Z
---

## 🧱 Technologies Used

- **Python 3.10+**
- **AWS CloudWatch Logs**
- **AWS Lambda (serverless detection)**
- **AWS S3 (log storage)**
- **AWS SNS / Slack (alerting)**
- (Optional) **Splunk Free Tier** or **CloudWatch Dashboards**

📸 Screenshots
(Add your own screenshots below)

Simulated Logs	CloudWatch Logs	Slack Alert

📐 Architecture Diagram
(Optional: Add your own diagram here)


📄 Project Status
✅ Version 1 complete – monitoring + alerting
🔜 In progress – adding Splunk integration + dashboard visualizations



💡 Inspiration
This project was built to demonstrate real-world security monitoring, log analysis, and threat detection workflows common in SOC Analyst and Cloud Security roles. It aligns with principles from the MITRE ATT&CK framework and SIEM pipelines.

📄 License
This project is licensed under the MIT License. You are free to use, modify, and share it.
