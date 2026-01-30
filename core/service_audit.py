import subprocess

INSECURE_SERVICES = ["telnet", "ftp", "rsh", "rexec"]

def run_service_audit():
    findings = []

    try:
        output = subprocess.check_output(
            ["systemctl", "list-units", "--type=service", "--state=running"],
            stderr=subprocess.DEVNULL,
            text=True
        )
        for service in INSECURE_SERVICES:
            if service in output:
                findings.append({
                    "severity": "HIGH",
                    "message": f"Insecure service running: {service}"
                })
    except Exception:
        findings.append({
            "severity": "MEDIUM",
            "message": "Cannot query running services (systemctl failed)"
        })

    return findings
