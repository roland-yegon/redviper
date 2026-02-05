import platform
from utils.logger import log

def run(target):
    print(f"\n[Enumeration] Basic system/service fingerprinting for {target}")
    os_guess = platform.system()
    print(f"Local OS (for demo): {os_guess}")
    log(f"Enumeration OS guess: {os_guess}")
