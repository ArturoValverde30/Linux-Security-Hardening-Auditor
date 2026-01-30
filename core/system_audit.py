import os
import stat

def run_system_audit():
    findings = []

    # /etc/passwd permissions
    try:
        st = os.stat("/etc/passwd")
        if st.st_mode & stat.S_IWOTH:
            findings.append({
                "severity": "CRITICAL",
                "message": "/etc/passwd is world writable"
            })
    except Exception as e:
        findings.append({
            "severity": "MEDIUM",
            "message": f"Cannot analyze /etc/passwd: {e}"
        })

    # /etc/shadow permissions
    try:
        st = os.stat("/etc/shadow")
        if st.st_mode & stat.S_IRWXO:
            findings.append({
                "severity": "CRITICAL",
                "message": "/etc/shadow has insecure permissions"
            })
    except Exception as e:
        findings.append({
            "severity": "MEDIUM",
            "message": f"Cannot analyze /etc/shadow: {e}"
        })

    # Users with UID 0
    try:
        with open("/etc/passwd") as f:
            for line in f:
                parts = line.split(":")
                if len(parts) > 2 and parts[2] == "0" and parts[0] != "root":
                    findings.append({
                        "severity": "HIGH",
                        "message": f"User with UID 0 detected: {parts[0]}"
                    })
    except Exception as e:
        findings.append({
            "severity": "MEDIUM",
            "message": f"Cannot analyze users: {e}"
        })

    return findings
