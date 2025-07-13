# 🔐 Cloud Log Monitoring & Alerting System (Mini SIEM)

A cloud-native, lightweight security monitoring system that detects suspicious activity (e.g., brute force login attempts) using AWS services and Python. Alerts are triggered via Slack for investigation—mimicking a basic SIEM pipeline.

---

## 📌 Project Overview

| Category      | Info                                      |
|---------------|-------------------------------------------|
| **Type**      | Cybersecurity / Cloud Security Project    |
| **Built With**| Python, AWS (S3, Lambda, Slack) |
| **Skills**    | Log Analysis, Threat Detection, Alerting  |
| **Level**     | Entry to Intermediate                     |

---

## 🎯 Key Features

- ✅ Simulates security logs (e.g., failed logins, file access events)
- ✅ Pushes logs to **AWS S3** or **CloudWatch**
- ✅ AWS Lambda function scans logs for suspicious patterns
- ✅ Alerts sent to **Slack** or **Email (via SNS)**
- 🔜 Visualizations using **CloudWatch Dashboards** or **Splunk**

---

## 🧪 How It Works

1. **Simulate Logs**  
   `generate_logs.py` creates fake security event logs including login attempts, file access, and sudo commands.

2. **Ingest Logs**  
   Logs are pushed to **AWS S3** using the ingestion scripts.

3. **Detect Threats**  
   A Lambda function scans the logs to detect:
   - Multiple failed logins from the same IP
   - Access to sensitive files or suspicious commands

4. **Trigger Alerts**  
   Alerts are sent to Slack when thresholds are met.

5. **Visualize Logs**
   Visualize logs with dashboards using Splunk or CloudWatch to mimic a SOC environment.

---

## 📊 Example Alert Output

ALERT: Suspicious Activity Detected 🚨

IP: 192.168.1.245

Event: 7 failed login attempts

User: eve

Time: 2025-07-08T18:15:21Z
---

## 🧱 Technologies Used

- **Python 3.10+**
- **AWS Lambda (serverless detection)**
- **AWS S3 (log storage)**
- **Slack (alerting)**
- (Optional) **Splunk Free Tier** or **CloudWatch Dashboards**

📸 Screenshots
(Add your own screenshots below)

Simulated Logs	to S3
<img width="1662" height="467" alt="image" src="https://github.com/user-attachments/assets/c7e454a3-39fe-453a-bd6b-5b42ba72a7ef" />
<img width="797" height="670" alt="image" src="https://github.com/user-attachments/assets/1edc270b-719c-4734-9397-6945350222b8" />

Slack Alert
<img width="1137" height="596" alt="image" src="https://github.com/user-attachments/assets/86d11d77-01c1-45b4-ae76-30575fa647fc" />

📄 Project Status
✅ Version 1 complete – monitoring + alerting
🔜 In progress – adding Splunk integration + dashboard visualizations



💡 Inspiration
This project was built to demonstrate real-world security monitoring, log analysis, and threat detection workflows common in SOC Analyst and Cloud Security roles. It aligns with principles from the MITRE ATT&CK framework and SIEM pipelines.

📄 License
This project is licensed under the MIT License. You are free to use, modify, and share it.
