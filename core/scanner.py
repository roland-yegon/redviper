import socket
from utils.logger import log

def run(target):
    print(f"\n[Scan] Scanning ports on {target}")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443]
    
    for port in common_ports:
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((target, port))
            print(f"Port {port} OPEN")
            log(f"Port open: {port}")
            s.close()
        except:
            pass
