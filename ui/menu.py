from core import recon, scanner, enumerator, vuln_scanner, exploit_lab, reporter

def start_menu():
    while True:
        print("\n===== RedViper Menu =====")
        print("[1] Reconnaissance")
        print("[2] Port Scanning")
        print("[3] Enumeration")
        print("[4] Vulnerability Scan")
        print("[5] Exploit Lab Simulator")
        print("[6] Generate Report")
        print("[0] Exit")

        choice = input("Select option: ")

        if choice == "1":
            target = input("Enter domain or IP: ")
            recon.run(target)
        elif choice == "2":
            target = input("Enter IP: ")
            scanner.run(target)
        elif choice == "3":
            target = input("Enter IP: ")
            enumerator.run(target)
        elif choice == "4":
            target = input("Enter IP or domain: ")
            vuln_scanner.run(target)
        elif choice == "5":
            exploit_lab.run()
        elif choice == "6":
            reporter.generate()
        elif choice == "0":
            print("Exiting RedViper...")
            break
        else:
            print("Invalid option.")
