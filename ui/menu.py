from core import recon, scanner, enumerator, vuln_scanner, exploit_lab, reporter

def post_action():
    """Ask user whether to continue or quit after a task."""
    while True:
        print("\nTask completed.")
        print("[1] Return to main menu")
        print("[0] Quit RedViper")

        choice = input("Select option: ")

        if choice == "1":
            return True
        elif choice == "0":
            print("Exiting RedViper...")
            return False
        else:
            print("Invalid input.")


def start_menu():
    running = True

    while running:
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
            running = post_action()

        elif choice == "2":
            target = input("Enter IP: ")
            scanner.run(target)
            running = post_action()

        elif choice == "3":
            target = input("Enter IP: ")
            enumerator.run(target)
            running = post_action()

        elif choice == "4":
            target = input("Enter IP or domain: ")
            vuln_scanner.run(target)
            running = post_action()

        elif choice == "5":
            exploit_lab.run()
            running = post_action()

        elif choice == "6":
            reporter.generate()
            running = post_action()

        elif choice == "0":
            print("Exiting RedViper...")
            break

        else:
            print("Invalid option.")
