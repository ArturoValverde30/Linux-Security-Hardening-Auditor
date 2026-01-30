def run_config_audit():
    findings = []
    ssh_config = "/etc/ssh/sshd_config"

    try:
        with open(ssh_config) as f:
            content = f.read()

        checks = {
            "PermitRootLogin yes": ("CRITICAL", "SSH allows root login"),
            "PasswordAuthentication yes": ("HIGH", "SSH allows password authentication"),
            "Protocol 1": ("CRITICAL", "SSH uses insecure protocol 1")
        }

        for key, (sev, msg) in checks.items():
            if key in content:
                findings.append({
                    "severity": sev,
                    "message": msg
                })

    except FileNotFoundError:
        findings.append({
            "severity": "MEDIUM",
            "message": "sshd_config file not found"
        })

    return findings
