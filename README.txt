HARDEN-SEC

HARDEN-SEC is a Python-based security auditing tool for Linux systems. It automates the detection of common misconfigurations, evaluates system risk, and generates professional reports in multiple formats. It is designed for learning, lab environments, and as a starting point for practical Linux hardening.

Features

Audits critical system files (/etc/passwd, /etc/shadow) for insecure permissions.

Detects non-root users with UID 0.

Identifies insecure running services (telnet, FTP, rsh, etc.).

Checks SSH configuration for weak settings (password authentication, root login, protocol version).

Calculates a global security score and risk level.

Generates reports in TXT, JSON, and HTML formats.

JSON reports can be imported into SIEM platforms (Splunk, ELK, Graylog, Wazuh) for alerts, dashboards, and analytics.

Usage

Run HARDEN-SEC as root for a complete audit:

sudo python3 main.py --format txt
sudo python3 main.py --format json
sudo python3 main.py --format html


--format specifies the output report format (txt, json, or html).

Reports are saved in the reports/ directory.

Example Output

Console summary:

[+] Starting HARDEN-SEC in REAL mode
[*] Auditing system files...
[*] System audit completed (1 findings)
[*] Auditing services...
[*] Service audit completed (1 findings)
[*] Auditing configurations...
[*] Configuration audit completed (2 findings)

[+] Audit finished
[+] Security Score: 40/100
[+] Risk Level: HIGH
[+] Summary: {'CRITICAL': 1, 'HIGH': 2, 'MEDIUM': 1, 'LOW': 0}


JSON/HTML reports provide structured and visual representations of findings for documentation and SIEM integration.

Contributing

Contributions are welcome! You can help by:

Adding more CIS benchmark checks.

Auditing Docker containers or web services.

Improving report formatting and readability.

References

CIS Benchmarks

SSH Hardening Guide – Hackviser

Arch Linux Security Hardening Guide

License

This project is open-source and free to use under the MIT License.
