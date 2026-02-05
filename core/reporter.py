from datetime import datetime
import os

def generate():
    # Ensure reports directory exists
    os.makedirs("reports", exist_ok=True)

    report_path = f"reports/redviper_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    try:
        with open("logs/redviper.log", "r") as log_file:
            logs = log_file.read()
    except FileNotFoundError:
        logs = "No logs found."

    with open(report_path, "w") as report:
        report.write("RedViper Security Report\n")
        report.write(f"Generated: {datetime.now()}\n\n")
        report.write(logs)

    print(f"Report saved to {report_path}")
