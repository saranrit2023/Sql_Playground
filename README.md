📜 README.md
# SQL Injection Playground with Real-Time Detection

An intentionally vulnerable web app designed to demonstrate SQL Injection (SQLi) and a Python-based engine to detect attacks in real time.

## 🎓 Features
- ❌ Vulnerable login page (raw SQL)
- ✅ Safe login page (parameterized queries)
- ⚡ Real-time attack detection
- 🔍 SQLi simulation via Python script
- ✉ Logs attacks with timestamps and payloads

## 📊 Technologies
- Python, Flask
- SQLite
- HTML/CSS
- Python Requests

## 🔧 Installation
```bash

cd Sql_playground
🔄 Run the App
python run.py
Visit http://127.0.0.1:5000
🚨 Launch the Detector
python sqli_detector.py
🔍 Key Routes
•	/ - Vulnerable login
•	/safe - Safe login (parameterized)
•	/init - Reset DB
•	/logs - View logs

