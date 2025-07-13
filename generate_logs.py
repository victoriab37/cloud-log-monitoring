import random, time, json
from datetime import datetime

users = ['alice', 'bob', 'eve']
events = ['login_success', 'login_failure', 'file_access', 'sudo_command']

def generate_log():
    return {
        'timestamp': datetime.utcnow().isoformat(),
        'user': random.choice(users),
        'event_type': random.choices(events, weights=[1, 3, 2, 1])[0],
        'ip': f"192.168.1.{random.randint(1, 255)}",
        'resource': random.choice(['/etc/passwd', '/home/alice/docs', '/var/log/syslog'])
    }

# Write logs to file
with open('security_logs.json', 'w') as f:
    for _ in range(100):
        json.dump(generate_log(), f)
        f.write('\n')
