# 🐍 RedViper — Modular Ethical Hacking Framework

RedViper is a **menu-driven penetration testing learning framework** built in Python.
It simulates the workflow used by real security professionals while maintaining a strong focus on **ethics, authorization, and safe lab usage**.

---

## ⚠️ Legal & Ethical Notice

This tool is for:

* Systems you own
* Lab environments
* Targets you have **explicit written permission** to test

Unauthorized use against real systems is illegal.

---

## 🎯 Purpose of the Project

RedViper is designed to:

* Teach penetration testing methodology
* Demonstrate tool architecture
* Practice automation and modular coding
* Serve as a cybersecurity portfolio project

It is **not** a hacking weapon.

---

## 🧠 Pentesting Phases Covered

| Phase                  | Module            | Description                       |
| ---------------------- | ----------------- | --------------------------------- |
| Reconnaissance         | `recon.py`        | Domain/IP information gathering   |
| Scanning               | `scanner.py`      | Basic port scanning               |
| Enumeration            | `enumerator.py`   | System/service fingerprint demo   |
| Vulnerability Analysis | `vuln_scanner.py` | Misconfiguration checks           |
| Exploit Simulation     | `exploit_lab.py`  | Safe post-exploitation simulation |
| Reporting              | `reporter.py`     | Log-based report generation       |

---

## 🏗 Project Structure

```
RedViper/
│
├── core/        # Security modules
├── ui/          # Menu interface
├── utils/       # Logging, banner, helpers
├── reports/     # Generated reports
├── main.py      # Entry point
└── README.md
```

---

## ▶️ Running RedViper

```bash
python3 main.py
```

You will see an interactive menu similar to classic CLI security tools.

---

## 📁 Reports

All generated reports are stored inside:

```
reports/
```

---

## 🛠 Technologies Used

* Python 3
* Socket programming
* HTTP requests
* Modular software design
* Logging systems

---

## 🚀 Future Improvements

* Nmap integration
* CVE API lookup
* Web vulnerability checks
* Report export to PDF
* Authentication testing modules

---

## 👨‍💻 Author

Roland Yegon
Aspiring Software & Security Engineer
GitHub: [https://github.com/roland-yegon](https://github.com/roland-yegon)

---

**RedViper — Learn security. Build tools. Stay ethical.**
