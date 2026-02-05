from datetime import datetime

def generate():
    filename = "redviper_report.txt"
    with open("redviper.log", "r") as log_file:
        logs = log_file.read()

    with open(filename, "w") as report:
        report.write("RedViper Security Report\n")
        report.write(f"Generated: {datetime.now()}\n\n")
        report.write(logs)

    print(f"Report saved as {filename}")
