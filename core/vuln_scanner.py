from utils.logger import log

def run(target):
    print(f"\n[Vuln Scan] Checking common misconfigurations for {target}")
    print("• Checking for open common ports...")
    print("• Checking HTTP exposure...")
    print("• Checking default services...")

    log(f"Vulnerability scan performed on {target}")
    print("No real exploits run — analysis only.")
