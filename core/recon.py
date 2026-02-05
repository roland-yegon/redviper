import socket
import requests
from utils.logger import log

def run(target):
    print(f"\n[Recon] Gathering info for {target}")
    try:
        ip = socket.gethostbyname(target)
        print(f"IP Address: {ip}")
        log(f"Recon IP resolved: {ip}")

        response = requests.get(f"http://{target}", timeout=5)
        print(f"HTTP Status: {response.status_code}")
        log(f"Recon HTTP status: {response.status_code}")

    except Exception as e:
        print("Recon error:", e)
        log(f"Recon error: {e}")
